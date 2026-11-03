"""Bloque 6 · Examen fácil — soluciones comentadas.

Usa la librería 'cryptography'. Las claves se generan al vuelo en los tests;
nunca se incrustan claves privadas reales.
"""
import hashlib
import hmac

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def huella_sha256(datos):
    """Huella SHA-256 (hexadecimal) del contenido en bytes."""
    return hashlib.sha256(datos).hexdigest()


def coincide_huella(datos, huella_hex):
    """True si la huella SHA-256 de 'datos' coincide con huella_hex."""
    calculada = hashlib.sha256(datos).hexdigest()
    # compare_digest evita filtrar información por el tiempo de comparación.
    return hmac.compare_digest(calculada, huella_hex.strip().lower())


def cifrar_nota(clave, texto):
    """Cifra 'texto' con Fernet (cifrado autenticado) y devuelve el token en bytes."""
    f = Fernet(clave)
    return f.encrypt(texto.encode("utf-8"))


def descifrar_nota(clave, token):
    """Recupera el texto original de un token de Fernet."""
    f = Fernet(clave)
    return f.decrypt(token).decode("utf-8")


def cifrar_para(publica, mensaje):
    """Cifra 'mensaje' (bytes) con la clave pública RSA del destinatario (OAEP)."""
    return publica.encrypt(
        mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def descifrar_con(privada, criptograma):
    """Descifra con la clave privada RSA y devuelve el mensaje en bytes."""
    return privada.decrypt(
        criptograma,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )


def esconder_bit(valor, bit):
    """Devuelve el valor (0-255) con su bit menos significativo puesto a 'bit'."""
    # Borramos el último bit (& ~1) y colocamos el deseado (| bit).
    return (valor & ~1) | bit


def extraer_bit(valor):
    """Devuelve el bit menos significativo del valor."""
    return valor & 1
