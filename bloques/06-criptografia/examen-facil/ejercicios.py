"""Bloque 06 · Examen fácil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 06 facil
"""


import hashlib
import hmac
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def huella_sha256(datos):
    """Huella SHA-256 (hexadecimal) del contenido en bytes."""
    raise NotImplementedError("Implementa huella_sha256")


def coincide_huella(datos, huella_hex):
    """True si la huella SHA-256 de 'datos' coincide con huella_hex."""
    raise NotImplementedError("Implementa coincide_huella")


def cifrar_nota(clave, texto):
    """Cifra 'texto' con Fernet (cifrado autenticado) y devuelve el token en bytes."""
    raise NotImplementedError("Implementa cifrar_nota")


def descifrar_nota(clave, token):
    """Recupera el texto original de un token de Fernet."""
    raise NotImplementedError("Implementa descifrar_nota")


def cifrar_para(publica, mensaje):
    """Cifra 'mensaje' (bytes) con la clave pública RSA del destinatario (OAEP)."""
    raise NotImplementedError("Implementa cifrar_para")


def descifrar_con(privada, criptograma):
    """Descifra con la clave privada RSA y devuelve el mensaje en bytes."""
    raise NotImplementedError("Implementa descifrar_con")


def esconder_bit(valor, bit):
    """Devuelve el valor (0-255) con su bit menos significativo puesto a 'bit'."""
    raise NotImplementedError("Implementa esconder_bit")


def extraer_bit(valor):
    """Devuelve el bit menos significativo del valor."""
    raise NotImplementedError("Implementa extraer_bit")
