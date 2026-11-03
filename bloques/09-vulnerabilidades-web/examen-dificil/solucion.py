"""Bloque 9 · Examen difícil — soluciones comentadas (defensivo)."""
import ipaddress
from html.parser import HTMLParser
from urllib.parse import urlsplit

_ORDEN_PERMITIDO = {"nombre", "precio", "id"}


class _Formularios(HTMLParser):
    """Recorre todos los <form> y, dentro de cada uno, sus campos y token CSRF."""

    def __init__(self):
        super().__init__()
        self.formularios = []
        self._actual = None

    def handle_starttag(self, tag, attrs):
        atributos = dict(attrs)
        if tag == "form":
            self._actual = {"accion": atributos.get("action"),
                            "metodo": (atributos.get("method") or "get").lower(),
                            "campos": [], "token_csrf": None}
            self.formularios.append(self._actual)
        elif tag in ("input", "textarea", "select") and self._actual is not None:
            nombre = atributos.get("name")
            if nombre is not None:
                self._actual["campos"].append(nombre)
                if "csrf" in nombre.lower() and self._actual["token_csrf"] is None:
                    self._actual["token_csrf"] = atributos.get("value")

    def handle_endtag(self, tag):
        if tag == "form":
            self._actual = None


def buscar_productos(con, texto, orden="nombre", limite=10):
    """Productos cuyo nombre contiene 'texto', con orden (allowlist) y límite 1-100."""
    if orden not in _ORDEN_PERMITIDO:
        raise ValueError("campo de orden no permitido")
    if not isinstance(limite, int) or isinstance(limite, bool) or not 1 <= limite <= 100:
        raise ValueError("límite fuera de rango")
    # Escapamos los comodines de LIKE para buscarlos de forma literal.
    seguro = texto.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    sql = (f"SELECT id, nombre, precio FROM productos WHERE nombre LIKE ? ESCAPE '\\' "
           f"ORDER BY {orden}, id LIMIT ?")   # 'orden' validado por la allowlist
    return con.execute(sql, (f"%{seguro}%", limite)).fetchall()


def reflejo_sin_escapar(valor, respuesta):
    """True si 'valor' lleva < o > y aparece literal (sin escapar) en la respuesta."""
    tiene_html = "<" in valor or ">" in valor
    return tiene_html and valor in respuesta


def destino_seguro(url, dominio_permitido):
    """True si la redirección se queda dentro del sitio permitido."""
    partes = urlsplit(url)
    if partes.scheme and partes.scheme not in ("http", "https"):
        return False
    if partes.netloc:                       # hay host: debe ser exactamente el permitido
        return partes.hostname == dominio_permitido
    # Sin host: solo rutas que no intenten saltar a otro dominio (// o /\).
    return url.startswith("/") and not url.startswith("//") and not url.startswith("/\\")


def apunta_a_interno(url):
    """True si el host es localhost o una IP privada/loopback/enlace local/reservada."""
    host = urlsplit(url).hostname
    if host is None:
        return False
    if host == "localhost":
        return True
    try:
        ip = ipaddress.ip_address(host)
    except ValueError:
        return False                        # es un nombre de dominio: aquí no se resuelve
    return ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_reserved


def inventario_formularios(html):
    """Lista de formularios con accion, metodo, campos y token_csrf."""
    parser = _Formularios()
    parser.feed(html)
    return parser.formularios
