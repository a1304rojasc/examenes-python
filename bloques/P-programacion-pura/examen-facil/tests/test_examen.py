import numpy as np
import pytest


def test_ej1_ventas(m):
    assert m.ventas_sobre_promedio([10, 20, 30]) == 1
    assert m.ventas_sobre_promedio([5, 5, 5, 5]) == 0
    assert m.ventas_sobre_promedio([1, 2, 3, 100]) == 1
    assert m.ventas_sobre_promedio([]) == 0


def test_ej2_temperaturas(m):
    assert m.temperatura_extremos("12.5,8,20,15") == (8.0, 20.0)
    assert m.temperatura_extremos("-3,-10,4") == (-10.0, 4.0)
    assert m.temperatura_extremos("21") == (21.0, 21.0)


def test_ej3_stock(m):
    inv = [{"producto": "router", "cantidad": 7}, {"producto": "cable", "cantidad": 2}, {"producto": "switch", "cantidad": 5}]
    assert m.producto_menor_stock(inv) == "cable"
    empate = [{"producto": "a", "cantidad": 3}, {"producto": "b", "cantidad": 3}]
    assert m.producto_menor_stock(empate) == "a"


def test_ej4_promedios(m):
    assert m.promedio_por_estudiante([[10, 20], [0, 10, 20]]) == [15.0, 10.0]
    assert m.promedio_por_estudiante([[5]]) == [5.0]


def test_ej5_espejo(m):
    img = np.array([[1, 2, 3], [4, 5, 6]])
    assert np.array_equal(m.espejo_horizontal(img), np.array([[3, 2, 1], [6, 5, 4]]))
    col = np.array([[1], [2]])
    assert np.array_equal(m.espejo_horizontal(col), col)
