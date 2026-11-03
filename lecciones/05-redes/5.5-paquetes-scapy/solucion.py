"""5.5 · Paquetes con Scapy — solución oficial."""

from collections import defaultdict

from scapy.all import IP, TCP, Ether, Raw, rdpcap


def construir_sonda(ip_destino, puerto, puerto_origen=40000):
    """Paquete IP/TCP con solo la flag SYN: el primer paso del handshake."""
    return IP(dst=ip_destino) / TCP(sport=puerto_origen, dport=puerto, flags="S")


def capas(trama):
    """Nombres de las capas de una trama Ethernet en bytes, de fuera hacia dentro."""
    p = Ether(trama)
    return [capa.__name__ for capa in p.layers()]


def datos_de_aplicacion(trama):
    """Bytes de la capa Raw (la carga útil), o b'' si no hay."""
    p = Ether(trama)
    return bytes(p[Raw].load) if p.haslayer(Raw) else b""


def sospechosos_de_escaneo(ruta, umbral=10):
    """IPs que mandaron SYN (sin ACK) a al menos 'umbral' puertos distintos."""
    puertos = defaultdict(set)
    for p in rdpcap(str(ruta)):
        if p.haslayer(IP) and p.haslayer(TCP) and p[TCP].flags == "S":
            puertos[p[IP].src].add(p[TCP].dport)
    return {ip: len(ps) for ip, ps in puertos.items() if len(ps) >= umbral}
