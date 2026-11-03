import pytest


def test_ej1_area(m):
    assert m.area_rectangulo(3, 4) == 12
    assert m.area_rectangulo(5) == 5
    assert m.area_rectangulo(altura=2, base=6) == 12


def test_ej2_estadisticas(m):
    minimo, maximo, media = m.estadisticas([4, 1, 7])
    assert (minimo, maximo) == (1, 7)
    assert media == pytest.approx(4.0)
    assert m.estadisticas([5]) == (5, 5, 5)


def test_ej3_aplicar(m):
    assert m.aplicar(lambda x: x * 2, 3, 2) == 12
    assert m.aplicar(lambda x: x + 1, 0) == 1
    assert m.aplicar(str.upper, "ssh") == "SSH"
    assert m.aplicar(lambda x: x * 2, 5, 0) == 5


def test_ej4_contador(m):
    m.reiniciar_eventos()
    assert m.registrar_evento() == 1
    assert m.registrar_evento() == 2
    assert m.EVENTOS == 2
    m.reiniciar_eventos()
    assert m.EVENTOS == 0
    assert m.registrar_evento() == 1


def test_ej5_hipotenusa(m):
    assert m.hipotenusa(3, 4) == pytest.approx(5)
    assert m.hipotenusa(1, 1) == pytest.approx(2 ** 0.5)
