import hashlib
import hmac


def test_ej1_vigenere(m):
    assert m.vigenere("ATTACKATDAWN", "LEMON") == "LXFOPVEFRNHR"
    assert m.vigenere("Ataque al amanecer!", "Clave") == "Cealyg ll vqcyexit!"
    assert m.vigenere("Cealyg ll vqcyexit!", "clave", descifrar=True) == "Ataque al amanecer!"


def test_ej2_romper(m):
    claro = "el equipo de seguridad revisa los registros del servidor cada manana para detectar intentos de acceso"
    cifrado = m_cesar(claro, 11)
    assert m.romper_cesar(cifrado) == (11, claro)
    assert m.romper_cesar(claro)[0] == 0


def m_cesar(texto, d):
    return "".join(chr((ord(c) - 97 + d) % 26 + 97) if c.isalpha() else c for c in texto)


def test_ej3_hash_formato(m):
    sal = bytes(range(16))
    h = m.hash_password("hunter2", sal, 1000)
    esperado = hashlib.pbkdf2_hmac("sha256", b"hunter2", sal, 1000).hex()
    assert h == f"pbkdf2_sha256$1000${sal.hex()}${esperado}"


def test_ej3_sal_y_verificacion(m):
    a, b = m.hash_password("igual", iteraciones=1000), m.hash_password("igual", iteraciones=1000)
    assert a != b, "cada hash debe llevar una sal aleatoria distinta"
    assert m.verificar_password("igual", a)
    assert not m.verificar_password("otra", a)
    assert not m.verificar_password("igual", "basura")


def test_ej4_hmac(m):
    esperado = hmac.new(b"clave", b"transferir 100", hashlib.sha256).hexdigest()
    assert m.firmar("transferir 100", "clave") == esperado
    assert m.verificar_firma("transferir 100", "clave", esperado)
    assert not m.verificar_firma("transferir 900", "clave", esperado)
    assert not m.verificar_firma("transferir 100", "otra", esperado)


def test_ej5_auditar(m):
    h = lambda p: hashlib.sha256(p.encode()).hexdigest()
    usuarios = {"ana": h("123456"), "luis": h("Kq7#vP2!xz"), "eva": h("password")}
    assert m.auditar_debiles(usuarios, ["password", "123456", "qwerty"]) == {"ana": "123456", "eva": "password"}
    assert m.auditar_debiles({}, ["x"]) == {}
