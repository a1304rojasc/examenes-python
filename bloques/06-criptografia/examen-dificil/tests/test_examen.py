import datetime

import numpy as np
import pytest
from cryptography import x509
from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa, x25519
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.x509.oid import NameOID


def test_ej1_gcm(m):
    clave = AESGCM.generate_key(bit_length=256)
    datos, aad = b"expediente confidencial", b"expediente-42"
    bloque = m.cifrar_gcm(clave, datos, aad)
    assert len(bloque) > len(datos)
    assert m.descifrar_gcm(clave, bloque, aad) == datos
    with pytest.raises(InvalidTag):
        m.descifrar_gcm(clave, bloque, b"expediente-99")   # aad alterado
    alterado = bytearray(bloque)
    alterado[-1] ^= 1
    with pytest.raises(InvalidTag):
        m.descifrar_gcm(clave, bytes(alterado), aad)        # criptograma alterado


def test_ej2_firma(m):
    privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    publica = privada.public_key()
    mensaje = b"corte de servicio el 2026-01-15"
    firma = m.firmar(privada, mensaje)
    assert m.verificar(publica, mensaje, firma) is True
    assert m.verificar(publica, b"corte de servicio el 2026-02-15", firma) is False
    otra = rsa.generate_private_key(public_exponent=65537, key_size=2048).public_key()
    assert m.verificar(otra, mensaje, firma) is False


def test_ej3_ecdh(m):
    a = x25519.X25519PrivateKey.generate()
    b = x25519.X25519PrivateKey.generate()
    secreto_a = m.derivar_secreto_compartido(a, b.public_key())
    secreto_b = m.derivar_secreto_compartido(b, a.public_key())
    assert isinstance(secreto_a, bytes) and len(secreto_a) == 32
    assert secreto_a == secreto_b
    c = x25519.X25519PrivateKey.generate()
    assert m.derivar_secreto_compartido(a, c.public_key()) != secreto_a


def _cert_pem(cn="example.com", emisor="Ejemplo CA", serie=4242):
    clave = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    sujeto = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, cn)])
    emisor_n = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, emisor)])
    inicio = datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
    cert = (x509.CertificateBuilder()
            .subject_name(sujeto).issuer_name(emisor_n)
            .public_key(clave.public_key()).serial_number(serie)
            .not_valid_before(inicio)
            .not_valid_after(inicio + datetime.timedelta(days=90))
            .sign(clave, hashes.SHA256()))
    return cert.public_bytes(serialization.Encoding.PEM)


def test_ej4_certificado(m):
    info = m.datos_certificado(_cert_pem())
    assert info["sujeto_cn"] == "example.com"
    assert info["emisor_cn"] == "Ejemplo CA"
    assert info["numero_serie"] == 4242
    assert info["no_antes"] == datetime.datetime(2026, 1, 1, tzinfo=datetime.timezone.utc)
    assert info["no_despues"] == datetime.datetime(2026, 4, 1, tzinfo=datetime.timezone.utc)


def test_ej5_stego(m):
    rng = np.random.default_rng(0)
    imagen = rng.integers(0, 256, size=(40, 40), dtype=np.uint8)
    secreto = "Aviso: revisar la cámara 3 ✓"
    con_mensaje = m.ocultar_texto(imagen, secreto)
    assert con_mensaje.shape == imagen.shape and con_mensaje.dtype == imagen.dtype
    assert m.revelar_texto(con_mensaje) == secreto
    # Cada píxel cambia como mucho en 1 (solo el bit menos significativo).
    assert int(np.max(np.abs(con_mensaje.astype(int) - imagen.astype(int)))) <= 1
    with pytest.raises(ValueError):
        m.ocultar_texto(np.zeros((2, 2), dtype=np.uint8), "mensaje demasiado largo")
