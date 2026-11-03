"""5.4 · Clientes HTTP — solución oficial."""

import requests

AGENTE = "monitor-utec/1.0"


def consultar_estado(base_url):
    """(código de estado, valor de 'ok') de GET /estado con el User-Agent exigido."""
    r = requests.get(f"{base_url}/estado", headers={"User-Agent": AGENTE}, timeout=5)
    if not r.ok:
        return (r.status_code, False)
    return (r.status_code, bool(r.json().get("ok", False)))


def titulos_abiertos(base_url, usuario, clave):
    """Login con sesión (la cookie viaja sola) y títulos de tickets abiertos, ordenados."""
    with requests.Session() as s:
        r = s.post(f"{base_url}/login", json={"usuario": usuario, "clave": clave}, timeout=5)
        if r.status_code != 200:
            return None
        r = s.get(f"{base_url}/tickets", timeout=5)
        r.raise_for_status()
        return sorted(t["titulo"] for t in r.json() if t["estado"] == "abierto")


def descargar_informe(base_url, ruta, usuario, clave, intentos=3):
    """Autenticación básica + reintentos solo ante 503. None si 401 o si se agotan."""
    for _ in range(intentos):
        r = requests.get(f"{base_url}{ruta}", auth=(usuario, clave), timeout=5)
        if r.status_code == 200:
            return r.text
        if r.status_code != 503:  # 401 u otro error: reintentar no lo arregla
            return None
    return None
