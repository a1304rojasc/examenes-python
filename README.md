# Exámenes Python 0 → Ciberseguridad

Banco de exámenes del curso **"Python 0 → Ciberseguridad"**: 10 bloques, cada uno con repaso,
examen fácil y examen difícil, y corrección automática con `pytest`.

## Bloques (editables)

> Esta lista es provisional: puedes renombrar, reordenar o cambiar temas. Cada bloque es una
> carpeta independiente en `bloques/`.

| Nº | Carpeta | Temas |
|----|---------|-------|
| 01 | `01-fundamentos` | variables, tipos, operadores, `input`/`print`, f-strings |
| 02 | `02-control-de-flujo` | `if`, bucles, `break`/`continue` |
| 03 | `03-funciones-y-modulos` | parámetros, retorno, alcance, `import` |
| 04 | `04-estructuras-de-datos` | listas, tuplas, diccionarios, conjuntos, comprensiones |
| 05 | `05-archivos-y-excepciones` | leer/escribir, `with`, `try/except`, rutas |
| 06 | `06-texto-y-regex` | expresiones regulares, parsear logs estilo `auth.log` de SSH |
| 07 | `07-redes` | IPs, puertos, CIDR (`ipaddress`), sockets básicos, HTTP |
| 08 | `08-criptografia-basica` | base64, `hashlib`, César/Vigenère, por qué no inventar cripto |
| 09 | `09-seguridad-web` | validación de entrada, inyección SQL, consultas parametrizadas (`sqlite3`) |
| 10 | `10-automatizacion-defensiva` | fuerza bruta con ventana de tiempo, CLI con `argparse`, tests con `pytest` |

## Estructura

```
corregir.py                 ← corrector: nota sobre 5
conftest.py / pytest.ini    ← configuración de pytest (opción --solucion)
herramientas/generar_ejercicios.py  ← regenera ejercicios.py desde solucion.py
bloques/NN-nombre/
├── repaso.md               ← 3-5 preguntas de repaso con respuesta
├── examen-facil/
│   ├── examen.md           ← 10 preguntas teóricas + 5 ejercicios de código
│   ├── ejercicios.py       ← AQUÍ escribes tu código (funciones vacías)
│   ├── soluciones.md       ← respuestas explicadas de la parte teórica
│   ├── solucion.py         ← soluciones de código comentadas
│   └── tests/test_examen.py
└── examen-dificil/         ← mismo formato; combina bloques anteriores
```

## Cómo hacer un examen

1. Lee `repaso.md` del bloque.
2. Abre `examen.md` y responde la **Parte A** (teoría) en un papel o archivo aparte.
3. Resuelve la **Parte B** en `ejercicios.py` (no cambies nombres ni parámetros).
4. Sin mirar `soluciones.md` ni `solucion.py` hasta terminar 😉

## Cómo corregirse

Requisito: Python 3.10+ y `pip install pytest`.

```bash
python corregir.py 03 facil      # corrige tu ejercicios.py del bloque 03, examen fácil
python corregir.py 03 dificil
```

Muestra cada ejercicio (✔/✘), el primer error y la **nota de código sobre 5**
(1 punto por ejercicio con todos sus tests en verde). La teoría se corrige con `soluciones.md`.

También puedes usar pytest directamente:

```bash
pytest bloques/03-funciones-y-modulos/examen-facil -v
```

## Correr todo con las soluciones oficiales

```bash
pytest --solucion                 # todos los tests contra solucion.py
EXAMEN_SOLUCION=1 pytest          # equivalente con variable de entorno
python corregir.py todo --solucion   # tabla con la nota de cada examen
```

Todos deben pasar. Si editas un `solucion.py`, regenera la plantilla del alumno con
`python herramientas/generar_ejercicios.py bloques/NN-nombre/examen-facil`.

## Ética

Todos los ejercicios de ciberseguridad son **defensivos y locales**: no se ataca ningún sistema
real. Se usan solo datos ficticios e IPs/dominios de documentación
(`192.0.2.x`, `198.51.100.x`, `203.0.113.x`, `example.com`).
