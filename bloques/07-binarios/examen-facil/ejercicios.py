"""Bloque 07 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 07 facil
"""


import struct


def permiso_activo(permisos, posicion):
    """True si el bit en 'posicion' (desde 0) está encendido."""
    raise NotImplementedError("Implementa permiso_activo")


def a_hex(datos):
    """Representación hex de los bytes, dos dígitos por byte, separados por espacio."""
    raise NotImplementedError("Implementa a_hex")


def leer_registro(datos):
    """Desempaqueta 4 bytes (uint32) + 2 bytes (int16), big-endian."""
    raise NotImplementedError("Implementa leer_registro")


def identificar_formato(datos):
    """Devuelve el formato según la firma inicial, o 'desconocido'."""
    raise NotImplementedError("Implementa identificar_formato")


def entero_desde_bytes(datos, orden):
    """Convierte bytes al entero que representan, con orden 'big' o 'little'."""
    raise NotImplementedError("Implementa entero_desde_bytes")
