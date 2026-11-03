def test_ej1_lineas(m, tmp_path):
    f = tmp_path / "a.txt"
    f.write_text("uno\ndos\ntres\n", encoding="utf-8")
    assert m.contar_lineas(f) == 3
    (tmp_path / "vacio.txt").write_text("")
    assert m.contar_lineas(tmp_path / "vacio.txt") == 0


def test_ej2_escribir(m, tmp_path):
    f = tmp_path / "salida.txt"
    f.write_text("viejo\n")
    m.escribir_lineas(f, ["ssh", "http"])
    assert f.read_text(encoding="utf-8") == "ssh\nhttp\n"
    m.escribir_lineas(f, [])
    assert f.read_text() == ""


def test_ej3_division(m):
    assert m.dividir_seguro(10, 4) == 2.5
    assert m.dividir_seguro(1, 0) is None


def test_ej4_config(m, tmp_path):
    f = tmp_path / "sshd.conf"
    f.write_text("# comentario\nPort = 22\n\nPermitRootLogin=no\nBanner=a=b\n", encoding="utf-8")
    assert m.leer_config(f) == {"Port": "22", "PermitRootLogin": "no", "Banner": "a=b"}


def test_ej4_no_existe(m, tmp_path):
    assert m.leer_config(tmp_path / "no_existe.conf") == {}


def test_ej5_extension(m):
    assert m.extension("logs/Auth.LOG") == "log"
    assert m.extension("datos.tar.gz") == "gz"
    assert m.extension("Makefile") == ""
