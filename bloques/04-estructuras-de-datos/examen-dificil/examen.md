# Bloque 04 · Estructuras de datos — Examen difícil

Combina bloques 01–03 (bucles, funciones, `key=`/lambdas) con estructuras de datos. Datos ficticios de un servidor.

## Parte A — Teoría (10 preguntas)

1. ¿Qué imprime?
   ```python
   a = [1, 2]; b = a; b += [3]
   print(a)
   ```
2. ¿Por qué `{[1, 2]: "x"}` da error y `{(1, 2): "x"}` no?
3. ¿Qué devuelve `sorted([("b", 2), ("a", 2), ("c", 5)], key=lambda t: (-t[1], t[0]))`?
4. ¿Qué diferencia hay entre `lista.sort()` y `sorted(lista)`?
5. ¿Qué devuelve `{x % 3 for x in range(10)}`?
6. ¿Qué es `collections.Counter` y qué devuelve `Counter("aab").most_common(1)`?
7. ¿Qué hace `d.setdefault("k", []).append(1)` si `"k"` no existe?
8. ¿Qué devuelve `[[0] * 2] * 2` y qué problema tiene si luego haces `m[0][0] = 9`?
9. ¿Qué es el *desempaquetado*? ¿Qué valen `a, *b = [1, 2, 3]`?
10. Para comprobar si una IP está en una lista negra de 1 millón de IPs, ¿`list` o `set`? ¿Por qué?

## Parte B — Código (5 ejercicios)

1. `top_ips(ips, n)` → lista de tuplas `(ip, veces)` con las `n` IPs más frecuentes, ordenadas por veces (desc) y, a igualdad, por IP (asc, como texto).
2. `agrupar_por_puerto(conexiones)` → recibe tuplas `(ip, puerto)` y devuelve `{puerto: [ips únicas ordenadas]}`.
3. `admins_sin_mfa(usuarios)` → recibe dicts `{"nombre", "admin", "mfa"}` y devuelve, ordenados, los nombres de administradores **sin** MFA (usa una comprensión).
4. `diff_reglas(antes, despues)` → `{"añadidas": [...], "eliminadas": [...]}` (listas ordenadas) comparando dos listas de reglas de firewall.
5. `valores_sobre_umbral(matriz, umbral)` → con una comprensión anidada, aplana la matriz (lista de listas) y deja solo los valores `> umbral`.

Corrige con: `python corregir.py 04 dificil`
