L1 = "Mar 10 08:15:01 servidor sshd[1234]: Failed password for root from 203.0.113.5 port 52211 ssh2"
L2 = "Mar 10 08:15:09 servidor sshd[1234]: Failed password for invalid user admin from 198.51.100.7 port 40022 ssh2"
L3 = "Mar 10 08:16:00 servidor sshd[1240]: Accepted password for ana from 192.0.2.10 port 50000 ssh2"
L4 = "Mar 10 08:17:00 servidor CRON[999]: pam_unix(cron:session): session opened for user root"


def test_ej1_espacios(m):
    assert m.normalizar_espacios("  hola   mundo \t ssh ") == "hola mundo ssh"
    assert m.normalizar_espacios("") == ""


def test_ej2_ips(m):
    assert m.extraer_ips(L1) == ["203.0.113.5"]
    assert m.extraer_ips("de 192.0.2.1 a 198.51.100.200 y 10.0.0") == ["192.0.2.1", "198.51.100.200"]
    assert m.extraer_ips("sin ips") == []


def test_ej3_fallida(m):
    assert m.es_linea_fallida(L1) and m.es_linea_fallida(L2)
    assert not m.es_linea_fallida(L3) and not m.es_linea_fallida(L4)


def test_ej4_usuario(m):
    assert m.extraer_usuario(L1) == "root"
    assert m.extraer_usuario(L2) == "admin"
    assert m.extraer_usuario(L3) == "ana"
    assert m.extraer_usuario(L4) is None


def test_ej5_email(m):
    for ok in ["ana@example.com", "soc.team+alertas@mail.example.org"]:
        assert m.es_email_valido(ok), ok
    for malo in ["ana@", "ana example.com", "a@b@example.com", "ana@example", "x ana@example.com", "ana@example.c"]:
        assert not m.es_email_valido(malo), malo
