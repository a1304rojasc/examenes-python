def test_ej1_xor(m):
    claro = "FLAG{xor_de_un_byte}"
    cifrado = bytes(b ^ 0x42 for b in claro.encode("latin-1"))
    assert m.romper_xor_un_byte(cifrado, "FLAG{") == (0x42, claro)
    assert m.romper_xor_un_byte(cifrado, "NADA") is None


def test_ej2_alertas(m):
    eventos = (
        [{"ts": t, "ip": "203.0.113.5", "tipo": "login_fallido"} for t in (0, 5, 10, 15, 20)]
        + [{"ts": t, "ip": "198.51.100.7", "tipo": "login_fallido"} for t in (0, 100, 200)]
        + [{"ts": 1, "ip": "203.0.113.5", "tipo": "login_ok"}]
        + [{"ts": t, "ip": "192.0.2.9", "tipo": "login_fallido"} for t in (0, 1, 2, 3, 4)]
    )
    assert m.alertas_fuerza_bruta(eventos, 5, 60) == ["192.0.2.9", "203.0.113.5"]
    assert m.alertas_fuerza_bruta(eventos, 6, 60) == []
    assert m.alertas_fuerza_bruta(eventos, 3, 300) == ["192.0.2.9", "198.51.100.7", "203.0.113.5"]


def test_ej3_agrupar(m):
    alertas = [
        {"tipo": "sqli", "origen": "203.0.113.5", "ts": 100},
        {"tipo": "sqli", "origen": "203.0.113.5", "ts": 50},
        {"tipo": "sqli", "origen": "203.0.113.5", "ts": 120},
        {"tipo": "xss", "origen": "198.51.100.7", "ts": 10},
    ]
    assert m.agrupar_alertas(alertas) == [
        {"tipo": "sqli", "origen": "203.0.113.5", "conteo": 3, "primero": 50, "ultimo": 120},
        {"tipo": "xss", "origen": "198.51.100.7", "conteo": 1, "primero": 10, "ultimo": 10},
    ]
    assert m.agrupar_alertas([]) == []


def test_ej4_servicios(m):
    texto = "PORT     STATE  SERVICE\n22/tcp   open   ssh\n80/tcp   closed http\n443/tcp  open   https\nbasura\n53/udp open dns"
    assert m.parsear_servicios(texto) == [{"puerto": 22, "servicio": "ssh"}, {"puerto": 443, "servicio": "https"}]
    assert m.parsear_servicios("") == []


def test_ej5_ciclico(m):
    patron = m.generar_ciclico(100)
    assert len(patron) == 100
    # cada ventana de 4 es única
    ventanas = [patron[i:i + 4] for i in range(len(patron) - 3)]
    assert len(ventanas) == len(set(ventanas))
    fragmento = patron[42:46]
    assert m.posicion_ciclico(patron, fragmento) == 42
    assert m.posicion_ciclico(patron, "ZZZZ") == -1
