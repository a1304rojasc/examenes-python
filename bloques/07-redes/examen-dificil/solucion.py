"""Bloque 07 · Examen difícil — soluciones comentadas."""
import ipaddress
import socket
from http import HTTPStatus


def agrupar_por_red(ips, prefijo):
    """{"red/prefijo": [ips ordenadas numéricamente]}."""
    grupos = {}
    for ip in ips:
        red = ipaddress.ip_network(f"{ip}/{prefijo}", strict=False)
        grupos.setdefault(str(red), []).append(ip)
    # key=ip_address compara como números, no como texto.
    return {red: sorted(lista, key=ipaddress.ip_address) for red, lista in grupos.items()}


def fuera_de_allowlist(ips, redes):
    """IPs (orden original) que no pertenecen a ninguna red permitida."""
    permitidas = [ipaddress.ip_network(r, strict=False) for r in redes]
    fuera = []
    for texto in ips:
        try:
            ip = ipaddress.ip_address(texto)
        except ValueError:
            fuera.append(texto)        # inválida = no permitida (seguro por defecto)
            continue
        if not any(ip in red for red in permitidas):
            fuera.append(texto)
    return fuera


def parsear_peticion(texto):
    """{"metodo", "ruta", "version", "cabeceras", "cuerpo"} de una petición HTTP."""
    cabecera, _, cuerpo = texto.partition("\r\n\r\n")   # línea vacía separa el cuerpo
    lineas = cabecera.split("\r\n")
    metodo, ruta, version = lineas[0].split(" ", 2)
    cabeceras = {}
    for linea in lineas[1:]:
        nombre, _, valor = linea.partition(":")
        cabeceras[nombre.strip().lower()] = valor.strip()   # nombres sin mayúsculas
    return {"metodo": metodo, "ruta": ruta, "version": version, "cabeceras": cabeceras, "cuerpo": cuerpo}


def respuesta_http(codigo, cuerpo):
    """Bytes de una respuesta HTTP/1.1 text/plain con Content-Length en bytes."""
    datos = cuerpo.encode("utf-8")                # longitud en BYTES, no caracteres
    estado = HTTPStatus(codigo)
    cabecera = (
        f"HTTP/1.1 {estado.value} {estado.phrase}\r\n"
        "Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(datos)}\r\n"
        "\r\n"
    )
    return cabecera.encode("ascii") + datos


def puerto_abierto(host, puerto, timeout=1.0):
    """True si se puede abrir una conexión TCP a host:puerto."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)                    # nunca esperar indefinidamente
        return s.connect_ex((host, puerto)) == 0
