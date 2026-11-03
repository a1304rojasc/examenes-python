"""Bloque 05 · Examen difícil — soluciones comentadas."""
from pathlib import Path

NIVELES = {"INFO", "WARN", "ERROR"}


def convertir_enteros(valores, defecto=0):
    """Convierte cada valor a int; los no convertibles se cambian por defecto."""
    resultado = []
    for valor in valores:
        try:
            resultado.append(int(valor))
        except (ValueError, TypeError):   # "abc" -> ValueError, None -> TypeError
            resultado.append(defecto)
    return resultado


def registrar(ruta, nivel, mensaje):
    """Añade "NIVEL: mensaje" al log y devuelve el total de líneas.

    Lanza ValueError si el nivel no es INFO, WARN o ERROR.
    """
    if nivel not in NIVELES:
        raise ValueError(f"nivel desconocido: {nivel}")
    with open(ruta, "a", encoding="utf-8") as f:   # "a": nunca borra lo anterior
        f.write(f"{nivel}: {mensaje}\n")
    with open(ruta, encoding="utf-8") as f:
        return len(f.readlines())


def buscar_archivos(directorio, ext):
    """Rutas relativas (texto con "/") de archivos *.ext en todo el árbol, ordenadas."""
    base = Path(directorio)
    ext = ext.lstrip(".")
    return sorted(
        p.relative_to(base).as_posix()        # as_posix() usa "/" también en Windows
        for p in base.rglob(f"*.{ext}")
        if p.is_file()
    )


def copiar_filtrando(origen, destino, palabra):
    """Copia a destino las líneas de origen que contienen palabra (sin mayúsculas).

    Devuelve cuántas líneas se copiaron. Si origen no existe, salta
    FileNotFoundError antes de crear destino.
    """
    # Abrimos primero el origen: si falla, nunca llegamos a crear el destino.
    with open(origen, encoding="utf-8") as entrada:
        lineas = [l for l in entrada if palabra.lower() in l.lower()]
    with open(destino, "w", encoding="utf-8") as salida:
        salida.writelines(lineas)
    return len(lineas)


def ruta_segura(base, nombre):
    """Ruta absoluta de base/nombre; ValueError si se sale de base (path traversal)."""
    base = Path(base).resolve()
    destino = (base / nombre).resolve()    # resuelve "..", enlaces, etc.
    if not destino.is_relative_to(base):   # Python 3.9+
        raise ValueError(f"ruta fuera del directorio permitido: {nombre}")
    return destino
