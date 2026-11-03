"""Bloque 8 · Examen fácil — soluciones comentadas (análisis local, sin red)."""
from html.parser import HTMLParser

_CAMPOS_WHOIS = ("registrar", "creation date", "registry expiry date")


class _Enlaces(HTMLParser):
    """Recolecta los href de las etiquetas <a>."""

    def __init__(self):
        super().__init__()
        self.enlaces = []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for clave, valor in attrs:
                if clave == "href" and valor is not None:
                    self.enlaces.append(valor)


def extraer_campos_whois(texto):
    """Extrae registrar, creation date y registry expiry date (primera aparición)."""
    datos = {}
    for linea in texto.splitlines():
        if ":" in linea:
            clave, _, valor = linea.partition(":")
            clave = clave.strip().lower()
            if clave in _CAMPOS_WHOIS and clave not in datos:
                datos[clave] = valor.strip()
    return datos


def extraer_enlaces(html):
    """Lista de href de los enlaces del HTML, en orden de aparición."""
    parser = _Enlaces()
    parser.feed(html)
    return parser.enlaces


def permitido_por_robots(reglas, ruta):
    """True si 'ruta' no empieza por ninguna regla Disallow (ignora reglas vacías)."""
    return not any(ruta.startswith(prohibida) for prohibida in reglas if prohibida)


def puertos_abiertos(resultado):
    """Lista ordenada de los puertos con estado 'open'."""
    return sorted(puerto for puerto, estado in resultado.items() if estado == "open")


def combinaciones_posibles(longitud, tamano_alfabeto):
    """Número de contraseñas distintas: tamano_alfabeto ** longitud."""
    return tamano_alfabeto ** longitud
