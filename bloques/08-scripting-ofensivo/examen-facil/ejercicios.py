"""Bloque 08 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 08 facil
"""


from html.parser import HTMLParser


def extraer_campos_whois(texto):
    """Extrae registrar, creation date y registry expiry date (primera aparición)."""
    raise NotImplementedError("Implementa extraer_campos_whois")


def extraer_enlaces(html):
    """Lista de href de los enlaces del HTML, en orden de aparición."""
    raise NotImplementedError("Implementa extraer_enlaces")


def permitido_por_robots(reglas, ruta):
    """True si 'ruta' no empieza por ninguna regla Disallow (ignora reglas vacías)."""
    raise NotImplementedError("Implementa permitido_por_robots")


def puertos_abiertos(resultado):
    """Lista ordenada de los puertos con estado 'open'."""
    raise NotImplementedError("Implementa puertos_abiertos")


def combinaciones_posibles(longitud, tamano_alfabeto):
    """Número de contraseñas distintas: tamano_alfabeto ** longitud."""
    raise NotImplementedError("Implementa combinaciones_posibles")
