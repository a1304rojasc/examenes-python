import hashlib

import pytest
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.asymmetric import rsa


def test_ej1_huella(m):
    assert m.huella_sha256(b"") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert m.huella_sha256(b"abc") == hashlib.sha256(b"abc").hexdigest()
    assert len(m.huella_sha256(b"x")) == 64


def test_ej2_coincide(m):
    datos = b"instalador-1.0.bin"
    h = hashlib.sha256(datos).hexdigest()
    assert m.coincide_huella(datos, h)
    assert m.coincide_huella(datos, h.upper())
    assert not m.coincide_huella(datos, "0" * 64)
    assert not m.coincide_huella(b"otro", h)


def test_ej3_fernet(m):
    clave = Fernet.generate_key()
    secreto = "clave del wifi: ejemplo ñ"
    token = m.cifrar_nota(clave, secreto)
    assert isinstance(token, bytes) and token != secreto.encode("utf-8")
    assert m.descifrar_nota(clave, token) == secreto
    with pytest.raises(InvalidToken):
        m.descifrar_nota(Fernet.generate_key(), token)


def test_ej4_rsa(m):
    privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    publica = privada.public_key()
    mensaje = b"reunion a las 10 en example.com"
    cripto = m.cifrar_para(publica, mensaje)
    assert cripto != mensaje
    assert m.descifrar_con(privada, cripto) == mensaje


def test_ej5_lsb(m):
    assert m.esconder_bit(200, 1) == 201
    assert m.esconder_bit(201, 0) == 200
    assert m.esconder_bit(255, 0) == 254
    assert m.extraer_bit(201) == 1
    assert m.extraer_bit(200) == 0
    for v in (0, 1, 128, 255):
        for b in (0, 1):
            assert m.extraer_bit(m.esconder_bit(v, b)) == b
