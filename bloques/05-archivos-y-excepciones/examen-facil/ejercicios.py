"""Bloque 05 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 05 facil
"""


from pathlib import Path


def contar_lineas(ruta):
    """Devuelve el número de líneas del archivo."""
    raise NotImplementedError("Implementa contar_lineas")


def escribir_lineas(ruta, lineas):
    """Escribe cada cadena en una línea terminada en "\\n" (sobrescribe)."""
    raise NotImplementedError("Implementa escribir_lineas")


def dividir_seguro(a, b):
    """Devuelve a / b o None si b es 0 (capturando ZeroDivisionError)."""
    raise NotImplementedError("Implementa dividir_seguro")


def leer_config(ruta):
    """Lee líneas clave=valor a un dict; ignora vacías y comentarios (#).

    Si el archivo no existe devuelve {}.
    """
    raise NotImplementedError("Implementa leer_config")


def extension(ruta):
    """Extensión en minúsculas sin punto ("logs/Auth.LOG" -> "log")."""
    raise NotImplementedError("Implementa extension")
