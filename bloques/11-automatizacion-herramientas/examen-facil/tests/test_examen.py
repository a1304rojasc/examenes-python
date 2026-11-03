import pytest


def test_ej1_parser(m):
    p = m.crear_parser()
    a = p.parse_args(["escanear", "192.0.2.10"])
    assert a.comando == "escanear" and a.objetivo == "192.0.2.10" and a.puertos == "1-1024"
    a = p.parse_args(["escanear", "example.com", "--puertos", "22,80"])
    assert a.puertos == "22,80"
    a = p.parse_args(["reportar", "salida.txt", "--json"])
    assert a.comando == "reportar" and a.archivo == "salida.txt" and a.json is True
    with pytest.raises(SystemExit):
        p.parse_args(["escanear"])   # falta el objetivo


def test_ej2_log(m):
    assert m.linea_log("INFO", "acceso", {"usuario": "ana", "ip": "192.0.2.1"}) == "[INFO] acceso | ip=192.0.2.1 usuario=ana"
    assert m.linea_log("ERROR", "fallo", {}) == "[ERROR] fallo"


def test_ej3_vt(m):
    r = {"data": {"attributes": {"last_analysis_stats": {"malicious": 7, "harmless": 60}}}}
    assert m.detecciones_vt(r) == 7
    assert m.detecciones_vt({"data": {"attributes": {"last_analysis_stats": {"harmless": 70}}}}) == 0
    assert m.detecciones_vt({}) == 0
    assert m.detecciones_vt({"data": {}}) == 0


def test_ej4_hibp(m):
    respuesta = "0018A45C4D1DEF81644B54AB7F969B88D65:3\r\n00D4F6E8FA6EECAD2A3AA415EEC418D38EC:17\r\nFFFF:1"
    assert m.veces_filtrada(respuesta, "00D4F6E8FA6EECAD2A3AA415EEC418D38EC") == 17
    assert m.veces_filtrada(respuesta, "0018a45c4d1def81644b54ab7f969b88d65") == 3
    assert m.veces_filtrada(respuesta, "ABCDEF") == 0


def test_ej5_apikey(m):
    assert m.leer_api_key({"VT_API_KEY": "secreto123"}, "VT_API_KEY") == "secreto123"
    with pytest.raises(ValueError):
        m.leer_api_key({}, "VT_API_KEY")
    with pytest.raises(ValueError):
        m.leer_api_key({"VT_API_KEY": ""}, "VT_API_KEY")
