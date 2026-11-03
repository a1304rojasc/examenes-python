import pytest


def test_ej1_convertir(m):
    assert m.convertir_enteros(["1", "x", "3", None, 4.7]) == [1, 0, 3, 0, 4]
    assert m.convertir_enteros(["?"], defecto=-1) == [-1]
    assert m.convertir_enteros([]) == []


def test_ej2_registrar(m, tmp_path):
    log = tmp_path / "app.log"
    assert m.registrar(log, "INFO", "inicio") == 1
    assert m.registrar(log, "ERROR", "fallo") == 2
    assert log.read_text(encoding="utf-8") == "INFO: inicio\nERROR: fallo\n"


def test_ej2_nivel_invalido(m, tmp_path):
    log = tmp_path / "app.log"
    with pytest.raises(ValueError):
        m.registrar(log, "DEBUG", "x")
    assert not log.exists()


def test_ej3_buscar(m, tmp_path):
    (tmp_path / "var" / "log").mkdir(parents=True)
    (tmp_path / "a.log").write_text("")
    (tmp_path / "var" / "log" / "auth.log").write_text("")
    (tmp_path / "var" / "notas.txt").write_text("")
    assert m.buscar_archivos(tmp_path, "log") == ["a.log", "var/log/auth.log"]
    assert m.buscar_archivos(tmp_path, "csv") == []


def test_ej4_copiar(m, tmp_path):
    origen = tmp_path / "auth.log"
    origen.write_text("Failed password\naccepted\nFAILED again\n", encoding="utf-8")
    destino = tmp_path / "fallos.log"
    assert m.copiar_filtrando(origen, destino, "failed") == 2
    assert destino.read_text(encoding="utf-8") == "Failed password\nFAILED again\n"


def test_ej4_origen_inexistente(m, tmp_path):
    destino = tmp_path / "salida.log"
    with pytest.raises(FileNotFoundError):
        m.copiar_filtrando(tmp_path / "nada.log", destino, "x")
    assert not destino.exists()


def test_ej5_ruta_segura(m, tmp_path):
    (tmp_path / "subidas").mkdir()
    base = tmp_path / "subidas"
    assert m.ruta_segura(base, "foto.png") == (base / "foto.png").resolve()
    assert m.ruta_segura(base, "a/../b.txt") == (base / "b.txt").resolve()
    for malo in ["../secreto.txt", "../../etc/passwd", str(tmp_path / "otro.txt")]:
        with pytest.raises(ValueError):
            m.ruta_segura(base, malo)
