"""Bloque 09 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 09 dificil
"""


import ipaddress
from html.parser import HTMLParser
from urllib.parse import urlsplit


def buscar_productos(con, texto, orden="nombre", limite=10):
    """Productos cuyo nombre contiene 'texto', con orden (allowlist) y límite 1-100."""
    raise NotImplementedError("Implementa buscar_productos")


def reflejo_sin_escapar(valor, respuesta):
    """True si 'valor' lleva < o > y aparece literal (sin escapar) en la respuesta."""
    raise NotImplementedError("Implementa reflejo_sin_escapar")


def destino_seguro(url, dominio_permitido):
    """True si la redirección se queda dentro del sitio permitido."""
    raise NotImplementedError("Implementa destino_seguro")


def apunta_a_interno(url):
    """True si el host es localhost o una IP privada/loopback/enlace local/reservada."""
    raise NotImplementedError("Implementa apunta_a_interno")


def inventario_formularios(html):
    """Lista de formularios con accion, metodo, campos y token_csrf."""
    raise NotImplementedError("Implementa inventario_formularios")
