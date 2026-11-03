def test_ej1_privilegios(m):
    assert m.necesita_privilegios(22) is True
    assert m.necesita_privilegios(1023) is True
    assert m.necesita_privilegios(1024) is False
    assert m.necesita_privilegios(8080) is False


def test_ej2_xor(m):
    assert m.xor_repetida(b"\x00\x01\x02", b"\xff") == bytes([0xff, 0xfe, 0xfd])
    cifrado = m.xor_repetida(b"mensaje secreto", b"CTF")
    assert cifrado != b"mensaje secreto"
    assert m.xor_repetida(cifrado, b"CTF") == b"mensaje secreto"
    assert m.xor_repetida(b"", b"k") == b""


def test_ej3_flag(m):
    assert m.buscar_flag("ruido FLAG{xor_es_facil} mas ruido") == "FLAG{xor_es_facil}"
    assert m.buscar_flag("primera FLAG{a} y FLAG{b}") == "FLAG{a}"
    assert m.buscar_flag("aqui no hay bandera") is None


def test_ej4_severidad(m):
    eventos = [{"severidad": "alta"}, {"severidad": "baja"}, {"severidad": "alta"}, {"severidad": "media"}]
    assert m.contar_por_severidad(eventos) == {"alta": 2, "baja": 1, "media": 1}
    assert m.contar_por_severidad([]) == {}


def test_ej5_opciones(m):
    lineas = ["use exploit/demo", "set RHOSTS 192.0.2.10", "set RPORT 8080", "set RHOSTS 198.51.100.7", "run"]
    assert m.opciones_modulo(lineas) == {"RHOSTS": "198.51.100.7", "RPORT": "8080"}
    assert m.opciones_modulo(["set PAYLOAD windows/meterpreter/reverse_tcp"]) == {"PAYLOAD": "windows/meterpreter/reverse_tcp"}
    assert m.opciones_modulo(["# comentario", "run"]) == {}
