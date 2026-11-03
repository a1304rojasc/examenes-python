"""Bloque 10 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 10 facil
"""


import argparse
from datetime import datetime


def parsear_marca_tiempo(texto, anio=2026):
    """datetime desde "Mar 10 08:15:01" (syslog no incluye el año)."""
    raise NotImplementedError("Implementa parsear_marca_tiempo")


def dentro_de_ventana(t1, t2, segundos):
    """True si |t2 - t1| <= segundos."""
    raise NotImplementedError("Implementa dentro_de_ventana")


def max_en_ventana(tiempos, ventana):
    """Máximo de eventos en cualquier intervalo de 'ventana' segundos."""
    raise NotImplementedError("Implementa max_en_ventana")


def crear_parser():
    """ArgumentParser con archivo, --umbral, --ventana y --json."""
    raise NotImplementedError("Implementa crear_parser")


def es_fuerza_bruta(tiempos, umbral, ventana):
    """True si hay al menos 'umbral' eventos dentro de una ventana."""
    raise NotImplementedError("Implementa es_fuerza_bruta")
