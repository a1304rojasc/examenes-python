"""Bloque 09 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 09 facil
"""


import html
import re
from html.parser import HTMLParser
from urllib.parse import urlsplit


def buscar_usuario(con, nombre):
    """(id, nombre, email) del usuario, o None. Consulta parametrizada."""
    raise NotImplementedError("Implementa buscar_usuario")


def parece_sqli(entrada):
    """True si la entrada contiene patrones típicos de inyección SQL (para alertar)."""
    raise NotImplementedError("Implementa parece_sqli")


def escapar_html(texto):
    """Escapa &, <, >, \" y ' para insertar texto en HTML de forma segura."""
    raise NotImplementedError("Implementa escapar_html")


def extraer_token_csrf(html_texto):
    """Valor del primer campo oculto con 'csrf' en el nombre, o None."""
    raise NotImplementedError("Implementa extraer_token_csrf")


def url_permitida(url, hosts_permitidos):
    """True si el esquema es http/https y el host está en la allowlist."""
    raise NotImplementedError("Implementa url_permitida")
