#!/usr/bin/env python3
"""Corrector automático de exámenes.

Uso:
    python corregir.py P facil           # corrige bloques/P-*/examen-facil/ejercicios.py
    python corregir.py 06 dificil
    python corregir.py 6 facil --solucion    # comprueba la solución oficial
    python corregir.py todo [--solucion]     # todos los exámenes

Nota: cada uno de los 5 ejercicios de código vale 1 punto. Un ejercicio
cuenta solo si TODOS sus tests pasan. La parte teórica se corrige a mano
con soluciones.md.
"""
import re
import sys
from pathlib import Path

try:
    import pytest
except ImportError:
    sys.exit("Falta pytest. Instálalo con:  pip install pytest")

RAIZ = Path(__file__).resolve().parent
NIVELES = {"facil": "examen-facil", "fácil": "examen-facil", "dificil": "examen-dificil", "difícil": "examen-dificil"}


def _clave_orden(bloque: Path):
    """Ordena los bloques: P primero, luego 06, 07, ... numéricamente."""
    prefijo = bloque.name.split("-")[0]
    return (0, 0) if prefijo.upper() == "P" else (1, int(prefijo))


def bloques_ordenados():
    return sorted((RAIZ / "bloques").glob("*-*"), key=_clave_orden)


class Recolector:
    def __init__(self):
        self.ejercicios = {}  # n -> lista de (nombre_test, ok, mensaje)

    def pytest_runtest_logreport(self, report):
        if report.when == "call" or (report.when == "setup" and report.failed):
            coincidencia = re.search(r"test_ej(\d+)", report.nodeid)
            if not coincidencia:
                return
            n = int(coincidencia.group(1))
            mensaje = ""
            if report.failed:
                crash = getattr(report.longrepr, "reprcrash", None)
                mensaje = crash.message.splitlines()[0] if crash else str(report.longrepr).splitlines()[-1]
            nombre = report.nodeid.split("::")[-1]
            self.ejercicios.setdefault(n, []).append((nombre, report.passed, mensaje))


def buscar_examen(bloque: str, nivel: str) -> Path:
    nivel_dir = NIVELES.get(nivel.lower())
    if not nivel_dir:
        sys.exit(f"Nivel desconocido: {nivel!r}. Usa 'facil' o 'dificil'.")
    prefijo = bloque.upper() if bloque.upper() == "P" else bloque.zfill(2)
    candidatos = sorted((RAIZ / "bloques").glob(f"{prefijo}-*"))
    if not candidatos:
        sys.exit(f"No existe el bloque {bloque}.")
    return candidatos[0] / nivel_dir


def corregir(examen: Path, solucion: bool, detalle: bool = True) -> int:
    rec = Recolector()
    args = [str(examen / "tests"), "-c", str(RAIZ / "pytest.ini"), "--rootdir", str(RAIZ), "-p", "no:terminal"]
    if solucion:
        args.append("--solucion")
    pytest.main(args, plugins=[rec])
    nota = 0
    for n in range(1, 6):
        resultados = rec.ejercicios.get(n, [])
        ok = bool(resultados) and all(r[1] for r in resultados)
        nota += ok
        if detalle:
            pasados = sum(r[1] for r in resultados)
            print(f"  Ejercicio {n}: {'✔ correcto' if ok else '✘ incorrecto'}  ({pasados}/{len(resultados)} tests)")
            if not ok:
                for nombre, paso, msg in resultados:
                    if not paso:
                        print(f"      - {nombre}: {msg[:110]}")
                        if "NotImplementedError" in msg:
                            break
    return nota


def main(argv):
    solucion = "--solucion" in argv
    argv = [a for a in argv if a != "--solucion"]
    archivo = "solucion.py" if solucion else "ejercicios.py"
    if argv and argv[0] == "todo":
        total = 0
        for bloque in bloques_ordenados():
            for nivel in ("examen-facil", "examen-dificil"):
                nota = corregir(bloque / nivel, solucion, detalle=False)
                total += nota
                print(f"{bloque.name:<34} {nivel:<15} {nota}/5")
        print(f"\nTotal: {total} ejercicios correctos ({archivo})")
        return 0
    if len(argv) != 2:
        print(__doc__)
        return 2
    examen = buscar_examen(argv[0], argv[1])
    print(f"Corrigiendo {examen.relative_to(RAIZ)}/{archivo}\n")
    nota = corregir(examen, solucion)
    print(f"\nNota de código: {nota}/5")
    mensajes = {5: "¡Excelente! Examen perfecto.", 4: "Muy bien, revisa el ejercicio que falló.",
                3: "Aprobado. Repasa los ejercicios fallidos.", }
    print(mensajes.get(nota, "Sigue practicando: repasa el bloque (repaso.md) y vuelve a intentarlo."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
