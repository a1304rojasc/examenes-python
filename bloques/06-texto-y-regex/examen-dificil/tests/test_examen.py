LOG = [
    "Mar 10 08:15:01 servidor sshd[1234]: Failed password for root from 203.0.113.5 port 52211 ssh2",
    "Mar 10 08:15:09 servidor sshd[1234]: Failed password for invalid user admin from 198.51.100.7 port 40022 ssh2",
    "Mar 10 08:15:12 servidor sshd[1234]: Failed password for invalid user test from 203.0.113.5 port 52212 ssh2",
    "Mar 10 08:16:00 servidor sshd[1240]: Accepted password for ana from 192.0.2.10 port 50000 ssh2",
    "Mar  9 23:59:59 bastion sshd[77]: Accepted publickey for luis from 192.0.2.11 port 50001 ssh2",
    "Mar 10 08:17:00 servidor CRON[999]: pam_unix(cron:session): session opened for user root",
    "Mar 10 08:18:00 servidor sshd[1250]: Failed password for invalid user admin from 203.0.113.9 port 1 ssh2",
]


def test_ej1_parsear_fallo(m):
    assert m.parsear_linea(LOG[1]) == {
        "fecha": "Mar 10 08:15:09", "host": "servidor", "pid": 1234, "evento": "Failed",
        "metodo": "password", "usuario": "admin", "invalido": True, "ip": "198.51.100.7", "puerto": 40022,
    }


def test_ej1_parsear_otros(m):
    d = m.parsear_linea(LOG[4])
    assert d["fecha"] == "Mar  9 23:59:59" and d["host"] == "bastion" and d["metodo"] == "publickey"
    assert d["invalido"] is False and d["usuario"] == "luis" and d["evento"] == "Accepted"
    assert m.parsear_linea(LOG[5]) is None
    assert m.parsear_linea("") is None


def test_ej2_fallos(m):
    assert m.fallos_por_ip(LOG) == {"203.0.113.5": 2, "198.51.100.7": 1, "203.0.113.9": 1}
    assert m.fallos_por_ip([]) == {}


def test_ej3_invalidos(m):
    assert m.usuarios_invalidos(LOG) == ["admin", "test"]


def test_ej4_ips(m):
    texto = "ok 192.0.2.1, malo 999.1.1.1, ok 203.0.113.255, repetida 192.0.2.1, malo 1.2.3.256"
    assert m.ips_validas(texto) == ["192.0.2.1", "203.0.113.255"]


def test_ej5_anonimizar(m):
    assert m.anonimizar(LOG[0]) == LOG[0].replace("203.0.113.5", "203.0.113.x")
    assert m.anonimizar("192.0.2.10 -> 198.51.100.200") == "192.0.2.x -> 198.51.100.x"
    assert m.anonimizar("sin ips") == "sin ips"
