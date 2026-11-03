import sqlite3

import pytest


@pytest.fixture
def con():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
    c.executemany("INSERT INTO productos (nombre, precio) VALUES (?, ?)", [
        ("Cable 100% cobre", 5.0), ("Router", 80.0), ("Cable_UTP", 3.0), ("cable coaxial", 4.0)])
    c.commit()
    yield c
    c.close()


def test_ej1_buscar(m, con):
    assert [p[1] for p in m.buscar_productos(con, "cable")] == ["Cable 100% cobre", "Cable_UTP", "cable coaxial"]
    assert [p[1] for p in m.buscar_productos(con, "%")] == ["Cable 100% cobre"]
    assert [p[1] for p in m.buscar_productos(con, "_")] == ["Cable_UTP"]
    assert [p[2] for p in m.buscar_productos(con, "", orden="precio", limite=2)] == [3.0, 4.0]
    assert m.buscar_productos(con, "' OR 1=1 --") == []


def test_ej1_validaciones(m, con):
    for orden in ["precio DESC", "nombre; DROP TABLE productos", "clave"]:
        with pytest.raises(ValueError):
            m.buscar_productos(con, "x", orden=orden)
    for limite in [0, 101, "5", -1, True]:
        with pytest.raises(ValueError):
            m.buscar_productos(con, "x", limite=limite)


def test_ej2_reflejo(m):
    assert m.reflejo_sin_escapar("<script>", "<html><script>...</html>") is True
    assert m.reflejo_sin_escapar("<script>", "&lt;script&gt;") is False
    assert m.reflejo_sin_escapar("hola", "bienvenido hola") is False
    assert m.reflejo_sin_escapar("<b>", "texto <b> negrita") is True


def test_ej3_destino(m):
    assert m.destino_seguro("/panel/inicio", "example.com") is True
    assert m.destino_seguro("https://example.com/x", "example.com") is True
    assert m.destino_seguro("https://evil.com", "example.com") is False
    assert m.destino_seguro("//evil.com", "example.com") is False
    assert m.destino_seguro("/\\evil.com", "example.com") is False
    assert m.destino_seguro("https://example.com@evil.com/", "example.com") is False
    assert m.destino_seguro("javascript:alert(1)", "example.com") is False


def test_ej4_ssrf(m):
    for interno in ["http://127.0.0.1/", "http://169.254.169.254/latest/meta-data/",
                    "http://10.0.0.5/", "http://192.168.1.1/", "http://[::1]/", "http://localhost:8080/"]:
        assert m.apunta_a_interno(interno) is True, interno
    for externo in ["http://93.184.216.34/", "https://example.com/", "http://api.example.com/v1"]:
        assert m.apunta_a_interno(externo) is False, externo


def test_ej5_inventario(m):
    html = (
        '<form action="/login" method="POST"><input name="u"><input type="hidden" name="csrf" value="t1"></form>'
        '<form><input name="q"></form>'
    )
    inv = m.inventario_formularios(html)
    assert len(inv) == 2
    assert inv[0] == {"accion": "/login", "metodo": "post", "campos": ["u", "csrf"], "token_csrf": "t1"}
    assert inv[1] == {"accion": None, "metodo": "get", "campos": ["q"], "token_csrf": None}
