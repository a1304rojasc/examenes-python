# Bloque 05 · Archivos y excepciones — Repaso

**1. ¿Por qué usar `with open(...) as f:`?**
Porque cierra el archivo automáticamente al salir del bloque, incluso si ocurre una excepción.

**2. ¿Qué significan los modos `"r"`, `"w"` y `"a"`?**
Leer; escribir (crea o **sobrescribe**); añadir al final (crea si no existe).

**3. ¿Cómo capturo solo el error de "archivo no encontrado"?**
`except FileNotFoundError:`. Captura excepciones concretas, nunca un `except:` vacío que oculte errores.

**4. ¿Para qué sirven `else` y `finally` en un `try`?**
`else` se ejecuta si **no** hubo excepción; `finally` se ejecuta **siempre** (limpieza).

**5. ¿Qué ventaja tiene `pathlib.Path` sobre concatenar cadenas?**
Une rutas de forma portable (`base / "logs" / "a.txt"`), y trae métodos útiles: `.exists()`, `.suffix`, `.read_text()`, `.glob()`…
