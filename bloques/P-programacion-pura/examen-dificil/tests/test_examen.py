import pytest

DISCO = {
    "readme.txt": 100,
    "fotos": {"a.jpg": 2000, "b.jpg": 3000, "raw": {"c.dng": 10000}},
    "docs": {"cv.pdf": 500},
}


def test_ej1_tamano(m):
    assert m.tamano_total(DISCO) == 15600
    assert m.tamano_total({"x": 42}) == 42
    assert m.tamano_total({}) == 0
    assert m.tamano_total({"vacia": {}, "f": 7}) == 7


def test_ej2_cambio(m):
    r = m.cambio_exacto(30, [10, 20, 5])
    assert sum(r) == 30 and all(x in {10, 20, 5} for x in r)
    assert m.cambio_exacto(0, [1, 2]) == []
    assert m.cambio_exacto(3, [2]) is None
    assert m.cambio_exacto(1, []) is None
    r2 = m.cambio_exacto(63, [1, 5, 10, 25])
    assert sum(r2) == 63


def test_ej3_pares(m):
    assert m.comparaciones_todos_los_pares(1) == 0
    assert m.comparaciones_todos_los_pares(2) == 1
    assert m.comparaciones_todos_los_pares(5) == 10
    assert m.comparaciones_todos_los_pares(1000) == 499500


def test_ej4_primera(m):
    datos = [1, 3, 3, 3, 5, 8, 8]
    assert m.primera_aparicion(datos, 3) == 1
    assert m.primera_aparicion(datos, 8) == 5
    assert m.primera_aparicion(datos, 1) == 0
    assert m.primera_aparicion(datos, 4) == -1
    assert m.primera_aparicion([], 3) == -1


def test_ej5_fusionar(m):
    assert m.fusionar_ordenadas([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9]
    assert m.fusionar_ordenadas([], [1, 2]) == [1, 2]
    assert m.fusionar_ordenadas([1, 1], [1]) == [1, 1, 1]
    assert m.fusionar_ordenadas([5], []) == [5]
