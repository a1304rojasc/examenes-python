"""Bloque 05 · Examen fácil — soluciones comentadas."""
from pathlib import Path


def contar_lineas(ruta):
    """Devuelve el número de líneas del archivo."""
    with open(ruta, encoding="utf-8") as f:
        # Iterar sobre el archivo recorre línea a línea sin cargarlo entero.
        return sum(1 for _ in f)


def escribir_lineas(ruta, lineas):
    """Escribe cada cadena en una línea terminada en "\\n" (sobrescribe)."""
    with open(ruta, "w", encoding="utf-8") as f:
        for linea in lineas:
            f.write(linea + "\n")


def dividir_seguro(a, b):
    """Devuelve a / b o None si b es 0 (capturando ZeroDivisionError)."""
    try:
        return a / b
    except ZeroDivisionError:
        return None


def leer_config(ruta):
    """Lee líneas clave=valor a un dict; ignora vacías y comentarios (#).

    Si el archivo no existe devuelve {}.
    """
    config = {}
    try:
        with open(ruta, encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea or linea.startswith("#"):
                    continue
                # partition separa solo por el PRIMER "=" (el valor puede tener "=").
                clave, _, valor = linea.partition("=")
                config[clave.strip()] = valor.strip()
    except FileNotFoundError:
        return {}
    return config


def extension(ruta):
    """Extensión en minúsculas sin punto ("logs/Auth.LOG" -> "log")."""
    return Path(ruta).suffix.lower().lstrip(".")
