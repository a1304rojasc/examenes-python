"""Bloque 6 · Examen difícil — soluciones comentadas.

Librería 'cryptography'. Todas las claves se generan al vuelo en los tests.
"""
import os

import numpy as np
from cryptography import x509
from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509.oid import NameOID

_PSS = lambda: padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH)


def cifrar_gcm(clave, datos, aad):
    """AES-GCM: devuelve nonce (12 bytes) + criptograma autenticado."""
    nonce = os.urandom(12)                 # único por mensaje; no secreto
    criptograma = AESGCM(clave).encrypt(nonce, datos, aad)
    return nonce + criptograma


def descifrar_gcm(clave, bloque, aad):
    """Separa el nonce y descifra; lanza InvalidTag si algo fue alterado."""
    nonce, criptograma = bloque[:12], bloque[12:]
    return AESGCM(clave).decrypt(nonce, criptograma, aad)


def firmar(privada, mensaje):
    """Firma RSA-PSS sobre SHA-256 del mensaje."""
    return privada.sign(mensaje, _PSS(), hashes.SHA256())


def verificar(publica, mensaje, firma):
    """True si la firma corresponde al mensaje y a la clave pública."""
    try:
        publica.verify(firma, mensaje, _PSS(), hashes.SHA256())
        return True
    except InvalidSignature:
        return False


def derivar_secreto_compartido(mi_privada, su_publica):
    """Secreto compartido ECDH (curva de Montgomery X25519)."""
    # exchange() combina mi privada con la pública del otro: ambos llegan al mismo valor.
    return mi_privada.exchange(su_publica)


def datos_certificado(pem):
    """Extrae sujeto, emisor, número de serie y validez de un certificado PEM."""
    cert = x509.load_pem_x509_certificate(pem)

    def nombre_comun(nombre):
        atributos = nombre.get_attributes_for_oid(NameOID.COMMON_NAME)
        return atributos[0].value if atributos else None

    return {
        "sujeto_cn": nombre_comun(cert.subject),
        "emisor_cn": nombre_comun(cert.issuer),
        "numero_serie": cert.serial_number,
        "no_antes": cert.not_valid_before_utc,
        "no_despues": cert.not_valid_after_utc,
    }


def _bits(datos):
    """Genera los bits (de más a menos significativo) de una secuencia de bytes."""
    for byte in datos:
        for i in range(7, -1, -1):
            yield (byte >> i) & 1


def ocultar_texto(imagen, texto):
    """Oculta 'texto' en los bits menos significativos de la imagen (copia)."""
    datos = texto.encode("utf-8")
    # Cabecera de 4 bytes con la longitud, para saber cuánto leer al revelar.
    carga = len(datos).to_bytes(4, "big") + datos
    bits = list(_bits(carga))
    plano = imagen.flatten()
    if len(bits) > len(plano):
        raise ValueError("la imagen no tiene capacidad suficiente")
    salida = plano.copy()
    for i, bit in enumerate(bits):
        salida[i] = (int(salida[i]) & ~1) | bit
    return salida.reshape(imagen.shape).astype(imagen.dtype)


def revelar_texto(imagen):
    """Recupera el texto oculto con ocultar_texto."""
    plano = imagen.flatten()
    cabecera = [int(plano[i]) & 1 for i in range(32)]
    longitud = 0
    for bit in cabecera:
        longitud = (longitud << 1) | bit
    bits = [int(plano[32 + i]) & 1 for i in range(longitud * 8)]
    datos = bytearray()
    for i in range(0, len(bits), 8):
        byte = 0
        for j in range(8):
            byte = (byte << 1) | bits[i + j]
        datos.append(byte)
    return datos.decode("utf-8")
