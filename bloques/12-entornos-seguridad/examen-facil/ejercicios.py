"""Bloque 12 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 12 facil
"""


import re


def necesita_privilegios(puerto):
    """True si el puerto es privilegiado (< 1024)."""
    raise NotImplementedError("Implementa necesita_privilegios")


def xor_repetida(datos, clave):
    """XOR byte a byte de 'datos' con 'clave' repetida. Cifra y descifra igual."""
    raise NotImplementedError("Implementa xor_repetida")


def buscar_flag(texto):
    """Primera cadena con formato FLAG{...}, o None."""
    raise NotImplementedError("Implementa buscar_flag")


def contar_por_severidad(eventos):
    """{severidad: número de eventos} a partir de una lista de registros."""
    raise NotImplementedError("Implementa contar_por_severidad")


def opciones_modulo(lineas):
    """{OPCION: valor} de las líneas 'set OPCION valor' (la última gana)."""
    raise NotImplementedError("Implementa opciones_modulo")
