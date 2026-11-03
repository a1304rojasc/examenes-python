# Bloque 02 · Control de flujo — Examen difícil

Combina el bloque 01 (tipos, conversión, f-strings, operadores) con el control de flujo.

## Parte A — Teoría (10 preguntas)

1. ¿Qué imprime?
   ```python
   for i in range(3):
       if i == 1:
           continue
       print(i, end="")
   else:
       print("!", end="")
   ```
2. ¿Y si cambiamos `continue` por `break`?
3. ¿Cuántas veces se ejecuta `while n > 0: n //= 2` si `n = 20`?
4. ¿Qué devuelve `"8080".isdigit()`? ¿Y `"-1".isdigit()`?
5. ¿Por qué `if x = 5:` es un error y `if x == 5:` no?
6. ¿Qué imprime `print("ok" if 0 else "vacío")`?
7. En `for c in "ssh":`, ¿qué tipo tiene `c` en cada vuelta?
8. ¿Qué es más eficiente para comprobar si `n` es primo: probar divisores hasta `n` o hasta `√n`? ¿Por qué?
9. ¿Cuántas líneas imprime un bucle anidado `for i in range(3): for j in range(4): print(i, j)`?
10. ¿Qué devuelve `not (True or x)` aunque `x` no esté definida? Explica el cortocircuito.

## Parte B — Código (5 ejercicios)

1. `validar_puerto(texto)` → `"inválido"` si no son solo dígitos o está fuera de 1–65535; `"reservado"` si < 1024; si no, `"válido"`. Ignora espacios alrededor.
2. `intento_exitoso(intentos, correcta, max_intentos=3)` → número de intento (1, 2, …) en que la contraseña coincide, o `0` si se agotan los `max_intentos` (bloqueo) o la lista se termina.
3. `es_primo(n)` → `True` si `n` es primo (prueba divisores hasta la raíz cuadrada).
4. `fortaleza(password)` → puntuación de 0 a 4: +1 si longitud ≥ 8, +1 si tiene mayúscula, +1 si tiene dígito, +1 si tiene un símbolo (carácter no alfanumérico).
5. `tabla_multiplicar(n, hasta)` → cadena con una línea por valor, `"n x i = r"`, de 1 a `hasta`, separadas por `"\n"` (sin salto final).

Corrige con: `python corregir.py 02 dificil`
