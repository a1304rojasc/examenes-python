import socket


def test_ej1_agrupar(m):
    ips = ["192.0.2.10", "192.0.2.9", "198.51.100.1", "192.0.2.200"]
    assert m.agrupar_por_red(ips, 24) == {"192.0.2.0/24": ["192.0.2.9", "192.0.2.10", "192.0.2.200"], "198.51.100.0/24": ["198.51.100.1"]}
    assert m.agrupar_por_red(["192.0.2.10", "192.0.2.200"], 25) == {"192.0.2.0/25": ["192.0.2.10"], "192.0.2.128/25": ["192.0.2.200"]}


def test_ej2_allowlist(m):
    redes = ["192.0.2.0/24", "198.51.100.128/25"]
    ips = ["192.0.2.5", "203.0.113.9", "198.51.100.200", "198.51.100.5", "no-es-ip"]
    assert m.fuera_de_allowlist(ips, redes) == ["203.0.113.9", "198.51.100.5", "no-es-ip"]
    assert m.fuera_de_allowlist([], redes) == []


def test_ej3_peticion(m):
    raw = "POST /login HTTP/1.1\r\nHost: example.com\r\nContent-Type: application/x-www-form-urlencoded\r\nX-Test:  a:b \r\n\r\nuser=ana&pw=x"
    p = m.parsear_peticion(raw)
    assert (p["metodo"], p["ruta"], p["version"]) == ("POST", "/login", "HTTP/1.1")
    assert p["cabeceras"] == {"host": "example.com", "content-type": "application/x-www-form-urlencoded", "x-test": "a:b"}
    assert p["cuerpo"] == "user=ana&pw=x"


def test_ej3_sin_cuerpo(m):
    p = m.parsear_peticion("GET / HTTP/1.0\r\nHost: example.com\r\n\r\n")
    assert p["cuerpo"] == "" and p["ruta"] == "/"


def test_ej4_respuesta(m):
    r = m.respuesta_http(200, "hola")
    assert isinstance(r, bytes)
    assert r == b"HTTP/1.1 200 OK\r\nContent-Type: text/plain; charset=utf-8\r\nContent-Length: 4\r\n\r\nhola"


def test_ej4_bytes_utf8(m):
    r = m.respuesta_http(404, "¡no está!")
    assert r.startswith(b"HTTP/1.1 404 Not Found\r\n")
    assert b"Content-Length: 11\r\n" in r
    assert r.endswith("¡no está!".encode())


def test_ej5_puerto(m):
    servidor = socket.socket()
    servidor.bind(("127.0.0.1", 0))
    servidor.listen()
    puerto = servidor.getsockname()[1]
    try:
        assert m.puerto_abierto("127.0.0.1", puerto) is True
    finally:
        servidor.close()
    assert m.puerto_abierto("127.0.0.1", puerto, timeout=0.5) is False
