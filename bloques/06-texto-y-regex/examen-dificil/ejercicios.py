"""Bloque 06 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 06 dificil
"""


import re

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
    raise NotImplementedError("Implementa parsear_linea")


def fallos_por_ip(lineas):
    """{ip: número de líneas Failed} usando parsear_linea."""
    raise NotImplementedError("Implementa fallos_por_ip")


def usuarios_invalidos(lineas):
    """Lista ordenada y sin repetidos de usuarios marcados como 'invalid user'."""
    raise NotImplementedError("Implementa usuarios_invalidos")


def ips_validas(texto):
    """IPv4 con octetos 0-255, sin repetir y en orden de aparición."""
    raise NotImplementedError("Implementa ips_validas")


def anonimizar(linea):
    """Cambia el último octeto de cada IPv4 por "x" (203.0.113.5 -> 203.0.113.x)."""
    raise NotImplementedError("Implementa anonimizar")
