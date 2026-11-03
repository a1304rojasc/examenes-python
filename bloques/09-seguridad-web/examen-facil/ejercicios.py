"""Bloque 09 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 09 facil
"""


import html
import re

COLUMNAS_PERMITIDAS = {"id", "nombre", "email"}


def validar_usuario(nombre):
    """True si nombre tiene 3-16 caracteres de [a-z0-9_]."""
    raise NotImplementedError("Implementa validar_usuario")


def escapar_html(texto):
    """Escapa &, <, >, " y ' para insertar texto en HTML de forma segura."""
    raise NotImplementedError("Implementa escapar_html")


def crear_tabla(con):
    """Crea la tabla usuarios(id, nombre UNIQUE NOT NULL, email)."""
    raise NotImplementedError("Implementa crear_tabla")


def insertar_usuario(con, nombre, email):
    """Inserta un usuario con parámetros, hace commit y devuelve su id."""
    raise NotImplementedError("Implementa insertar_usuario")


def buscar_usuario(con, nombre):
    """(id, nombre, email) del usuario o None. Consulta parametrizada."""
    raise NotImplementedError("Implementa buscar_usuario")


def columna_orden(campo):
    """Devuelve campo si está en la allowlist; si no, ValueError."""
    raise NotImplementedError("Implementa columna_orden")
