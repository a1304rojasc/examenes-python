"""Bloque 04 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 04 dificil
"""


from collections import Counter


def top_ips(ips, n):
    """Las n IPs más frecuentes como (ip, veces): veces desc, luego ip asc."""
    raise NotImplementedError("Implementa top_ips")


def agrupar_por_puerto(conexiones):
    """{puerto: [ips únicas ordenadas]} a partir de tuplas (ip, puerto)."""
    raise NotImplementedError("Implementa agrupar_por_puerto")


def admins_sin_mfa(usuarios):
    """Nombres ordenados de usuarios con admin=True y mfa=False."""
    raise NotImplementedError("Implementa admins_sin_mfa")


def diff_reglas(antes, despues):
    """{"añadidas": [...], "eliminadas": [...]} comparando dos listas de reglas."""
    raise NotImplementedError("Implementa diff_reglas")


def valores_sobre_umbral(matriz, umbral):
    """Aplana la matriz y deja los valores > umbral (comprensión anidada)."""
    raise NotImplementedError("Implementa valores_sobre_umbral")
