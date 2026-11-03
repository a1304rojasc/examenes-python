"""Bloque 06 · Examen difícil — soluciones comentadas."""
import re

# Patrón de una línea de sshd con grupos con nombre. re.VERBOSE permite
# escribirlo en varias líneas con comentarios.
PATRON_SSHD = re.compile(
    r"""
    ^(?P<fecha>\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2})\s   # Mar 10 08:15:01
    (?P<host>\S+)\s                                    # servidor
    sshd\[(?P<pid>\d+)\]:\s                            # sshd[1234]:
    (?P<evento>Failed|Accepted)\s
    (?P<metodo>\w+)\sfor\s
    (?P<invalido>invalid\suser\s)?                     # opcional
    (?P<usuario>\S+)\sfrom\s
    (?P<ip>\S+)\sport\s(?P<puerto>\d+)
    """,
    re.VERBOSE,
)

PATRON_IP = re.compile(r"\b(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})\b")


def parsear_linea(linea):
    """Dict con fecha, host, pid, evento, metodo, usuario, invalido, ip y puerto, o None."""
    m = PATRON_SSHD.search(linea)
    if not m:
        return None
    datos = m.groupdict()
    datos["pid"] = int(datos["pid"])
    datos["puerto"] = int(datos["puerto"])
    datos["invalido"] = datos["invalido"] is not None   # grupo opcional -> bool
    return datos


def fallos_por_ip(lineas):
    """{ip: número de líneas Failed} usando parsear_linea."""
    conteo = {}
    for linea in lineas:
        datos = parsear_linea(linea)
        if datos and datos["evento"] == "Failed":
            conteo[datos["ip"]] = conteo.get(datos["ip"], 0) + 1
    return conteo


def usuarios_invalidos(lineas):
    """Lista ordenada y sin repetidos de usuarios marcados como 'invalid user'."""
    usuarios = set()
    for linea in lineas:
        datos = parsear_linea(linea)
        if datos and datos["invalido"]:
            usuarios.add(datos["usuario"])
    return sorted(usuarios)


def ips_validas(texto):
    """IPv4 con octetos 0-255, sin repetir y en orden de aparición."""
    resultado = []
    for m in PATRON_IP.finditer(texto):
        # La regex solo garantiza la forma; el rango se comprueba con int().
        if all(int(octeto) <= 255 for octeto in m.groups()):
            ip = m.group(0)
            if ip not in resultado:
                resultado.append(ip)
    return resultado


def anonimizar(linea):
    """Cambia el último octeto de cada IPv4 por "x" (203.0.113.5 -> 203.0.113.x)."""
    # \1..\3 reinsertan los tres primeros octetos capturados.
    return PATRON_IP.sub(r"\1.\2.\3.x", linea)
