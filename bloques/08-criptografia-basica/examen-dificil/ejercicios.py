"""Bloque 08 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 08 dificil
"""


import hashlib
import hmac
import secrets

FRECUENCIAS_ES = {
    "a": 12.5, "b": 1.4, "c": 4.7, "d": 5.9, "e": 13.7, "f": 0.7, "g": 1.0, "h": 0.7,
    "i": 6.3, "j": 0.4, "k": 0.1, "l": 5.0, "m": 3.2, "n": 6.7, "o": 8.7, "p": 2.5,
    "q": 0.9, "r": 6.9, "s": 8.0, "t": 4.6, "u": 3.9, "v": 0.9, "w": 0.1, "x": 0.2,
    "y": 0.9, "z": 0.5,
}


def _desplazar(c, d):
    """Desplaza una letra ASCII d posiciones (auxiliar)."""
    raise NotImplementedError("Implementa _desplazar")


def vigenere(texto, clave, descifrar=False):
    """Cifra (o descifra) Vigenère; la clave solo avanza con letras A-Z/a-z."""
    raise NotImplementedError("Implementa vigenere")


def romper_cesar(cifrado):
    """(desplazamiento, texto_claro) con menor chi-cuadrado frente al español."""
    raise NotImplementedError("Implementa romper_cesar")


def hash_password(password, sal=None, iteraciones=100_000):
    """Devuelve "pbkdf2_sha256$iter$sal_hex$hash_hex" usando PBKDF2-HMAC-SHA256."""
    raise NotImplementedError("Implementa hash_password")


def verificar_password(password, almacenado):
    """True si password corresponde al hash almacenado (tiempo constante)."""
    raise NotImplementedError("Implementa verificar_password")


def firmar(mensaje, clave):
    """HMAC-SHA256 en hexadecimal del mensaje con la clave."""
    raise NotImplementedError("Implementa firmar")


def verificar_firma(mensaje, clave, firma):
    """True si la firma es válida (comparación en tiempo constante)."""
    raise NotImplementedError("Implementa verificar_firma")


def auditar_debiles(hashes, diccionario):
    """{usuario: contraseña débil} para usuarios cuyo sha256 está en el diccionario."""
    raise NotImplementedError("Implementa auditar_debiles")
