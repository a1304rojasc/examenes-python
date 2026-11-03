def test_ej1_tramos(m):
    assert m.clasificar_nota(4.9) == "suspenso"
    assert m.clasificar_nota(5) == "aprobado"
    assert m.clasificar_nota(7) == "notable"
    assert m.clasificar_nota(8.99) == "notable"
    assert m.clasificar_nota(9) == "sobresaliente"
    assert m.clasificar_nota(10) == "sobresaliente"


def test_ej2_suma(m):
    assert m.suma_hasta(1) == 1
    assert m.suma_hasta(10) == 55
    assert m.suma_hasta(0) == 0
    assert m.suma_hasta(-5) == 0


def test_ej3_vocales(m):
    assert m.contar_vocales("murcielago") == 5
    assert m.contar_vocales("AEIOU xyz") == 5
    assert m.contar_vocales("") == 0
    assert m.contar_vocales("rtx 4090") == 0


def test_ej4_negativo(m):
    assert m.primer_negativo([3, 1, -2, -5]) == 2
    assert m.primer_negativo([-1]) == 0
    assert m.primer_negativo([1, 2, 3]) == -1
    assert m.primer_negativo([]) == -1


def test_ej5_continue(m):
    assert m.suma_sin_multiplos_de_3(10) == 37
    assert m.suma_sin_multiplos_de_3(2) == 3
    assert m.suma_sin_multiplos_de_3(3) == 3
