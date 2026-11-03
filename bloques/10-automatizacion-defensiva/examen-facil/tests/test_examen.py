from datetime import datetime

import pytest


def test_ej1_fecha(m):
    assert m.parsear_marca_tiempo("Mar 10 08:15:01") == datetime(2026, 3, 10, 8, 15, 1)
    assert m.parsear_marca_tiempo("Mar  9 23:59:59", anio=2025) == datetime(2025, 3, 9, 23, 59, 59)
    with pytest.raises(ValueError):
        m.parsear_marca_tiempo("no es fecha")


def test_ej2_ventana(m):
    a = datetime(2026, 3, 10, 8, 0, 0)
    b = datetime(2026, 3, 10, 8, 1, 0)
    assert m.dentro_de_ventana(a, b, 60)
    assert m.dentro_de_ventana(b, a, 60)
    assert not m.dentro_de_ventana(a, b, 59)


def test_ej3_max(m):
    assert m.max_en_ventana([0, 10, 20, 100, 105], 30) == 3
    assert m.max_en_ventana([105, 0, 100, 20, 10], 30) == 3
    assert m.max_en_ventana([0, 60], 60) == 2
    assert m.max_en_ventana([0, 61], 60) == 1
    assert m.max_en_ventana([], 60) == 0


def test_ej4_parser(m):
    p = m.crear_parser()
    a = p.parse_args(["auth.log"])
    assert (a.archivo, a.umbral, a.ventana, a.json) == ("auth.log", 5, 60, False)
    a = p.parse_args(["x.log", "--umbral", "3", "--ventana", "30", "--json"])
    assert (a.umbral, a.ventana, a.json) == (3, 30, True)
    with pytest.raises(SystemExit):
        p.parse_args([])


def test_ej5_fuerza_bruta(m):
    assert m.es_fuerza_bruta([0, 5, 10, 15, 20], 5, 60)
    assert not m.es_fuerza_bruta([0, 100, 200, 300, 400], 5, 60)
    assert m.es_fuerza_bruta([0, 1, 2], 3, 2)
    assert not m.es_fuerza_bruta([0, 1, 2], 4, 100)
