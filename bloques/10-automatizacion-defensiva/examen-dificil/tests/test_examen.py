import json

import pytest


def linea(seg, ip, usuario="root", invalido=False):
    m, s = divmod(seg, 60)
    inv = "invalid user " if invalido else ""
    return f"Mar 10 08:{m:02d}:{s:02d} servidor sshd[1234]: Failed password for {inv}{usuario} from {ip} port 5{seg:04d} ssh2"


LOG = (
    [linea(s, "203.0.113.5") for s in (0, 5, 10, 15, 20, 25)]           # 6 en 25 s
    + [linea(s, "198.51.100.7", "admin", True) for s in (0, 100, 200, 300, 400)]  # dispersos
    + [linea(s, "192.0.2.50") for s in (30, 31, 32, 33, 34)]            # 5 en 4 s
    + ["Mar 10 08:00:40 servidor sshd[99]: Accepted password for ana from 192.0.2.10 port 50000 ssh2",
       "Mar 10 08:00:41 servidor sshd[99]: Failed password for root from no.es.una.ip port 1 ssh2"]
)


def test_ej1_detectar(m):
    assert m.detectar_fuerza_bruta(LOG) == {"203.0.113.5": 6, "192.0.2.50": 5}
    assert m.detectar_fuerza_bruta(LOG, umbral=6) == {"203.0.113.5": 6}
    assert m.detectar_fuerza_bruta(LOG, umbral=2, ventana=100) == {"203.0.113.5": 6, "192.0.2.50": 5, "198.51.100.7": 2}
    assert m.detectar_fuerza_bruta([]) == {}


def test_ej2_informe(m):
    alertas = {"192.0.2.50": 5, "203.0.113.5": 6, "192.0.2.9": 5}
    assert m.generar_informe(alertas) == (
        "ALERTA 203.0.113.5: 6 fallos en ventana\n"
        "ALERTA 192.0.2.9: 5 fallos en ventana\n"
        "ALERTA 192.0.2.50: 5 fallos en ventana"
    )
    assert m.generar_informe({}) == "Sin alertas"
    assert json.loads(m.generar_informe(alertas, como_json=True)) == alertas


def test_ej3_cli(m, tmp_path, capsys):
    log = tmp_path / "auth.log"
    log.write_text("\n".join(LOG) + "\n", encoding="utf-8")
    assert m.main([str(log)]) == 1
    salida = capsys.readouterr().out
    assert "ALERTA 203.0.113.5: 6 fallos en ventana" in salida and "198.51.100.7" not in salida
    assert m.main([str(log), "--umbral", "10"]) == 0
    assert "Sin alertas" in capsys.readouterr().out
    assert m.main([str(log), "--json", "--umbral", "6"]) == 1
    assert json.loads(capsys.readouterr().out) == {"203.0.113.5": 6}


def test_ej4_reglas(m):
    ips = ["203.0.113.5", "192.0.2.50", "198.51.100.7", "203.0.113.5", "203.0.113.10"]
    assert m.reglas_bloqueo(ips, ["192.0.2.0/24"]) == ["DENY 198.51.100.7", "DENY 203.0.113.5", "DENY 203.0.113.10"]
    assert m.reglas_bloqueo(ips, ["0.0.0.0/0"]) == []
    assert m.reglas_bloqueo([], []) == []


# --- Ejercicio 5: los tests del alumno deben distinguir el detector bueno de los mutantes ---

def _ventana(t, v):
    t, mejor, i = sorted(t), 0, 0
    for j in range(len(t)):
        while t[j] - t[i] > v:
            i += 1
        mejor = max(mejor, j - i + 1)
    return mejor


def bueno(t, u, v):
    return _ventana(t, v) >= u


def mutante_mayor_estricto(t, u, v):
    return _ventana(t, v) > u


def mutante_sin_ventana(t, u, v):
    return len(t) >= u


def mutante_no_ordena(t, u, v):
    mejor, i = 0, 0
    for j in range(len(t)):
        while i < j and t[j] - t[i] > v:
            i += 1
        mejor = max(mejor, j - i + 1)
    return mejor >= u


def mutante_ventana_exclusiva(t, u, v):
    return _ventana(t, v - 1) >= u


def mutante_siempre_falso(t, u, v):
    return False


def test_ej5_acepta_correcto(m):
    m.verificar_detector(bueno)


@pytest.mark.parametrize("mutante", [mutante_mayor_estricto, mutante_sin_ventana, mutante_no_ordena,
                                     mutante_ventana_exclusiva, mutante_siempre_falso])
def test_ej5_detecta_mutantes(m, mutante):
    with pytest.raises(AssertionError):
        m.verificar_detector(mutante)
