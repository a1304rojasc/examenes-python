"""Bloque 04 · Examen difícil — soluciones comentadas."""
from collections import Counter


def top_ips(ips, n):
    """Las n IPs más frecuentes como (ip, veces): veces desc, luego ip asc."""
    conteo = Counter(ips)
    # Clave de orden compuesta: -veces para descendente, ip para desempatar.
    ordenadas = sorted(conteo.items(), key=lambda par: (-par[1], par[0]))
    return ordenadas[:n]


def agrupar_por_puerto(conexiones):
    """{puerto: [ips únicas ordenadas]} a partir de tuplas (ip, puerto)."""
    grupos = {}
    for ip, puerto in conexiones:          # desempaquetado de la tupla
        grupos.setdefault(puerto, set()).add(ip)
    return {puerto: sorted(ips) for puerto, ips in grupos.items()}


def admins_sin_mfa(usuarios):
    """Nombres ordenados de usuarios con admin=True y mfa=False."""
    return sorted(u["nombre"] for u in usuarios if u["admin"] and not u["mfa"])


def diff_reglas(antes, despues):
    """{"añadidas": [...], "eliminadas": [...]} comparando dos listas de reglas."""
    a, d = set(antes), set(despues)
    return {
        "añadidas": sorted(d - a),     # están ahora y no antes
        "eliminadas": sorted(a - d),   # estaban antes y ya no
    }


def valores_sobre_umbral(matriz, umbral):
    """Aplana la matriz y deja los valores > umbral (comprensión anidada)."""
    # Se lee igual que dos for anidados: primero filas, luego valores.
    return [valor for fila in matriz for valor in fila if valor > umbral]
