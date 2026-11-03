"""Bloque 06 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 06 dificil
"""


import os
import numpy as np
from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509.oid import NameOID


def cifrar_gcm(clave, datos, aad):
    """AES-GCM: devuelve nonce (12 bytes) + criptograma autenticado."""
    raise NotImplementedError("Implementa cifrar_gcm")


def descifrar_gcm(clave, bloque, aad):
    """Separa el nonce y descifra; lanza InvalidTag si algo fue alterado."""
    raise NotImplementedError("Implementa descifrar_gcm")


def firmar(privada, mensaje):
    """Firma RSA-PSS sobre SHA-256 del mensaje."""
    raise NotImplementedError("Implementa firmar")


def verificar(publica, mensaje, firma):
    """True si la firma corresponde al mensaje y a la clave pública."""
    raise NotImplementedError("Implementa verificar")


def derivar_secreto_compartido(mi_privada, su_publica):
    """Secreto compartido ECDH (curva de Montgomery X25519)."""
    raise NotImplementedError("Implementa derivar_secreto_compartido")


def datos_certificado(pem):
    """Extrae sujeto, emisor, número de serie y validez de un certificado PEM."""
    raise NotImplementedError("Implementa datos_certificado")


def ocultar_texto(imagen, texto):
    """Oculta 'texto' en los bits menos significativos de la imagen (copia)."""
    raise NotImplementedError("Implementa ocultar_texto")


def revelar_texto(imagen):
    """Recupera el texto oculto con ocultar_texto."""
    raise NotImplementedError("Implementa revelar_texto")
