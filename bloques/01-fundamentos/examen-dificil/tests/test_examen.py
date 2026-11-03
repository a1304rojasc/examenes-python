import pytest


def test_ej1_enteros(m):
    assert m.leer_entero(" 42\n") == 42
    assert m.leer_entero("-7") == -7


def test_ej1_decimales(m):
    assert m.leer_entero("3.9") == 3
    assert isinstance(m.leer_entero("3.9"), int)


def test_ej2_cuenta(m):
    assert m.dividir_cuenta(100, 4, 10) == 27.5
    assert m.dividir_cuenta(50, 3, 0) == pytest.approx(16.67)
    assert m.dividir_cuenta(80, 2, 15) == 46.0


def test_ej3_fila(m):
    assert m.fila_puerto("ssh", 22) == "ssh     |   22"
    assert m.fila_puerto("https", 443) == "https   |  443"
    assert len(m.fila_puerto("dns", 53)) == 14


def test_ej4_hosts(m):
    assert m.hosts_por_prefijo(24) == 254
    assert m.hosts_por_prefijo(30) == 2
    assert m.hosts_por_prefijo(16) == 65534


def test_ej5_mascara(m):
    assert m.enmascarar("password") == "p******d"
    assert m.enmascarar("abc") == "a*c"
    assert len(m.enmascarar("s3cr3t0!")) == 8
