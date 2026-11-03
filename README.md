# Exámenes Python 0 → Ciberseguridad

Banco de exámenes del curso **"Python 0 → Ciberseguridad"**, con la estructura real de los sílabos
(ver `silabo/`): primero el **Bloque P (Programación Pura)** y luego los **Bloques 6 a 12** de ciberseguridad.
Cada bloque trae repaso espaciado, Examen Fácil y Examen Difícil, y corrección automática con `pytest`.

## Bloques

| Nº | Carpeta | Sub-temas |
|----|---------|-----------|
| P  | `P-programacion-pura` | P.1 funciones/selección · P.2 bucles · P.3 strings y listas · P.4 diccionarios · P.5 matrices · P.6 imágenes (numpy) · P.7–P.8 recursión y backtracking · P.9 Big O · P.10 búsqueda · P.11–P.12 ordenamiento |
| 6  | `06-criptografia` | 6.1 hashing · 6.2 simétrico (AES) · 6.3 asimétrico (RSA) · 6.4 curvas elípticas · 6.5 TLS · 6.6 esteganografía |
| 7  | `07-binarios` | 7.1 binario/hex y bitwise · 7.2 `struct` y endianness · 7.3 magic bytes y headers (ELF) · 7.4 PCAP |
| 8  | `08-scripting-ofensivo` | 8.1 reconocimiento · 8.2 escáneres · 8.3 fuerza bruta · 8.4 fuzzing · 8.5 scraping · 8.6 APIs |
| 9  | `09-vulnerabilidades-web` | 9.1 SQL injection · 9.2 XSS · 9.3 SSRF/redirección abierta · 9.4 parsing de HTML |
| 10 | `10-forense-y-malware` | 10.1 análisis estático (`ast`) · 10.2 binarios/entropía · 10.3 memoria/procesos · 10.4 logs · 10.5 hashing/IOC/YARA |
| 11 | `11-automatizacion-herramientas` | 11.1 CLI (`argparse`) · 11.2 logging · 11.3 testing/mocking · 11.4 packaging · 11.5 APIs de seguridad |
| 12 | `12-entornos-seguridad` | 12.1 Kali/permisos · 12.2 Metasploit · 12.3 CTF/pwntools · 12.4 SOC/SIEM |

> El sílabo completo (Bloques 0–12) y el de Programación Pura están en `silabo/`. Los Bloques 0–5 ya estaban
> cerrados antes de este banco; aquí se cubre el Bloque P (repaso/ampliación) y del 6 en adelante.

## Lecciones pendientes del Bloque 5

En [`lecciones/05-redes/`](lecciones/05-redes/) hay mini lecciones de **5.4 requests/httpx**, **5.5 Scapy** y **5.6 DNS con dnspython**: caso concreto, teoría y 3 ejercicios con tests cada una. Se corrigen con `pytest lecciones/05-redes/<tema>`.

## Formato de cada examen

- **Preguntas teóricas abiertas** (nada de opción múltiple): se responden con tus palabras.
- **Ejercicios narrativos estilo UTEC**: el enunciado plantea un problema de dominio y **no** dice qué función
  o estructura de Python usar; tú infieres la herramienta.
- Antes de ejecutar cada ejercicio, **predice** el resultado y tu confianza en %.
- Los ejercicios de ciberseguridad son **defensivos y locales**: se analizan datos de ejemplo y se hacen
  pruebas en tu propia máquina; nunca se ataca un sistema real. Criptografía con la librería
  `cryptography` y **claves generadas al vuelo, nunca reales**. Se usan IPs/dominios de documentación
  (`127.0.0.1`, `192.0.2.x`, `198.51.100.x`, `203.0.113.x`, `example.com`).

## Estructura de archivos

```
corregir.py                 ← corrector: nota sobre 5
conftest.py / pytest.ini    ← configuración de pytest (opción --solucion)
herramientas/generar_ejercicios.py  ← regenera ejercicios.py desde solucion.py
silabo/                     ← sílabos reales (referencia)
bloques/<bloque>/
├── repaso.md               ← 3-5 preguntas de repaso espaciado (mezclan sub-temas) con respuesta
├── examen-facil/
│   ├── examen.md           ← 10 preguntas teóricas abiertas + 5 ejercicios
│   ├── ejercicios.py       ← AQUÍ programas tú (funciones vacías)
│   ├── soluciones.md       ← respuestas explicadas de la teoría
│   ├── solucion.py         ← soluciones de código comentadas
│   └── tests/test_examen.py
└── examen-dificil/         ← mismo formato, más difícil y combinando conceptos
```

## Requisitos

Python 3.10+ y:

```bash
pip install pytest numpy cryptography pillow
```

> Nota: ejecuta los tests con `python -m pytest` (o con `corregir.py`), que usan tu Python con numpy y
> cryptography instalados. El comando suelto `pytest` puede correr en un entorno aislado sin esas librerías.

## Cómo hacer un examen

1. Lee `repaso.md` del bloque.
2. Abre `examen.md` y responde la **Parte A** (teoría) por tu cuenta.
3. Resuelve la **Parte B** en `ejercicios.py` (no cambies nombres ni parámetros).
4. No mires `soluciones.md` ni `solucion.py` hasta terminar.

## Cómo corregirse

```bash
python corregir.py P facil        # corrige tu ejercicios.py del Bloque P, examen fácil
python corregir.py 6 dificil      # Bloque 6, examen difícil
python corregir.py 10 facil
```

Muestra cada ejercicio (✔/✘), el primer error y la **nota de código sobre 5**
(1 punto por ejercicio con todos sus tests en verde). La teoría se corrige con `soluciones.md`.

## Correr todo con las soluciones oficiales

```bash
python -m pytest --solucion        # todos los tests contra solucion.py
EXAMEN_SOLUCION=1 python -m pytest  # equivalente con variable de entorno
python corregir.py todo --solucion  # tabla con la nota de cada examen
```

Todos deben pasar (GitHub Actions lo comprueba en cada push: `.github/workflows/soluciones.yml`).
Si editas un `solucion.py`, regenera la plantilla del alumno con
`python herramientas/generar_ejercicios.py bloques/<bloque>/examen-facil`.

## Ética

Material educativo. Todas las técnicas ofensivas se estudian con enfoque **defensivo** (detectar, validar,
analizar, corregir) sobre **datos de ejemplo y laboratorios propios**. No uses estas herramientas contra
sistemas de terceros sin autorización por escrito.
