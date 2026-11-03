# Bloque 05 · Examen fácil — Soluciones (teoría)

1. **c) `"w"`**. (`"x"` falla si ya existe; `"a"` añade al final).
2. **`ValueError`**.
3. **`FileNotFoundError`** (subclase de `OSError`).
4. `read()` devuelve **una cadena** con todo el contenido; `readlines()` una **lista de líneas** (con su `"\n"`).
5. Se ejecuta **siempre**, haya o no excepción; sirve para liberar recursos.
6. Captura **todo** (incluso `KeyboardInterrupt` y errores de programación) y oculta fallos reales.
7. **Lanza** una excepción `ValueError` con ese mensaje; interrumpe la función si nadie la captura.
8. **`".TXT"`** (conserva mayúsculas e incluye el punto).
9. Porque la codificación por defecto depende del sistema operativo; con UTF-8 explícito tildes y `ñ` se leen igual en todas partes.
10. **`A`** y **`C`**. Hubo excepción, así que no se ejecuta `else`; `finally` siempre.
