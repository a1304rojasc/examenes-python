import sqlite3

import pytest


@pytest.fixture
def con():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE usuarios (nombre TEXT PRIMARY KEY, hash TEXT NOT NULL)")
    c.execute("CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)")
    c.executemany("INSERT INTO productos (nombre, precio) VALUES (?, ?)", [
        ("Cable 100% cobre", 5.0), ("Router", 80.0), ("Cable_UTP", 3.0), ("Switch", 60.0), ("cable coaxial", 4.0),
    ])
    c.commit()
    yield c
    c.close()


def test_ej1_login(m, con):
    m.registrar(con, "ana", "Tr0ub4dor&3")
    h = con.execute("SELECT hash FROM usuarios").fetchone()[0]
    assert h.startswith("pbkdf2_sha256$10000$") and "Tr0ub4dor" not in h
    assert m.login(con, "ana", "Tr0ub4dor&3") is True
    assert m.login(con, "ana", "otra") is False
    assert m.login(con, "nadie", "Tr0ub4dor&3") is False
    assert m.login(con, "' OR '1'='1", "' OR '1'='1") is False


def test_ej2_busqueda(m, con):
    assert [p[1] for p in m.buscar_productos(con, "cable")] == ["Cable 100% cobre", "Cable_UTP", "cable coaxial"]
    assert [p[1] for p in m.buscar_productos(con, "%")] == ["Cable 100% cobre"]
    assert [p[1] for p in m.buscar_productos(con, "_")] == ["Cable_UTP"]
    assert [p[2] for p in m.buscar_productos(con, "", orden="precio", limite=2)] == [3.0, 4.0]
    assert m.buscar_productos(con, "' OR 1=1 --") == []


def test_ej2_validaciones(m, con):
    for orden in ["precio DESC", "nombre; DROP TABLE productos", "hash"]:
        with pytest.raises(ValueError):
            m.buscar_productos(con, "x", orden=orden)
    for limite in [0, 101, "5", -1]:
        with pytest.raises(ValueError):
            m.buscar_productos(con, "x", limite=limite)


def test_ej3_sqli(m):
    for malo in ["' OR '1'='1", "admin'--", "1; DROP TABLE usuarios", "x' and 1=1", "1 UNION ALL SELECT password FROM u", "/* */"]:
        assert m.parece_sqli(malo), malo
    for ok in ["O'Brien", "ana", "unión de vecinos", "Cable 100% cobre", "Seleccionar"]:
        assert not m.parece_sqli(ok), ok


def test_ej4_formulario(m):
    assert m.validar_formulario({"usuario": "ana_01", "email": "ana@example.com", "edad": "30"}) == {}
    assert m.validar_formulario({"usuario": "ana", "email": "ana@example.com", "edad": 18}) == {}
    errores = m.validar_formulario({"usuario": "A", "email": "malo", "edad": "17"})
    assert set(errores) == {"usuario", "email", "edad"}
    assert set(m.validar_formulario({})) == {"usuario", "email", "edad"}
    assert set(m.validar_formulario({"usuario": "ana", "email": "a@example.com", "edad": "treinta"})) == {"edad"}


def test_ej5_csrf(m):
    t1, t2 = m.generar_token_csrf(), m.generar_token_csrf()
    assert t1 != t2 and len(t1) >= 43
    assert all(c.isalnum() or c in "-_" for c in t1)
    assert m.verificar_csrf(t1, t1)
    assert not m.verificar_csrf(t1, t2)
    assert not m.verificar_csrf(t1, None) and not m.verificar_csrf(None, None) and not m.verificar_csrf("", "")
