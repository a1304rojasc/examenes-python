"""Bloque 8 · Examen difícil — soluciones comentadas (local, sin red)."""
import math
from html.parser import HTMLParser

_METODOS_ESCRITURA = {"POST", "PUT", "PATCH", "DELETE"}


class _Formulario(HTMLParser):
    """Captura action/method del <form> y los name de sus campos."""

    def __init__(self):
        super().__init__()
        self.accion = None
        self.metodo = "get"
        self.campos = []

    def handle_starttag(self, tag, attrs):
        atributos = dict(attrs)
        if tag == "form":
            self.accion = atributos.get("action")
            self.metodo = (atributos.get("method") or "get").lower()
        elif tag in ("input", "textarea", "select"):
            nombre = atributos.get("name")
            if nombre is not None:
                self.campos.append(nombre)


def tiempo_fuerza_bruta(longitud, tamano_alfabeto, intentos_por_segundo):
    """Segundos para agotar el espacio de claves a esa velocidad (peor caso)."""
    if intentos_por_segundo <= 0:
        raise ValueError("la velocidad debe ser positiva")
    combinaciones = tamano_alfabeto ** longitud
    return combinaciones / intentos_por_segundo


def entropia_bits(password):
    """Entropía aproximada: longitud * log2(tamaño del alfabeto usado)."""
    alfabeto = 0
    if any(c.islower() for c in password):
        alfabeto += 26
    if any(c.isupper() for c in password):
        alfabeto += 26
    if any(c.isdigit() for c in password):
        alfabeto += 10
    if any(not c.isalnum() for c in password):
        alfabeto += 32
    if alfabeto == 0:               # cadena vacía
        return 0.0
    return len(password) * math.log2(alfabeto)


def fuzzear(funcion, entradas):
    """Devuelve las entradas que hacen que 'funcion' lance una excepción."""
    crashean = []
    for entrada in entradas:
        try:
            funcion(entrada)
        except Exception:           # cualquier fallo cuenta como "crash"
            crashean.append(entrada)
    return crashean


def analizar_formulario(html):
    """{'accion', 'metodo', 'campos'} del primer formulario del HTML."""
    parser = _Formulario()
    parser.feed(html)
    return {"accion": parser.accion, "metodo": parser.metodo, "campos": parser.campos}


def endpoints_inseguros(endpoints):
    """Rutas (ordenadas) de endpoints de escritura que no exigen autenticación."""
    return sorted(
        e["ruta"]
        for e in endpoints
        if e["metodo"].upper() in _METODOS_ESCRITURA and not e["requiere_auth"]
    )
