"""Bloque 06 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 06 facil
"""


import re


def normalizar_espacios(texto):
    """Quita espacios en los extremos y deja uno solo entre palabras."""
    raise NotImplementedError("Implementa normalizar_espacios")


def extraer_ips(texto):
    """Lista de cadenas con forma IPv4 (n.n.n.n) en orden de aparición."""
    raise NotImplementedError("Implementa extraer_ips")


def es_linea_fallida(linea):
    """True si la línea contiene "Failed password"."""
    raise NotImplementedError("Implementa es_linea_fallida")


def extraer_usuario(linea):
    """Usuario de una línea Failed/Accepted de sshd, o None."""
    raise NotImplementedError("Implementa extraer_usuario")


def es_email_valido(texto):
    """True si todo el texto tiene forma usuario@dominio.tld."""
    raise NotImplementedError("Implementa es_email_valido")
