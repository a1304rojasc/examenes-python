"""Tests de la lección 5.6. Sin consultas a internet: localhost, mensajes en memoria y zonas de texto."""

import dns.message
import dns.rrset

ZONA_BUENA = """
$TTL 3600
@       IN SOA ns1.campus.example. admin.campus.example. 1 7200 3600 1209600 3600
@       IN NS  ns1.campus.example.
@       IN MX  20 respaldo.campus.example.
@       IN MX  10 correo.campus.example.
@       IN MX  30 ultimo.campus.example.
@       IN TXT "google-site-verification=abc123"
@       IN TXT "v=spf1 ip4:192.0.2.0/24 " "include:_spf.campus.example -all"
correo  IN A   192.0.2.25
"""

ZONA_SIN_SPF = """
$TTL 300
@   IN SOA ns1.utec-campus.example. x.utec-campus.example. 1 7200 3600 1209600 300
@   IN NS  ns1.utec-campus.example.
@   IN A   203.0.113.66
"""


def _zona_con_spf(spf):
    return f"""
$TTL 300
@   IN SOA ns1.d.example. x.d.example. 1 7200 3600 1209600 300
@   IN NS  ns1.d.example.
@   IN MX  5 mx.d.example.
@   IN TXT "{spf}"
"""


def test_ej1_localhost(m):
    r = m.direcciones_ipv4(["localhost"])
    assert "127.0.0.1" in r["localhost"]
    assert r["localhost"] == sorted(set(r["localhost"]))
    assert all(":" not in ip for ip in r["localhost"])


def test_ej1_nombre_inexistente_no_detiene(m):
    r = m.direcciones_ipv4(["no-existe.invalid", "localhost"])
    assert r["no-existe.invalid"] == []
    assert "127.0.0.1" in r["localhost"]


def _respuesta():
    consulta = dns.message.make_query("campus.example", "A")
    respuesta = dns.message.make_response(consulta)
    respuesta.answer.append(dns.rrset.from_text("campus.example.", 300, "IN", "A", "192.0.2.80", "192.0.2.10"))
    respuesta.answer.append(dns.rrset.from_text("www.campus.example.", 60, "IN", "CNAME", "campus.example."))
    respuesta.answer.append(dns.rrset.from_text("campus.example.", 3600, "IN", "MX", "10 correo.campus.example."))
    return respuesta.to_wire()


def test_ej2_registros(m):
    assert m.registros(_respuesta()) == [
        ("campus.example", "A", "192.0.2.10", 300),
        ("campus.example", "A", "192.0.2.80", 300),
        ("campus.example", "MX", "10 correo.campus.example.", 3600),
        ("www.campus.example", "CNAME", "campus.example.", 60),
    ]


def test_ej2_respuesta_vacia(m):
    vacia = dns.message.make_response(dns.message.make_query("nada.example", "A")).to_wire()
    assert m.registros(vacia) == []


def test_ej3_zona_bien_configurada(m):
    assert m.politica_correo(ZONA_BUENA, "campus.example") == {
        "mx": ["correo.campus.example", "respaldo.campus.example", "ultimo.campus.example"],
        "spf": "v=spf1 ip4:192.0.2.0/24 include:_spf.campus.example -all",
        "riesgo": "bajo",
    }


def test_ej3_sin_spf_es_riesgo_alto(m):
    assert m.politica_correo(ZONA_SIN_SPF, "utec-campus.example") == {"mx": [], "spf": None, "riesgo": "alto"}


def test_ej3_niveles_de_riesgo(m):
    assert m.politica_correo(_zona_con_spf("v=spf1 +all"), "d.example")["riesgo"] == "alto"
    assert m.politica_correo(_zona_con_spf("v=spf1 mx ~all"), "d.example")["riesgo"] == "medio"
    assert m.politica_correo(_zona_con_spf("v=spf1 mx ?all"), "d.example")["riesgo"] == "medio"
    assert m.politica_correo(_zona_con_spf("v=spf1 mx -all"), "d.example") == {
        "mx": ["mx.d.example"], "spf": "v=spf1 mx -all", "riesgo": "bajo",
    }
