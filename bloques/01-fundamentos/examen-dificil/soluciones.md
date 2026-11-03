# Bloque 01 · Examen difícil — Soluciones (teoría)

1. **`11`**. Orden: `4 ** 2 = 16`; `3 * 16 = 48`; `48 // 5 = 9`; `2 + 9 = 11`. `**` > `*`,`//` (izq. a der.) > `+`.
2. **`-4` y `1`**. `//` redondea hacia −∞ (−3.5 → −4) y se cumple `(-7//2)*2 + (-7%2) == -7`.
3. **`False`**. Los `float` usan binario y `0.1` no es representable exactamente; compara con `math.isclose`.
4. **b) `   ssh|`**. `>6` alinea a la derecha en un ancho de 6.
5. **c) `ValueError`**. `int()` no acepta una cadena con punto; habría que hacer `int(float("3.7"))` → `3`.
6. **`21`**. `5 + 2 = 7`; `7 * 3 = 21`.
7. **`"ababc"`**. `*` tiene más precedencia que `+`.
8. **`11111111`**. `b` = binario, `08` = 8 cifras rellenas con ceros (aquí ya son 8 unos).
9. **`"ol"`** y **`"a"`**. El slicing `[1:3]` toma los índices 1 y 2; `-1` es el último.
10. **`"admin"`**. `or` devuelve el primer valor *verdadero*; `0` y `""` son falsos.

Las soluciones de código están en `solucion.py`.
