"""Bloque 10 · Examen difícil — soluciones comentadas."""
import argparse
import ipaddress
import json
import re
from datetime import datetime

PATRON_FALLO = re.compile(
    r"^(?P<fecha>\w{3}\s+\d{1,2} \d{2}:\d{2}:\d{2}) \S+ sshd\[\d+\]: "
    r"Failed password for (?:invalid user )?\S+ from (?P<ip>\S+) port \d+"
)


def _max_en_ventana(tiempos, ventana):
    """Ventana deslizante con dos índices sobre tiempos (en segundos)."""
    t = sorted(tiempos)
    mejor, inicio = 0, 0
    for fin in range(len(t)):
        while t[fin] - t[inicio] > ventana:
            inicio += 1
        mejor = max(mejor, fin - inicio + 1)
    return mejor


def detectar_fuerza_bruta(lineas, umbral=5, ventana=60, anio=2026):
    """{ip: máximo de fallos en una ventana} para IPs que alcanzan el umbral."""
    tiempos_por_ip = {}
    for linea in lineas:
        m = PATRON_FALLO.search(linea)
        if not m:
            continue
        try:
            ip = str(ipaddress.ip_address(m["ip"]))   # descarta "IPs" falsas
        except ValueError:
            continue
        fecha = " ".join(m["fecha"].split())
        instante = datetime.strptime(f"{anio} {fecha}", "%Y %b %d %H:%M:%S")
        tiempos_por_ip.setdefault(ip, []).append(instante.timestamp())
    alertas = {}
    for ip, tiempos in tiempos_por_ip.items():
        maximo = _max_en_ventana(tiempos, ventana)
        if maximo >= umbral:
            alertas[ip] = maximo
    return alertas


def generar_informe(alertas, como_json=False):
    """Informe en texto (una línea por IP, más fallos primero) o JSON."""
    if como_json:
        return json.dumps(alertas, sort_keys=True)
    if not alertas:
        return "Sin alertas"
    orden = sorted(alertas.items(), key=lambda par: (-par[1], ipaddress.ip_address(par[0])))
    return "\n".join(f"ALERTA {ip}: {n} fallos en ventana" for ip, n in orden)


def main(argv):
    """CLI: analiza el log, imprime el informe y devuelve 1 si hay alertas."""
    parser = argparse.ArgumentParser(description="Detector de fuerza bruta SSH")
    parser.add_argument("archivo")
    parser.add_argument("--umbral", type=int, default=5)
    parser.add_argument("--ventana", type=int, default=60)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    with open(args.archivo, encoding="utf-8", errors="replace") as f:
        alertas = detectar_fuerza_bruta(f, args.umbral, args.ventana)
    print(generar_informe(alertas, como_json=args.json))
    return 1 if alertas else 0


def reglas_bloqueo(ips, allowlist):
    """["DENY ip", ...] ordenadas y sin repetir, excluyendo la allowlist."""
    redes = [ipaddress.ip_network(r, strict=False) for r in allowlist]
    candidatas = {ipaddress.ip_address(ip) for ip in ips}       # set: sin repetidos
    bloquear = [ip for ip in candidatas if not any(ip in red for red in redes)]
    return [f"DENY {ip}" for ip in sorted(bloquear)]


def verificar_detector(detector):
    """Lanza AssertionError si detector(tiempos, umbral, ventana) es incorrecto."""
    # Caso básico positivo y negativo.
    assert detector([0, 10, 20, 30, 40], 5, 60) is True
    assert detector([0, 100, 200, 300, 400], 5, 60) is False
    # Límite del umbral: exactamente 'umbral' eventos debe alertar (>=, no >).
    assert detector([0, 1, 2], 3, 10) is True
    assert detector([0, 1], 3, 10) is False
    # Límite de la ventana: diferencia == ventana cuenta (inclusiva).
    assert detector([0, 60], 2, 60) is True
    assert detector([0, 61], 2, 60) is False
    # Entrada desordenada.
    assert detector([50, 0, 400, 10, 30, 20], 5, 60) is True
    assert detector([300, 0, 600, 100, 200], 2, 60) is False
    # Muchos eventos en total pero dispersos: no es fuerza bruta.
    assert detector(list(range(0, 1000, 100)), 3, 60) is False
    # Lista vacía.
    assert detector([], 1, 60) is False
