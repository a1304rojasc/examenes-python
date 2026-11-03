"""Bloque 10 · Examen fácil — soluciones comentadas."""
import argparse
from datetime import datetime


def parsear_marca_tiempo(texto, anio=2026):
    """datetime desde "Mar 10 08:15:01" (syslog no incluye el año)."""
    limpio = " ".join(texto.split())           # "Mar  9" -> "Mar 9"
    return datetime.strptime(f"{anio} {limpio}", "%Y %b %d %H:%M:%S")


def dentro_de_ventana(t1, t2, segundos):
    """True si |t2 - t1| <= segundos."""
    return abs((t2 - t1).total_seconds()) <= segundos


def max_en_ventana(tiempos, ventana):
    """Máximo de eventos en cualquier intervalo de 'ventana' segundos."""
    t = sorted(tiempos)          # imprescindible: la entrada puede venir desordenada
    mejor = 0
    inicio = 0
    for fin in range(len(t)):
        # Encogemos la ventana por la izquierda hasta que vuelva a caber.
        while t[fin] - t[inicio] > ventana:
            inicio += 1
        mejor = max(mejor, fin - inicio + 1)
    return mejor


def crear_parser():
    """ArgumentParser con archivo, --umbral, --ventana y --json."""
    parser = argparse.ArgumentParser(description="Detector de fuerza bruta SSH")
    parser.add_argument("archivo", help="ruta del auth.log a analizar")
    parser.add_argument("--umbral", type=int, default=5, help="fallos para alertar (5)")
    parser.add_argument("--ventana", type=int, default=60, help="segundos de la ventana (60)")
    parser.add_argument("--json", action="store_true", help="salida en JSON")
    return parser


def es_fuerza_bruta(tiempos, umbral, ventana):
    """True si hay al menos 'umbral' eventos dentro de una ventana."""
    return max_en_ventana(tiempos, ventana) >= umbral
