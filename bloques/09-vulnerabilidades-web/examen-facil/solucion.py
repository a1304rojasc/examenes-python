"""Bloque 9 · Examen fácil — soluciones comentadas (defensivo, SQLite en memoria)."""
import html
import re
from html.parser import HTMLParser
from urllib.parse import urlsplit

PATRON_SQLI = re.compile(r"'\s*(or|and)\b|--|;|/\*|\bunion\b.*\bselect\b", re.IGNORECASE)


class _BuscadorCsrf(HTMLParser):
    """Encuentra el valor del primer input cuyo nombre contiene 'csrf'."""

    def __init__(self):
        super().__init__()
        self.token = None

    def handle_starttag(self, tag, attrs):
        if tag == "input" and self.token is None:
            atributos = dict(attrs)
            nombre = atributos.get("name") or ""
            if "csrf" in nombre.lower():
                self.token = atributos.get("value")


def buscar_usuario(con, nombre):
    """(id, nombre, email) del usuario, o None. Consulta parametrizada."""
    # El ? mantiene 'nombre' como dato: ' OR '1'='1 no altera la consulta.
    cur = con.execute("SELECT id, nombre, email FROM usuarios WHERE nombre = ?", (nombre,))
    return cur.fetchone()


def parece_sqli(entrada):
    """True si la entrada contiene patrones típicos de inyección SQL (para alertar)."""
    return PATRON_SQLI.search(entrada) is not None


def escapar_html(texto):
    """Escapa &, <, >, \" y ' para insertar texto en HTML de forma segura."""
    return html.escape(texto, quote=True)


def extraer_token_csrf(html_texto):
    """Valor del primer campo oculto con 'csrf' en el nombre, o None."""
    parser = _BuscadorCsrf()
    parser.feed(html_texto)
    return parser.token


def url_permitida(url, hosts_permitidos):
    """True si el esquema es http/https y el host está en la allowlist."""
    partes = urlsplit(url)
    return partes.scheme in ("http", "https") and partes.hostname in hosts_permitidos
