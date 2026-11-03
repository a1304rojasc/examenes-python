# Bloque 01 · Fundamentos — Repaso

**1. ¿Qué tipo devuelve siempre `input()`?**
Siempre `str`. Para operar con números hay que convertir: `int(input())` o `float(input())`.

**2. ¿Diferencia entre `/`, `//` y `%`?**
`/` es división real (`7 / 2 == 3.5`), `//` es división entera hacia abajo (`7 // 2 == 3`) y `%` es el resto (`7 % 2 == 1`).

**3. ¿Qué imprime `print(f"{3.14159:.2f}")`?**
`3.14`. El especificador `:.2f` formatea con 2 decimales.

**4. ¿Por qué `"5" + 5` da error y `"5" * 3` no?**
`+` entre `str` e `int` no está definido (`TypeError`). `str * int` repite la cadena: `"555"`.

**5. ¿Qué valen `bool("")`, `bool("0")` y `bool(0)`?**
`False`, `True`, `False`. Solo la cadena vacía es falsa; `"0"` es una cadena con un carácter.
