"""Bloque 07 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 07 facil
"""


import ipaddress
import socket
from urllib.parse import urlsplit

PUERTOS_POR_DEFECTO = {"http": 80, "https": 443}


def es_ip_valida(texto):
    """True si texto es una IPv4 o IPv6 válida."""
    raise NotImplementedError("Implementa es_ip_valida")


def en_red(ip, cidr):
    """True si la IP pertenece a la red CIDR."""
    raise NotImplementedError("Implementa en_red")


def info_red(cidr):
    """{"red", "broadcast", "mascara", "hosts"} de una red CIDR."""
    raise NotImplementedError("Implementa info_red")


def eco_socketpair(mensaje):
    """Envía mensaje por un socket de un par conectado y devuelve lo recibido."""
    raise NotImplementedError("Implementa eco_socketpair")


def parsear_url(url):
    """(esquema, host, puerto) de una URL; puerto 80/443 por defecto."""
    raise NotImplementedError("Implementa parsear_url")
