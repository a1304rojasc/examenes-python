"""Bloque 08 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 08 dificil
"""


import math
from html.parser import HTMLParser


def tiempo_fuerza_bruta(longitud, tamano_alfabeto, intentos_por_segundo):
    """Segundos para agotar el espacio de claves a esa velocidad (peor caso)."""
    raise NotImplementedError("Implementa tiempo_fuerza_bruta")


def entropia_bits(password):
    """Entropía aproximada: longitud * log2(tamaño del alfabeto usado)."""
    raise NotImplementedError("Implementa entropia_bits")


def fuzzear(funcion, entradas):
    """Devuelve las entradas que hacen que 'funcion' lance una excepción."""
    raise NotImplementedError("Implementa fuzzear")


def analizar_formulario(html):
    """{'accion', 'metodo', 'campos'} del primer formulario del HTML."""
    raise NotImplementedError("Implementa analizar_formulario")


def endpoints_inseguros(endpoints):
    """Rutas (ordenadas) de endpoints de escritura que no exigen autenticación."""
    raise NotImplementedError("Implementa endpoints_inseguros")
