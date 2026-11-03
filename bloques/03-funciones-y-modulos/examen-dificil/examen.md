# Bloque 03 · Funciones y módulos — Examen difícil

Combina bloques 01–02 (tipos, f-strings, bucles, condicionales) con funciones y módulos.

## Parte A — Teoría (10 preguntas)

1. ¿Qué imprime?
   ```python
   def f(lista=[]):
       lista.append(1)
       return lista
   f(); print(f())
   ```
   ¿Por qué es un error clásico y cómo se evita?
2. ¿Qué reciben `*args` y `**kwargs` dentro de la función (qué tipos)?
3. ¿Qué es una *closure*? Pon un ejemplo de una línea.
4. ¿Qué imprime `print((lambda a, b=2: a * b)(5))`?
5. ¿Qué es la recursión y qué necesita siempre para no ser infinita?
6. ¿Por qué para generar un token de sesión se usa `secrets` y no `random`?
7. ¿Qué pasa si un módulo propio se llama `random.py` y en otro archivo haces `import random`?
8. ¿Qué imprime?
   ```python
   def externa():
       x = 1
       def interna():
           nonlocal x
           x += 1
       interna(); return x
   print(externa())
   ```
9. ¿Qué diferencia hay entre `return` y `print` dentro de una función?
10. ¿Qué hace `pow(3, 4, 5)` y por qué es útil en criptografía?

## Parte B — Código (5 ejercicios)

1. `crear_validador(minimo, maximo)` → devuelve una **función** que recibe un número y devuelve `True` si está en `[minimo, maximo]`.
2. `construir_url(host, ruta="/", **params)` → `"https://host/ruta"` y, si hay parámetros, `"?k1=v1&k2=v2"` en el orden recibido. `construir_url("example.com", "/buscar", q="ssh", p=2) == "https://example.com/buscar?q=ssh&p=2"`.
3. `reintentar(funcion, max_intentos)` → llama a `funcion()` hasta que devuelva `True`; devuelve el nº de llamadas realizadas o `-1` si nunca lo logra.
4. `potencia_mod(base, exp, mod)` → `base**exp % mod` **recursivo** por exponenciación rápida (si `exp` es par, `(b^(e/2))²`). No uses `pow` ni `**` con el exponente completo.
5. `generar_pin(longitud, semilla)` → PIN de dígitos usando `random.Random(semilla)` (misma semilla ⇒ mismo PIN). Es un ejercicio **reproducible**; en producción se usaría `secrets`.

Corrige con: `python corregir.py 03 dificil`
