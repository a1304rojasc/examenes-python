import argparse

import pytest


def test_ej1_rango(m):
    assert m.rango_de_puertos("1-1024") == (1, 1024)
    assert m.rango_de_puertos("80-80") == (80, 80)
    for malo in ["0-100", "1-70000", "100-20", "abc", "22", "1-2-3", "-5"]:
        with pytest.raises(argparse.ArgumentTypeError):
            m.rango_de_puertos(malo)


def test_ej2_filtrar(m):
    lineas = ["[DEBUG] detalle", "[INFO] arranque", "[WARNING] disco al 90%", "[ERROR] caida", "[CRITICAL] fuego", "ruido"]
    assert m.filtrar_por_nivel(lineas, "WARNING") == ["[WARNING] disco al 90%", "[ERROR] caida", "[CRITICAL] fuego"]
    assert m.filtrar_por_nivel(lineas, "DEBUG") == lineas[:5]
    assert m.filtrar_por_nivel(lineas, "CRITICAL") == ["[CRITICAL] fuego"]


def test_ej3_cache(m):
    llamadas = []

    def cliente(clave):
        llamadas.append(clave)
        return f"resultado-{clave}"

    cache = {}
    assert m.consultar_con_cache(cliente, "a", cache) == "resultado-a"
    assert m.consultar_con_cache(cliente, "a", cache) == "resultado-a"
    assert m.consultar_con_cache(cliente, "b", cache) == "resultado-b"
    assert llamadas == ["a", "b"]    # "a" solo se consultó una vez
    assert cache == {"a": "resultado-a", "b": "resultado-b"}


def test_ej4_shodan(m):
    respuesta = {"ports": [443, 22, 22], "data": [{"port": 22, "product": "OpenSSH"}, {"port": 443, "product": "nginx"}]}
    assert m.resumen_shodan(respuesta) == {"puertos": [22, 443], "servicios": {22: "OpenSSH", 443: "nginx"}}
    assert m.resumen_shodan({}) == {"puertos": [], "servicios": {}}


def test_ej5_iocs(m):
    feeds = [
        {"ips": ["203.0.113.10", "203.0.113.9", "no-ip"], "dominios": ["Example.com", "mal.test"]},
        {"ips": ["203.0.113.9", "999.1.1.1"], "dominios": ["example.com"]},
    ]
    assert m.consolidar_iocs(feeds) == {
        "ips": ["203.0.113.9", "203.0.113.10"],
        "dominios": ["example.com", "mal.test"],
    }
    assert m.consolidar_iocs([]) == {"ips": [], "dominios": []}
