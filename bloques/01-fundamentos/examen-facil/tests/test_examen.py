import pytest


def test_ej1_conversion(m):
    assert m.celsius_a_fahrenheit(0) == 32
    assert m.celsius_a_fahrenheit(100) == 212
    assert m.celsius_a_fahrenheit(-40) == -40


def test_ej1_decimales(m):
    assert m.celsius_a_fahrenheit(37.5) == pytest.approx(99.5)


def test_ej2_saludo(m, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt="": "  Ana  ")
    m.saludar()
    assert capsys.readouterr().out.strip() == "Hola, Ana!"


def test_ej3_pares(m):
    assert m.es_par(0) is True
    assert m.es_par(10) is True
    assert m.es_par(-4) is True


def test_ej3_impares(m):
    assert m.es_par(7) is False
    assert m.es_par(-3) is False


def test_ej4_precio(m):
    assert m.formatear_precio(3.5) == "3.50 €"
    assert m.formatear_precio(10) == "10.00 €"
    assert m.formatear_precio(2.999) == "3.00 €"


def test_ej5_hms(m):
    assert m.segundos_a_hms(3725) == "01:02:05"
    assert m.segundos_a_hms(0) == "00:00:00"
    assert m.segundos_a_hms(86399) == "23:59:59"
    assert m.segundos_a_hms(59) == "00:00:59"
