import sqlite3

import pytest


@pytest.fixture
def con(m):
    c = sqlite3.connect(":memory:")
    m.crear_tabla(c)
    yield c
    c.close()


def test_ej1_usuario(m):
    for ok in ["ana", "soc_admin_01", "a" * 16]:
        assert m.validar_usuario(ok), ok
    for malo in ["ab", "a" * 17, "Ana", "ana lopez", "ana'--", "ana\n", ""]:
        assert not m.validar_usuario(malo), malo


def test_ej2_html(m):
    assert m.escapar_html("<script>alert(1)</script>") == "&lt;script&gt;alert(1)&lt;/script&gt;"
    assert m.escapar_html('"a" & \'b\'') == "&quot;a&quot; &amp; &#x27;b&#x27;"


def test_ej3_insertar(m, con):
    assert m.insertar_usuario(con, "ana", "ana@example.com") == 1
    assert m.insertar_usuario(con, "o'brien", "ob@example.com") == 2
    assert con.execute("SELECT nombre FROM usuarios ORDER BY id").fetchall() == [("ana",), ("o'brien",)]


def test_ej3_unico(m, con):
    m.insertar_usuario(con, "ana", "a@example.com")
    with pytest.raises(sqlite3.IntegrityError):
        m.insertar_usuario(con, "ana", "b@example.com")


def test_ej4_buscar(m, con):
    m.insertar_usuario(con, "ana", "ana@example.com")
    m.insertar_usuario(con, "luis", "luis@example.com")
    assert m.buscar_usuario(con, "luis") == (2, "luis", "luis@example.com")
    assert m.buscar_usuario(con, "nadie") is None


def test_ej4_inyeccion(m, con):
    m.insertar_usuario(con, "ana", "ana@example.com")
    assert m.buscar_usuario(con, "' OR '1'='1") is None
    assert m.buscar_usuario(con, "ana' --") is None


def test_ej5_orden(m):
    assert m.columna_orden("nombre") == "nombre"
    for malo in ["nombre; DROP TABLE usuarios", "password", "", "NOMBRE"]:
        with pytest.raises(ValueError):
            m.columna_orden(malo)
