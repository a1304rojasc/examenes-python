"""Bloque 11 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 11 facil
"""


import argparse


def crear_parser():
    """Parser con subcomandos 'escanear' y 'reportar'."""
    raise NotImplementedError("Implementa crear_parser")


def linea_log(nivel, mensaje, campos):
    """'[NIVEL] mensaje' y, si hay campos, ' | k=v ...' ordenados por clave."""
    raise NotImplementedError("Implementa linea_log")


def detecciones_vt(respuesta):
    """Número de motores que marcaron el archivo como malicioso (0 si falta algo)."""
    raise NotImplementedError("Implementa detecciones_vt")


def veces_filtrada(respuesta, sufijo):
    """Conteo asociado al sufijo en una respuesta tipo HIBP (0 si no está)."""
    raise NotImplementedError("Implementa veces_filtrada")


def leer_api_key(entorno, nombre):
    """Devuelve la clave del 'entorno' o lanza un error si falta o está vacía."""
    raise NotImplementedError("Implementa leer_api_key")
