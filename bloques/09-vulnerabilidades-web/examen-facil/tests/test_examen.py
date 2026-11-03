import sqlite3

import pytest


@pytest.fixture
def con():
    c = sqlite3.connect(":memory:")
    c.execute("CREATE TABLE usuarios (id INTEGER PRIMARY KEY, nombre TEXT, email TEXT)")
    c.executemany("INSERT INTO usuarios (nombre, email) VALUES (?, ?)",
                  [("ana", "ana@example.com"), ("luis", "luis@example.com")])
    c.commit()
    yield c
    c.close()


def test_ej1_buscar(m, con):
    assert m.buscar_usuario(con, "ana") == (1, "ana", "ana@example.com")
    assert m.buscar_usuario(con, "nadie") is None
    assert m.buscar_usuario(con, "' OR '1'='1") is None
    assert m.buscar_usuario(con, "ana' --") is None


def test_ej2_sqli(m):
    for malo in ["' OR '1'='1", "admin'--", "1; DROP TABLE usuarios", "x' and 1=1", "1 UNION ALL SELECT clave FROM u", "/*c*/"]:
        assert m.parece_sqli(malo), malo
    for ok in ["ana", "O'Brien", "unión de vecinos", "Seleccionar todo"]:
        assert not m.parece_sqli(ok), ok


def test_ej3_escape(m):
    assert m.escapar_html("<script>alert(1)</script>") == "&lt;script&gt;alert(1)&lt;/script&gt;"
    assert m.escapar_html('a "b" & \'c\'') == "a &quot;b&quot; &amp; &#x27;c&#x27;"


def test_ej4_csrf(m):
    html = '<form><input type="hidden" name="csrf_token" value="xyz123"><input name="q"></form>'
    assert m.extraer_token_csrf(html) == "xyz123"
    assert m.extraer_token_csrf('<input name="CSRFMiddleware" value="abc">') == "abc"
    assert m.extraer_token_csrf('<form><input name="q"></form>') is None


def test_ej5_url(m):
    permitidos = {"example.com", "api.example.com"}
    assert m.url_permitida("https://example.com/panel", permitidos) is True
    assert m.url_permitida("http://api.example.com/v1", permitidos) is True
    assert m.url_permitida("https://evil.com", permitidos) is False
    assert m.url_permitida("ftp://example.com", permitidos) is False
    assert m.url_permitida("javascript:alert(1)", permitidos) is False
