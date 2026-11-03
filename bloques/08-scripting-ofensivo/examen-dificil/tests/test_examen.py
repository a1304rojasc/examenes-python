import math

import pytest

FORM = (
    '<form action="/login" method="POST">'
    '<input type="text" name="usuario">'
    '<input type="password" name="clave">'
    '<input type="hidden" name="csrf_token" value="abc">'
    '<button>Entrar</button>'
    '</form>'
)


def test_ej1_tiempo(m):
    assert m.tiempo_fuerza_bruta(4, 10, 1000) == 10.0
    assert m.tiempo_fuerza_bruta(8, 62, 1_000_000_000) == pytest.approx(62 ** 8 / 1e9)
    with pytest.raises(ValueError):
        m.tiempo_fuerza_bruta(8, 62, 0)
    with pytest.raises(ValueError):
        m.tiempo_fuerza_bruta(8, 62, -5)


def test_ej2_entropia(m):
    assert m.entropia_bits("") == 0.0
    assert m.entropia_bits("abcdef") == pytest.approx(6 * math.log2(26))
    assert m.entropia_bits("Abc123!x") == pytest.approx(8 * math.log2(26 + 26 + 10 + 32))
    assert m.entropia_bits("12345") == pytest.approx(5 * math.log2(10))


def test_ej3_fuzzear(m):
    def analizar(entrada):
        return 10 / len(entrada)        # falla con "" (ZeroDivision) y con None (TypeError)

    entradas = ["ok", "", "hola", None]
    assert m.fuzzear(analizar, entradas) == ["", None]
    assert m.fuzzear(lambda x: x, ["a", "b"]) == []


def test_ej4_formulario(m):
    info = m.analizar_formulario(FORM)
    assert info["accion"] == "/login"
    assert info["metodo"] == "post"
    assert info["campos"] == ["usuario", "clave", "csrf_token"]
    simple = m.analizar_formulario('<form><input name="q"></form>')
    assert simple == {"accion": None, "metodo": "get", "campos": ["q"]}


def test_ej5_endpoints(m):
    endpoints = [
        {"ruta": "/api/users", "metodo": "GET", "requiere_auth": False},
        {"ruta": "/api/users", "metodo": "DELETE", "requiere_auth": False},
        {"ruta": "/api/config", "metodo": "put", "requiere_auth": False},
        {"ruta": "/api/profile", "metodo": "POST", "requiere_auth": True},
        {"ruta": "/api/notes", "metodo": "patch", "requiere_auth": False},
    ]
    assert m.endpoints_inseguros(endpoints) == ["/api/config", "/api/notes", "/api/users"]
    assert m.endpoints_inseguros([]) == []
