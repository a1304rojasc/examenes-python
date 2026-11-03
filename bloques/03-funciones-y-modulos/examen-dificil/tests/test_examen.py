def test_ej1_closure(m):
    es_puerto = m.crear_validador(1, 65535)
    es_nota = m.crear_validador(0, 10)
    assert es_puerto(22) and es_puerto(1) and es_puerto(65535)
    assert not es_puerto(0) and not es_puerto(70000)
    assert es_nota(10) and not es_nota(11)


def test_ej2_url(m):
    assert m.construir_url("example.com") == "https://example.com/"
    assert m.construir_url("example.com", "/buscar", q="ssh", p=2) == "https://example.com/buscar?q=ssh&p=2"
    assert m.construir_url("example.com", ruta="/api") == "https://example.com/api"


def test_ej3_reintentar(m):
    respuestas = iter([False, False, True])
    assert m.reintentar(lambda: next(respuestas), 5) == 3
    assert m.reintentar(lambda: False, 4) == -1
    assert m.reintentar(lambda: True, 1) == 1
    llamadas = []
    m.reintentar(lambda: llamadas.append(1), 3)
    assert len(llamadas) == 3


def test_ej4_potencia(m):
    assert m.potencia_mod(3, 4, 5) == pow(3, 4, 5)
    assert m.potencia_mod(2, 0, 7) == 1
    assert m.potencia_mod(7, 123456, 1000003) == pow(7, 123456, 1000003)
    assert m.potencia_mod(5, 1, 3) == 2


def test_ej5_pin(m):
    pin = m.generar_pin(6, 42)
    assert len(pin) == 6 and pin.isdigit()
    assert m.generar_pin(6, 42) == pin
    assert len({m.generar_pin(8, s) for s in range(10)}) > 1
    assert m.generar_pin(0, 1) == ""
