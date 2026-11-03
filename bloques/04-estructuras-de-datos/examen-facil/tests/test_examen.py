def test_ej1_duplicados(m):
    assert m.eliminar_duplicados([3, 1, 3, 2, 1]) == [3, 1, 2]
    assert m.eliminar_duplicados([]) == []
    original = ["a", "a"]
    m.eliminar_duplicados(original)
    assert original == ["a", "a"], "no modifiques la lista original"


def test_ej2_frecuencias(m):
    assert m.contar_frecuencias(["root", "admin", "root"]) == {"root": 2, "admin": 1}
    assert m.contar_frecuencias([]) == {}


def test_ej3_comunes(m):
    assert m.puertos_comunes([443, 22, 80, 22], [80, 8080, 22]) == [22, 80]
    assert m.puertos_comunes([1], [2]) == []


def test_ej4_cuadrados(m):
    assert m.cuadrados_pares(6) == [0, 4, 16, 36]
    assert m.cuadrados_pares(0) == [0]
    assert m.cuadrados_pares(5) == [0, 4, 16]


def test_ej5_invertir(m):
    assert m.invertir_diccionario({"ssh": 22, "http": 80}) == {22: "ssh", 80: "http"}
    assert m.invertir_diccionario({}) == {}
