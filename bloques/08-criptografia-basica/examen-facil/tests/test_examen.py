import hashlib


def test_ej1_b64(m):
    assert m.codificar_b64("hola") == "aG9sYQ=="
    assert m.decodificar_b64("aG9sYQ==") == "hola"
    assert m.decodificar_b64(m.codificar_b64("contraseña ñ")) == "contraseña ñ"


def test_ej2_sha256(m):
    assert m.sha256_hex("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    assert m.sha256_hex("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert len(m.sha256_hex("x")) == 64


def test_ej3_cesar(m):
    assert m.cesar("ABC", 3) == "DEF"
    assert m.cesar("xyz", 3) == "abc"
    assert m.cesar("Hola, Mundo 2024!", 1) == "Ipmb, Nvoep 2024!"
    assert m.cesar("abc", 29) == "def"
    assert m.cesar("abc", -1) == "zab"


def test_ej4_descifrar(m):
    assert m.descifrar_cesar("DEF", 3) == "ABC"
    for d in range(-30, 30, 7):
        assert m.descifrar_cesar(m.cesar("Ataque al Amanecer", d), d) == "Ataque al Amanecer"


def test_ej5_integridad(m, tmp_path):
    f = tmp_path / "descarga.iso"
    contenido = b"\x00\x01" * 100_000
    f.write_bytes(contenido)
    bueno = hashlib.sha256(contenido).hexdigest()
    assert m.verificar_integridad(f, bueno)
    assert m.verificar_integridad(f, bueno.upper())
    assert not m.verificar_integridad(f, "0" * 64)
