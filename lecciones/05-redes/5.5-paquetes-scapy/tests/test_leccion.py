"""Tests de la lección 5.5. No necesitan root ni red: paquetes en memoria y pcaps temporales."""

import pytest
from scapy.all import IP, TCP, UDP, Ether, Raw, wrpcap

# MACs fijas: un Ether(**MAC) vacío hace que Scapy pregunte por ARP en la red.
MAC = dict(src="02:00:00:00:00:01", dst="02:00:00:00:00:02")


def test_ej1_sonda_es_un_syn(m):
    p = m.construir_sonda("127.0.0.1", 22)
    assert p.haslayer(IP) and p.haslayer(TCP)
    assert p[IP].dst == "127.0.0.1"
    assert p[TCP].dport == 22 and p[TCP].sport == 40000
    assert p[TCP].flags == "S"
    assert not p.haslayer(Raw)


def test_ej1_puerto_origen_configurable(m):
    p = m.construir_sonda("192.0.2.10", 8080, puerto_origen=51515)
    assert (p[IP].dst, p[TCP].sport, p[TCP].dport) == ("192.0.2.10", 51515, 8080)
    assert IP(bytes(p))[TCP].flags == "S"  # sobrevive a la serialización


def test_ej2_capas_http(m):
    trama = bytes(Ether(**MAC) / IP(src="192.168.1.5", dst="192.0.2.1") / TCP(dport=80, flags="PA") / Raw(b"GET / HTTP/1.1\r\n\r\n"))
    assert m.capas(trama) == ["Ether", "IP", "TCP", "Raw"]
    assert m.datos_de_aplicacion(trama) == b"GET / HTTP/1.1\r\n\r\n"


def test_ej2_capas_sin_datos(m):
    trama = bytes(Ether(**MAC) / IP(dst="192.0.2.53") / UDP(dport=53))
    assert m.capas(trama) == ["Ether", "IP", "UDP"]
    assert m.datos_de_aplicacion(trama) == b""


@pytest.fixture
def captura(tmp_path):
    paquetes = []
    # escáner: SYN a 25 puertos distintos
    for puerto in range(20, 45):
        paquetes.append(Ether(**MAC) / IP(src="198.51.100.7", dst="192.168.1.10") / TCP(sport=50000, dport=puerto, flags="S"))
    # cliente normal: muchos SYN, pero siempre al 443
    for _ in range(30):
        paquetes.append(Ether(**MAC) / IP(src="192.168.1.20", dst="192.0.2.80") / TCP(sport=40001, dport=443, flags="S"))
    # servidor que responde SYN-ACK desde muchos puertos: no es escaneo
    for puerto in range(1000, 1020):
        paquetes.append(Ether(**MAC) / IP(src="192.168.1.10", dst="198.51.100.7") / TCP(sport=puerto, dport=puerto, flags="SA"))
    # escáner pequeño: 10 puertos exactos
    for puerto in (21, 22, 23, 25, 53, 80, 110, 143, 443, 445):
        paquetes.append(Ether(**MAC) / IP(src="203.0.113.9", dst="192.168.1.10") / TCP(dport=puerto, flags="S"))
    # tráfico UDP de relleno
    paquetes.append(Ether(**MAC) / IP(src="192.168.1.30", dst="192.0.2.53") / UDP(dport=53))
    ruta = tmp_path / "captura.pcap"
    wrpcap(str(ruta), paquetes)
    return ruta


def test_ej3_detecta_escaneos(m, captura):
    assert m.sospechosos_de_escaneo(captura) == {"198.51.100.7": 25, "203.0.113.9": 10}


def test_ej3_umbral(m, captura):
    assert m.sospechosos_de_escaneo(captura, umbral=11) == {"198.51.100.7": 25}
    assert m.sospechosos_de_escaneo(captura, umbral=100) == {}
