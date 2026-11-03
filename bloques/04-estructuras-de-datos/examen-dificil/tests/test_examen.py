IPS = ["203.0.113.5", "198.51.100.7", "203.0.113.5", "192.0.2.1", "198.51.100.7", "203.0.113.5", "192.0.2.9"]


def test_ej1_top(m):
    assert m.top_ips(IPS, 2) == [("203.0.113.5", 3), ("198.51.100.7", 2)]
    assert m.top_ips(IPS, 4) == [("203.0.113.5", 3), ("198.51.100.7", 2), ("192.0.2.1", 1), ("192.0.2.9", 1)]
    assert m.top_ips([], 3) == []


def test_ej2_agrupar(m):
    con = [("192.0.2.1", 22), ("192.0.2.2", 80), ("192.0.2.1", 22), ("192.0.2.0", 22)]
    assert m.agrupar_por_puerto(con) == {22: ["192.0.2.0", "192.0.2.1"], 80: ["192.0.2.2"]}
    assert m.agrupar_por_puerto([]) == {}


def test_ej3_mfa(m):
    usuarios = [
        {"nombre": "zoe", "admin": True, "mfa": False},
        {"nombre": "ana", "admin": True, "mfa": False},
        {"nombre": "luis", "admin": True, "mfa": True},
        {"nombre": "eva", "admin": False, "mfa": False},
    ]
    assert m.admins_sin_mfa(usuarios) == ["ana", "zoe"]
    assert m.admins_sin_mfa([]) == []


def test_ej4_diff(m):
    antes = ["allow 22", "allow 80", "deny all"]
    despues = ["allow 443", "allow 80", "deny all", "allow 22/192.0.2.0/24"]
    assert m.diff_reglas(antes, despues) == {"añadidas": ["allow 22/192.0.2.0/24", "allow 443"], "eliminadas": ["allow 22"]}
    assert m.diff_reglas(["a"], ["a"]) == {"añadidas": [], "eliminadas": []}


def test_ej5_umbral(m):
    assert m.valores_sobre_umbral([[1, 9], [5, 3, 7]], 4) == [9, 5, 7]
    assert m.valores_sobre_umbral([], 0) == []
    assert m.valores_sobre_umbral([[1], []], 1) == []
