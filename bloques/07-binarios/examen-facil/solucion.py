"""Bloque 7 · Examen fácil — soluciones comentadas."""
import struct

# Firmas (magic bytes) de cada formato reconocido.
_FIRMAS = [
    (b"\x89PNG\r\n\x1a\n", "PNG"),
    (b"%PDF", "PDF"),
    (b"PK\x03\x04", "ZIP"),
    (b"\x7fELF", "ELF"),
]


def permiso_activo(permisos, posicion):
    """True si el bit en 'posicion' (desde 0) está encendido."""
    # Desplazamos ese bit a la posición 0 y lo aislamos con la máscara 1.
    return (permisos >> posicion) & 1 == 1


def a_hex(datos):
    """Representación hex de los bytes, dos dígitos por byte, separados por espacio."""
    return datos.hex(" ")


def leer_registro(datos):
    """Desempaqueta 4 bytes (uint32) + 2 bytes (int16), big-endian."""
    # ">" big-endian, "I" entero sin signo de 4 bytes, "h" entero con signo de 2.
    marca, temperatura = struct.unpack(">Ih", datos)
    return (marca, temperatura)


def identificar_formato(datos):
    """Devuelve el formato según la firma inicial, o 'desconocido'."""
    for firma, nombre in _FIRMAS:
        if datos.startswith(firma):
            return nombre
    return "desconocido"


def entero_desde_bytes(datos, orden):
    """Convierte bytes al entero que representan, con orden 'big' o 'little'."""
    return int.from_bytes(datos, orden)
