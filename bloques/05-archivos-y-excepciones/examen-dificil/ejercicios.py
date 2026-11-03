"""Bloque 05 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 05 dificil
"""


from pathlib import Path

NIVELES = {"INFO", "WARN", "ERROR"}


def convertir_enteros(valores, defecto=0):
    """Convierte cada valor a int; los no convertibles se cambian por defecto."""
    raise NotImplementedError("Implementa convertir_enteros")


def registrar(ruta, nivel, mensaje):
    """Añade "NIVEL: mensaje" al log y devuelve el total de líneas.

    Lanza ValueError si el nivel no es INFO, WARN o ERROR.
    """
    raise NotImplementedError("Implementa registrar")


def buscar_archivos(directorio, ext):
    """Rutas relativas (texto con "/") de archivos *.ext en todo el árbol, ordenadas."""
    raise NotImplementedError("Implementa buscar_archivos")


def copiar_filtrando(origen, destino, palabra):
    """Copia a destino las líneas de origen que contienen palabra (sin mayúsculas).

    Devuelve cuántas líneas se copiaron. Si origen no existe, salta
    FileNotFoundError antes de crear destino.
    """
    raise NotImplementedError("Implementa copiar_filtrando")


def ruta_segura(base, nombre):
    """Ruta absoluta de base/nombre; ValueError si se sale de base (path traversal)."""
    raise NotImplementedError("Implementa ruta_segura")
