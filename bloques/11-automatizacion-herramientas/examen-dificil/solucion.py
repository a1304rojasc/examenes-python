"""Bloque 11 · Examen difícil — soluciones comentadas (datos de ejemplo, sin red)."""
import argparse
import ipaddress

_NIVELES = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def rango_de_puertos(texto):
    """'inicio-fin' -> (inicio, fin) validando 1..65535 e inicio <= fin."""
    partes = texto.split("-")
    if len(partes) != 2:
        raise argparse.ArgumentTypeError("formato esperado: inicio-fin")
    try:
        inicio, fin = int(partes[0]), int(partes[1])
    except ValueError:
        raise argparse.ArgumentTypeError("los puertos deben ser enteros")
    if not (1 <= inicio <= 65535 and 1 <= fin <= 65535):
        raise argparse.ArgumentTypeError("puertos fuera de rango (1-65535)")
    if inicio > fin:
        raise argparse.ArgumentTypeError("el inicio no puede ser mayor que el fin")
    return (inicio, fin)


def filtrar_por_nivel(lineas, minimo):
    """Líneas cuyo nivel es >= 'minimo' en el orden DEBUG<INFO<WARNING<ERROR<CRITICAL."""
    umbral = _NIVELES.index(minimo)
    resultado = []
    for linea in lineas:
        # El nivel va entre corchetes al inicio: "[INFO] ...".
        if linea.startswith("[") and "]" in linea:
            nivel = linea[1:linea.index("]")]
            if nivel in _NIVELES and _NIVELES.index(nivel) >= umbral:
                resultado.append(linea)
    return resultado


def consultar_con_cache(cliente, clave, cache):
    """Devuelve cache[clave]; si no está, llama a cliente(clave), lo guarda y lo devuelve."""
    if clave in cache:
        return cache[clave]            # acierto de caché: no se llama al cliente
    valor = cliente(clave)
    cache[clave] = valor
    return valor


def resumen_shodan(respuesta):
    """{'puertos': [ordenados y únicos], 'servicios': {puerto: product}}."""
    puertos = sorted(set(respuesta.get("ports", [])))
    servicios = {}
    for servicio in respuesta.get("data", []):
        servicios[servicio["port"]] = servicio.get("product")
    return {"puertos": puertos, "servicios": servicios}


def consolidar_iocs(feeds):
    """Consolida ips (válidas, únicas, ordenadas) y dominios (minúsculas, únicos)."""
    ips, dominios = set(), set()
    for feed in feeds:
        for texto in feed.get("ips", []):
            try:
                ips.add(ipaddress.ip_address(texto))   # descarta inválidas (ValueError)
            except ValueError:
                pass
        for dominio in feed.get("dominios", []):
            dominios.add(dominio.strip().lower())
    return {
        "ips": [str(ip) for ip in sorted(ips)],         # sorted ordena numéricamente
        "dominios": sorted(dominios),
    }
