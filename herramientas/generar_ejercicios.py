#!/usr/bin/env python3
"""Genera ejercicios.py (plantilla para el alumno) a partir de solucion.py.

Conserva imports, constantes (salvo las PATRON_*, que son parte de la
solución), firmas y docstrings; sustituye el cuerpo de
cada función por `raise NotImplementedError`.

Uso:  python herramientas/generar_ejercicios.py [ruta/a/examen ...]
Sin argumentos regenera todos los exámenes de bloques/.
"""
import ast
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

CABECERA = '''"""{titulo}

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py {bloque} {nivel}
"""
'''


def generar(examen: Path) -> None:
    fuente = (examen / "solucion.py").read_text(encoding="utf-8")
    lineas = fuente.splitlines()
    arbol = ast.parse(fuente)
    bloque = examen.parent.name.split("-")[0]
    nivel = "facil" if examen.name.endswith("facil") else "dificil"
    titulo = f"Bloque {bloque} · Examen {'fácil' if nivel == 'facil' else 'difícil'} — ejercicios"
    previo_import = False
    salida = [CABECERA.format(titulo=titulo, bloque=bloque, nivel=nivel)]
    for nodo in arbol.body:
        if isinstance(nodo, ast.Expr) and isinstance(getattr(nodo, "value", None), ast.Constant) and nodo is arbol.body[0]:
            continue  # docstring del módulo
        if isinstance(nodo, ast.Assign) and any(
            getattr(t, "id", "").startswith("PATRON") or getattr(t, "id", "").startswith("_") for t in nodo.targets
        ):
            continue  # patrones y ayudantes privados (_) son parte de la solución
        if isinstance(nodo, ast.FunctionDef):
            if nodo.name.startswith("_"):
                continue  # función ayudante privada: no se regala ni se pide como ejercicio
            inicio = (nodo.decorator_list[0].lineno if nodo.decorator_list else nodo.lineno) - 1
            primero = nodo.body[0]
            tiene_doc = isinstance(primero, ast.Expr) and isinstance(primero.value, ast.Constant) and isinstance(primero.value.value, str)
            fin = primero.end_lineno if tiene_doc else primero.lineno - 1
            bloque_txt = lineas[inicio:fin]
            sangria = " " * (primero.col_offset)
            salida.append("\n".join(bloque_txt) + f"\n{sangria}raise NotImplementedError(\"Implementa {nodo.name}\")\n")
        else:
            segmento = ast.get_source_segment(fuente, nodo)
            if salida and salida[-1].startswith("#cod#"):
                es_import = isinstance(nodo, (ast.Import, ast.ImportFrom))
                sep = "\n" if es_import == previo_import else "\n\n"
                salida[-1] += sep + segmento  # imports/constantes seguidos
            else:
                salida.append("#cod#" + segmento)
            previo_import = isinstance(nodo, (ast.Import, ast.ImportFrom))
    texto = "\n\n\n".join(s.removeprefix("#cod#").rstrip("\n") for s in salida) + "\n"
    (examen / "ejercicios.py").write_text(texto, encoding="utf-8")
    print(f"generado {examen.relative_to(RAIZ)}/ejercicios.py")


def main(args):
    examenes = [Path(a).resolve() for a in args] or sorted(RAIZ.glob("bloques/*/examen-*"))
    for ex in examenes:
        if (ex / "solucion.py").exists():
            generar(ex)


if __name__ == "__main__":
    main(sys.argv[1:])
