def test_ej1_puertos(m):
    assert m.validar_puerto("22") == "reservado"
    assert m.validar_puerto(" 8080 ") == "válido"
    assert m.validar_puerto("1024") == "válido"
    assert m.validar_puerto("65535") == "válido"


def test_ej1_invalidos(m):
    for malo in ["0", "65536", "-1", "abc", "", "80a", "3.5"]:
        assert m.validar_puerto(malo) == "inválido", malo


def test_ej2_login(m):
    assert m.intento_exitoso(["a", "b", "secreto"], "secreto") == 3
    assert m.intento_exitoso(["secreto"], "secreto") == 1
    assert m.intento_exitoso(["a", "b", "c", "secreto"], "secreto") == 0
    assert m.intento_exitoso(["a", "b", "c", "secreto"], "secreto", max_intentos=5) == 4
    assert m.intento_exitoso([], "x") == 0
    assert m.intento_exitoso(["a"], "x") == 0


def test_ej3_primos(m):
    primos = [n for n in range(50) if m.es_primo(n)]
    assert primos == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert m.es_primo(7919) is True
    assert m.es_primo(7917) is False


def test_ej4_fortaleza(m):
    assert m.fortaleza("") == 0
    assert m.fortaleza("abcdefgh") == 1
    assert m.fortaleza("Abcdefg1") == 3
    assert m.fortaleza("Abcdef1!") == 4
    assert m.fortaleza("a!") == 1


def test_ej5_tabla(m):
    assert m.tabla_multiplicar(7, 3) == "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21"
    assert m.tabla_multiplicar(2, 1) == "2 x 1 = 2"
    assert m.tabla_multiplicar(9, 10).count("\n") == 9
