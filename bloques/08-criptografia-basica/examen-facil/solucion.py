"""Bloque 08 · Examen fácil — soluciones comentadas."""
import base64
import hashlib


def codificar_b64(texto):
    """Texto UTF-8 -> cadena Base64."""
    # base64 trabaja con bytes: str -> bytes -> base64 (bytes) -> str
    return base64.b64encode(texto.encode("utf-8")).decode("ascii")


def decodificar_b64(b64):
    """Cadena Base64 -> texto UTF-8."""
    return base64.b64decode(b64).decode("utf-8")


def sha256_hex(texto):
    """SHA-256 en hexadecimal del texto codificado en UTF-8."""
    return hashlib.sha256(texto.encode("utf-8")).hexdigest()


def cesar(texto, desplazamiento):
    """Cifrado César sobre A-Z y a-z; el resto de caracteres no cambia."""
    resultado = []
    for c in texto:
        if "a" <= c <= "z" or "A" <= c <= "Z":
            base = ord("a") if c.islower() else ord("A")
            # % 26 hace que funcione con desplazamientos negativos o > 26.
            resultado.append(chr((ord(c) - base + desplazamiento) % 26 + base))
        else:
            resultado.append(c)   # espacios, dígitos, ñ, tildes... se quedan igual
    return "".join(resultado)


def descifrar_cesar(texto, desplazamiento):
    """Deshace cesar(): desplazar en sentido contrario."""
    return cesar(texto, -desplazamiento)


def verificar_integridad(ruta, hash_esperado):
    """True si el SHA-256 del archivo coincide con hash_esperado."""
    h = hashlib.sha256()
    with open(ruta, "rb") as f:              # "rb": bytes, sin tocar saltos de línea
        while bloque := f.read(65536):       # por bloques: sirve para archivos enormes
            h.update(bloque)
    return h.hexdigest() == hash_esperado.strip().lower()
