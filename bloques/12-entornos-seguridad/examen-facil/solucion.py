"""Bloque 12 · Examen fácil — soluciones comentadas (local, datos de ejemplo)."""
import re

PATRON_FLAG = re.compile(r"FLAG\{[^}]*\}")


def necesita_privilegios(puerto):
    """True si el puerto es privilegiado (< 1024)."""
    return puerto < 1024


def xor_repetida(datos, clave):
    """XOR byte a byte de 'datos' con 'clave' repetida. Cifra y descifra igual."""
    # i % len(clave) recorre la clave en círculo.
    return bytes(b ^ clave[i % len(clave)] for i, b in enumerate(datos))


def buscar_flag(texto):
    """Primera cadena con formato FLAG{...}, o None."""
    coincidencia = PATRON_FLAG.search(texto)
    return coincidencia.group() if coincidencia else None


def contar_por_severidad(eventos):
    """{severidad: número de eventos} a partir de una lista de registros."""
    conteo = {}
    for evento in eventos:
        sev = evento["severidad"]
        conteo[sev] = conteo.get(sev, 0) + 1
    return conteo


def opciones_modulo(lineas):
    """{OPCION: valor} de las líneas 'set OPCION valor' (la última gana)."""
    opciones = {}
    for linea in lineas:
        partes = linea.split()
        if len(partes) >= 3 and partes[0] == "set":
            # partes[1] es la opción; el resto (unido) es el valor.
            opciones[partes[1]] = " ".join(partes[2:])
    return opciones
