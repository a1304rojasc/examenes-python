"""Bloque 12 · Examen difícil — soluciones comentadas (local, datos de ejemplo)."""
import re

_SERVICIO = re.compile(r"^(\d+)/tcp\s+(\w+)\s+(\S+)")


def romper_xor_un_byte(cifrado, pista):
    """Prueba las 256 claves de un byte; devuelve (clave, texto) que contiene 'pista'."""
    for clave in range(256):
        texto = bytes(b ^ clave for b in cifrado).decode("latin-1")
        if pista in texto:
            return (clave, texto)
    return None


def _max_en_ventana(tiempos, ventana):
    """Máximo de eventos dentro de cualquier intervalo de 'ventana' segundos."""
    t = sorted(tiempos)
    mejor, inicio = 0, 0
    for fin in range(len(t)):
        while t[fin] - t[inicio] > ventana:
            inicio += 1
        mejor = max(mejor, fin - inicio + 1)
    return mejor


def alertas_fuerza_bruta(eventos, umbral, ventana):
    """IPs (ordenadas) con >= umbral eventos 'login_fallido' en alguna ventana."""
    por_ip = {}
    for evento in eventos:
        if evento["tipo"] == "login_fallido":
            por_ip.setdefault(evento["ip"], []).append(evento["ts"])
    return sorted(ip for ip, tiempos in por_ip.items() if _max_en_ventana(tiempos, ventana) >= umbral)


def agrupar_alertas(alertas):
    """Agrupa por (tipo, origen) con conteo y rango temporal, ordenado."""
    grupos = {}
    for alerta in alertas:
        clave = (alerta["tipo"], alerta["origen"])
        ts = alerta["ts"]
        if clave not in grupos:
            grupos[clave] = {"conteo": 0, "primero": ts, "ultimo": ts}
        g = grupos[clave]
        g["conteo"] += 1
        g["primero"] = min(g["primero"], ts)
        g["ultimo"] = max(g["ultimo"], ts)
    return [
        {"tipo": tipo, "origen": origen, "conteo": g["conteo"], "primero": g["primero"], "ultimo": g["ultimo"]}
        for (tipo, origen), g in sorted(grupos.items())
    ]


def parsear_servicios(texto):
    """Lista de {puerto, servicio} para cada línea 'PUERTO/tcp open SERVICIO'."""
    servicios = []
    for linea in texto.splitlines():
        m = _SERVICIO.match(linea.strip())
        if m and m.group(2) == "open":
            servicios.append({"puerto": int(m.group(1)), "servicio": m.group(3)})
    return servicios


def _de_bruijn(k, n):
    """Secuencia de De Bruijn B(k, n) como lista de índices (cada ventana de n es única)."""
    a = [0] * (k * n)
    secuencia = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                secuencia.extend(a[1:p + 1])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return secuencia


def generar_ciclico(longitud, n=4):
    """Cadena de 'longitud' donde cada subcadena de n (4) caracteres es única."""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    secuencia = _de_bruijn(len(alfabeto), n)
    cadena = "".join(alfabeto[i] for i in secuencia)
    return cadena[:longitud]


def posicion_ciclico(patron, fragmento):
    """Índice donde aparece 'fragmento' en el patrón, o -1."""
    return patron.find(fragmento)
