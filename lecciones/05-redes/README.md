# Bloque 5 · Lecciones pendientes

Mini lecciones de los temas del Bloque 5 que quedaron sin estudiar. Cada una sigue el mismo orden: **un caso concreto primero, la teoría después** y **3 ejercicios estilo UTEC** (el enunciado cuenta un problema y no nombra la herramienta), con soluciones explicadas y tests.

| Tema | Carpeta | Los tests usan |
|---|---|---|
| 5.4 requests y httpx | `5.4-clientes-http/` | un servidor HTTP en `127.0.0.1` que levantan los propios tests |
| 5.5 Scapy (fundamentos) | `5.5-paquetes-scapy/` | paquetes en memoria y archivos `.pcap` temporales (sin root ni red) |
| 5.6 DNS con dnspython | `5.6-dns/` | `localhost`, mensajes DNS en memoria y archivos de zona de texto |

Ningún test sale a internet. Las prácticas opcionales de las lecciones solo usan `127.0.0.1` o servicios públicos de prueba (`httpbin.org`, `example.com`).

En cada carpeta:

- `leccion.md`: el caso, la teoría y los enunciados.
- `ejercicios.py`: tu código.
- `solucion.py` y `soluciones.md`: la solución oficial y por qué.
- `tests/`: la corrección automática.

```bash
pip install requests httpx scapy dnspython pytest
pytest lecciones/05-redes/5.4-clientes-http              # corrige tu código
pytest lecciones/05-redes --solucion                     # comprueba las soluciones oficiales
```
