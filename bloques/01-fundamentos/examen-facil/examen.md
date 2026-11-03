# Bloque 01 · Fundamentos — Examen fácil

Tiempo sugerido: 45 min. Parte A: responde en papel. Parte B: programa en `ejercicios.py`.

## Parte A — Teoría (10 preguntas)

1. ¿Qué tipo de dato es `3.0`? a) `int` b) `float` c) `str` d) `bool`
2. ¿Cuál es el resultado de `17 % 5`?
3. ¿Cuál es el resultado de `17 // 5`?
4. ¿Qué imprime `print(type("42"))`?
5. ¿Qué devuelve `int("12") + 3`? a) `"123"` b) `15` c) error d) `"15"`
6. ¿Qué imprime `nombre = "Ana"; print(f"Hola {nombre}!")`?
7. ¿Cuál de estos nombres de variable es **inválido**? a) `_ip` b) `ip_origen` c) `2ip` d) `IP`
8. ¿Qué vale `2 ** 3`?
9. ¿Qué imprime `print("a", "b", sep="-")`?
10. Verdadero o falso: `True and not False` vale `True`.

## Parte B — Código (5 ejercicios)

Implementa en `ejercicios.py`:

1. `celsius_a_fahrenheit(c)` → devuelve `c * 9/5 + 32`.
2. `saludar()` → pide el nombre con `input("Nombre: ")` e imprime `Hola, <nombre>!` (sin espacios sobrantes alrededor del nombre).
3. `es_par(n)` → `True` si `n` es par, si no `False` (usa `%`).
4. `formatear_precio(cantidad)` → cadena con 2 decimales y el símbolo euro: `formatear_precio(3.5) == "3.50 €"`.
5. `segundos_a_hms(segundos)` → cadena `"HH:MM:SS"` con ceros a la izquierda: `segundos_a_hms(3725) == "01:02:05"`.

Corrige con: `python corregir.py 01 facil`
