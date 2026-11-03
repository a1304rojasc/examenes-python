# Bloque 01 · Fundamentos — Examen difícil

Tiempo sugerido: 60 min. Mismo formato que el fácil, con trampas de tipos, precedencia y formato.

## Parte A — Teoría (10 preguntas)

1. ¿Qué vale `2 + 3 * 4 ** 2 // 5`? (aplica la precedencia de operadores)
2. ¿Qué vale `-7 // 2`? ¿Y `-7 % 2`?
3. ¿Qué imprime `print(0.1 + 0.2 == 0.3)` y por qué?
4. ¿Qué imprime `print(f"{'ssh':>6}|")`? a) `ssh   |` b) `   ssh|` c) `ssh|` d) error
5. ¿Qué devuelve `int("3.7")`? a) `3` b) `4` c) `ValueError` d) `3.7`
6. ¿Qué imprime `x = 5; x += 2; x *= 3; print(x)`?
7. ¿Qué vale `"ab" * 2 + "c"`?
8. ¿Qué imprime `print(f"{255:08b}")`?
9. ¿Qué devuelve `"Hola"[1:3]`? ¿Y `"Hola"[-1]`?
10. ¿Qué valor tiene `0 or "" or "admin"`? ¿Por qué?

## Parte B — Código (5 ejercicios)

1. `leer_entero(texto)` → convierte una entrada del usuario (con espacios alrededor) a `int`: `" 42\n"` → `42`. Si viene con decimales (`"3.9"`) debe truncar a `3`.
2. `dividir_cuenta(total, personas, propina_pct)` → importe por persona tras añadir la propina en %, redondeado a 2 decimales: `dividir_cuenta(100, 4, 10) == 27.5`.
3. `fila_puerto(servicio, puerto)` → cadena con el servicio alineado a la izquierda en 8 caracteres, `|`, y el puerto alineado a la derecha en 5: `fila_puerto("ssh", 22) == "ssh     |   22"`.
4. `hosts_por_prefijo(prefijo)` → número de hosts usables en una red IPv4 `/prefijo`: `2 ** (32 - prefijo) - 2` (para prefijos de 1 a 30). `hosts_por_prefijo(24) == 254`.
5. `enmascarar(secreto)` → muestra solo el primer y el último carácter, el resto con `*` (longitud ≥ 3): `enmascarar("password") == "p******d"`. Usa slicing y repetición de cadenas.

Corrige con: `python corregir.py 01 dificil`
