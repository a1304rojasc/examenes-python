"""Bloque 08 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 08 facil
"""


import base64
import hashlib


def codificar_b64(texto):
    """Texto UTF-8 -> cadena Base64."""
    raise NotImplementedError("Implementa codificar_b64")


def decodificar_b64(b64):
    """Cadena Base64 -> texto UTF-8."""
    raise NotImplementedError("Implementa decodificar_b64")


def sha256_hex(texto):
    """SHA-256 en hexadecimal del texto codificado en UTF-8."""
    raise NotImplementedError("Implementa sha256_hex")


def cesar(texto, desplazamiento):
    """Cifrado César sobre A-Z y a-z; el resto de caracteres no cambia."""
    raise NotImplementedError("Implementa cesar")


def descifrar_cesar(texto, desplazamiento):
    """Deshace cesar(): desplazar en sentido contrario."""
    raise NotImplementedError("Implementa descifrar_cesar")


def verificar_integridad(ruta, hash_esperado):
    """True si el SHA-256 del archivo coincide con hash_esperado."""
    raise NotImplementedError("Implementa verificar_integridad")
