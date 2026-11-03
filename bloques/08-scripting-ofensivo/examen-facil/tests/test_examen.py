WHOIS = """Domain Name: EXAMPLE.COM
Registrar: Ejemplo Registrar S.A.
Creation Date: 1997-08-14T04:00:00Z
Registrar WHOIS Server: whois.example-registrar.com
Registry Expiry Date: 2027-08-13T04:00:00Z
Registrar: Duplicado No Usar
"""

HTML = '<ul><li><a href="/panel">Panel</a></li><li><a href="https://example.com/ayuda">Ayuda</a></li><li><a>sin href</a></li></ul>'


def test_ej1_whois(m):
    assert m.extraer_campos_whois(WHOIS) == {
        "registrar": "Ejemplo Registrar S.A.",
        "creation date": "1997-08-14T04:00:00Z",
        "registry expiry date": "2027-08-13T04:00:00Z",
    }
    assert m.extraer_campos_whois("Sin campos relevantes: nada") == {}


def test_ej2_enlaces(m):
    assert m.extraer_enlaces(HTML) == ["/panel", "https://example.com/ayuda"]
    assert m.extraer_enlaces("<p>sin enlaces</p>") == []


def test_ej3_robots(m):
    reglas = ["/admin", "/privado", ""]
    assert m.permitido_por_robots(reglas, "/publico/index.html") is True
    assert m.permitido_por_robots(reglas, "/admin/panel") is False
    assert m.permitido_por_robots(reglas, "/privado") is False
    assert m.permitido_por_robots([], "/cualquiera") is True


def test_ej4_puertos(m):
    estados = {22: "open", 80: "filtered", 443: "open", 3306: "closed"}
    assert m.puertos_abiertos(estados) == [22, 443]
    assert m.puertos_abiertos({25: "closed"}) == []


def test_ej5_combinaciones(m):
    assert m.combinaciones_posibles(4, 10) == 10000
    assert m.combinaciones_posibles(1, 26) == 26
    assert m.combinaciones_posibles(8, 62) == 62 ** 8
    assert m.combinaciones_posibles(0, 95) == 1
