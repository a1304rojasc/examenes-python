"""Bloque 06 · Examen fácil — soluciones comentadas."""
import re

# Cuatro bloques de 1-3 dígitos separados por puntos literales.
# \b = límite de palabra, evita cortar números más largos.
PATRON_IP = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

# "for" + opcionalmente "invalid user " + el usuario (sin espacios) + " from".
PATRON_USUARIO = re.compile(r"(?:Failed|Accepted) \w+ for (?:invalid user )?(\S+) from")

PATRON_EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}")


def normalizar_espacios(texto):
    """Quita espacios en los extremos y deja uno solo entre palabras."""
    return " ".join(texto.split())  # split() sin argumentos agrupa espacios/tabs


def extraer_ips(texto):
    """Lista de cadenas con forma IPv4 (n.n.n.n) en orden de aparición."""
    return PATRON_IP.findall(texto)


def es_linea_fallida(linea):
    """True si la línea contiene "Failed password"."""
    return "Failed password" in linea  # no hace falta regex para algo tan simple


def extraer_usuario(linea):
    """Usuario de una línea Failed/Accepted de sshd, o None."""
    coincidencia = PATRON_USUARIO.search(linea)
    if coincidencia:
        return coincidencia.group(1)  # grupo 1 = lo que hay en (\S+)
    return None


def es_email_valido(texto):
    """True si todo el texto tiene forma usuario@dominio.tld."""
    return PATRON_EMAIL.fullmatch(texto) is not None
