def test_ej1_validas(m):
    for ip in ["192.0.2.1", "203.0.113.255", "::1", "2001:db8::1"]:
        assert m.es_ip_valida(ip), ip


def test_ej1_invalidas(m):
    for ip in ["300.1.1.1", "192.0.2", "example.com", "", "1.2.3.4.5"]:
        assert not m.es_ip_valida(ip), ip


def test_ej2_en_red(m):
    assert m.en_red("192.0.2.50", "192.0.2.0/24")
    assert not m.en_red("192.0.3.1", "192.0.2.0/24")
    assert m.en_red("198.51.100.130", "198.51.100.128/25")
    assert not m.en_red("198.51.100.127", "198.51.100.128/25")


def test_ej3_info(m):
    assert m.info_red("192.0.2.0/24") == {"red": "192.0.2.0", "broadcast": "192.0.2.255", "mascara": "255.255.255.0", "hosts": 254}
    assert m.info_red("203.0.113.77/28") == {"red": "203.0.113.64", "broadcast": "203.0.113.79", "mascara": "255.255.255.240", "hosts": 14}


def test_ej4_socket(m):
    assert m.eco_socketpair("hola") == "hola"
    assert m.eco_socketpair("contraseña ñ") == "contraseña ñ"


def test_ej5_url(m):
    assert m.parsear_url("https://example.com/login") == ("https", "example.com", 443)
    assert m.parsear_url("http://example.com") == ("http", "example.com", 80)
    assert m.parsear_url("http://www.example.com:8080/a?b=1") == ("http", "www.example.com", 8080)
