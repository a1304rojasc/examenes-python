"""Bloque 11 · Examen fácil — soluciones comentadas (datos de ejemplo, sin red)."""
import argparse


def crear_parser():
    """Parser con subcomandos 'escanear' y 'reportar'."""
    parser = argparse.ArgumentParser(description="Herramienta de seguridad")
    # dest="comando" guarda qué subcomando se usó.
    sub = parser.add_subparsers(dest="comando")

    escanear = sub.add_parser("escanear", help="escanea un objetivo")
    escanear.add_argument("objetivo")
    escanear.add_argument("--puertos", default="1-1024")

    reportar = sub.add_parser("reportar", help="genera un informe")
    reportar.add_argument("archivo")
    reportar.add_argument("--json", action="store_true")
    return parser


def linea_log(nivel, mensaje, campos):
    """'[NIVEL] mensaje' y, si hay campos, ' | k=v ...' ordenados por clave."""
    linea = f"[{nivel}] {mensaje}"
    if campos:
        extra = " ".join(f"{clave}={campos[clave]}" for clave in sorted(campos))
        linea += f" | {extra}"
    return linea


def detecciones_vt(respuesta):
    """Número de motores que marcaron el archivo como malicioso (0 si falta algo)."""
    # get encadenado: si cualquier nivel falta, acabamos en {} o en 0.
    datos = respuesta.get("data", {})
    atributos = datos.get("attributes", {})
    stats = atributos.get("last_analysis_stats", {})
    return stats.get("malicious", 0)


def veces_filtrada(respuesta, sufijo):
    """Conteo asociado al sufijo en una respuesta tipo HIBP (0 si no está)."""
    objetivo = sufijo.strip().upper()
    for linea in respuesta.splitlines():
        if ":" in linea:
            suf, _, conteo = linea.partition(":")
            if suf.strip().upper() == objetivo:
                return int(conteo)
    return 0


def leer_api_key(entorno, nombre):
    """Devuelve la clave del 'entorno' o lanza un error si falta o está vacía."""
    valor = entorno.get(nombre)
    if not valor:
        raise ValueError(f"falta la variable de entorno {nombre}")
    return valor
