# Bloque 05 · Archivos y excepciones — Examen difícil

Combina bloques 01–04 (bucles, funciones, listas, diccionarios, conjuntos) con archivos y excepciones.

## Parte A — Teoría (10 preguntas)

1. ¿Qué imprime?
   ```python
   def f():
       try:
           return "try"
       finally:
           print("finally")
   print(f())
   ```
2. ¿En qué orden deben ir `except ValueError` y `except Exception` y por qué?
3. ¿Qué hace `raise` sin argumentos dentro de un `except`?
4. ¿Qué es `except (ValueError, TypeError) as e:` y qué contiene `e`?
5. ¿Cómo defines tu propia excepción `PuertoInvalido`?
6. ¿Qué es un ataque de *path traversal* (`../../etc/passwd`) y cómo se previene al unir rutas?
7. ¿Qué hace `Path.resolve()`?
8. ¿Diferencia entre `Path.glob("*.log")` y `Path.rglob("*.log")`?
9. ¿Qué es mejor: comprobar `if ruta.exists()` antes de abrir o capturar `FileNotFoundError`? (pista: condición de carrera TOCTOU)
10. ¿Qué pasa al abrir en modo `"w"` un log que otro proceso está escribiendo? ¿Qué modo usarías para añadir entradas?

## Parte B — Código (5 ejercicios)

1. `convertir_enteros(valores, defecto=0)` → lista de enteros; cada valor no convertible (`ValueError` o `TypeError`) se sustituye por `defecto`.
2. `registrar(ruta, nivel, mensaje)` → si `nivel` no es `"INFO"`, `"WARN"` o `"ERROR"` lanza `ValueError`; si no, **añade** la línea `"NIVEL: mensaje"` al archivo y devuelve el número total de líneas que tiene ahora.
3. `buscar_archivos(directorio, ext)` → lista ordenada de rutas **relativas** al directorio (como texto con `/`) de todos los archivos con esa extensión, en cualquier subcarpeta.
4. `copiar_filtrando(origen, destino, palabra)` → copia a `destino` solo las líneas de `origen` que contienen `palabra` (sin distinguir mayúsculas) y devuelve cuántas copió. Si `origen` no existe, deja que salte `FileNotFoundError` **sin crear** `destino`.
5. `ruta_segura(base, nombre)` → devuelve la ruta absoluta de `base/nombre`; si el resultado queda **fuera** de `base` (p. ej. `"../secreto"`), lanza `ValueError`.

Corrige con: `python corregir.py 05 dificil`
