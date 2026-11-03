"""Configuración común de pytest para todos los exámenes.

Por defecto los tests importan `ejercicios.py` (tu código).
Para probar `solucion.py` usa:
    pytest --solucion
o la variable de entorno:
    EXAMEN_SOLUCION=1 pytest
"""
import importlib.util
import os
import sys
from pathlib import Path

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--solucion",
        action="store_true",
        default=False,
        help="Probar solucion.py en lugar de ejercicios.py",
    )


def usar_solucion(config) -> bool:
    if config.getoption("--solucion"):
        return True
    return os.environ.get("EXAMEN_SOLUCION", "").strip().lower() in ("1", "si", "sí", "true", "yes")


def _cargar(ruta: Path, clave: str):
    if clave in sys.modules:
        return sys.modules[clave]
    spec = importlib.util.spec_from_file_location(clave, ruta)
    modulo = importlib.util.module_from_spec(spec)
    sys.modules[clave] = modulo
    spec.loader.exec_module(modulo)
    return modulo


@pytest.fixture
def m(request):
    """Módulo del examen: ejercicios.py o solucion.py (carpeta padre de tests/)."""
    examen = Path(str(request.path)).resolve().parent.parent
    nombre = "solucion" if usar_solucion(request.config) else "ejercicios"
    ruta = examen / f"{nombre}.py"
    clave = f"_examen_{examen.parent.name}_{examen.name}_{nombre}".replace("-", "_")
    return _cargar(ruta, clave)
