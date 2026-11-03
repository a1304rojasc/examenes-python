"""Bloque 10 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 10 dificil
"""


import argparse
import ipaddress
import json
import re
from datetime import datetime


def _max_en_ventana(tiempos, ventana):
    """Ventana deslizante con dos índices sobre tiempos (en segundos)."""
    raise NotImplementedError("Implementa _max_en_ventana")


def detectar_fuerza_bruta(lineas, umbral=5, ventana=60, anio=2026):
    """{ip: máximo de fallos en una ventana} para IPs que alcanzan el umbral."""
    raise NotImplementedError("Implementa detectar_fuerza_bruta")


def generar_informe(alertas, como_json=False):
    """Informe en texto (una línea por IP, más fallos primero) o JSON."""
    raise NotImplementedError("Implementa generar_informe")


def main(argv):
    """CLI: analiza el log, imprime el informe y devuelve 1 si hay alertas."""
    raise NotImplementedError("Implementa main")


def reglas_bloqueo(ips, allowlist):
    """["DENY ip", ...] ordenadas y sin repetir, excluyendo la allowlist."""
    raise NotImplementedError("Implementa reglas_bloqueo")


def verificar_detector(detector):
    """Lanza AssertionError si detector(tiempos, umbral, ventana) es incorrecto."""
    raise NotImplementedError("Implementa verificar_detector")
