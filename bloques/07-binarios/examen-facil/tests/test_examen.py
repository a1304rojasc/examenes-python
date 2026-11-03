import struct


def test_ej1_permisos(m):
    assert m.permiso_activo(0b101, 0) is True
    assert m.permiso_activo(0b101, 1) is False
    assert m.permiso_activo(0b101, 2) is True
    assert m.permiso_activo(0, 7) is False
    assert m.permiso_activo(0b10000000, 7) is True


def test_ej2_hex(m):
    assert m.a_hex(b"\xde\xad\xbe\xef") == "de ad be ef"
    assert m.a_hex(b"") == ""
    assert m.a_hex(b"\x00\x0f") == "00 0f"


def test_ej3_registro(m):
    datos = struct.pack(">Ih", 1_700_000_000, -45)
    assert m.leer_registro(datos) == (1_700_000_000, -45)
    assert m.leer_registro(struct.pack(">Ih", 0, 100)) == (0, 100)


def test_ej4_formato(m):
    assert m.identificar_formato(b"\x89PNG\r\n\x1a\n....") == "PNG"
    assert m.identificar_formato(b"%PDF-1.7") == "PDF"
    assert m.identificar_formato(b"PK\x03\x04blah") == "ZIP"
    assert m.identificar_formato(b"\x7fELF\x02\x01") == "ELF"
    assert m.identificar_formato(b"hola mundo") == "desconocido"
    assert m.identificar_formato(b"") == "desconocido"


def test_ej5_entero(m):
    assert m.entero_desde_bytes(b"\x01\x00", "big") == 256
    assert m.entero_desde_bytes(b"\x01\x00", "little") == 1
    assert m.entero_desde_bytes(b"\xff\xff\xff\xff", "big") == 4294967295
    assert m.entero_desde_bytes(b"\x00", "big") == 0
