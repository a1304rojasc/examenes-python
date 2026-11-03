# Bloque 04 · Estructuras de datos — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Qué vale `[1, 2, 3][-1]`?
2. ¿Qué método añade un elemento al final de una lista?
3. ¿Cuál de estas estructuras es inmutable? a) `list` b) `dict` c) `tuple` d) `set`
4. ¿Qué devuelve `len({1, 1, 2, 3, 3})`?
5. ¿Qué imprime `d = {"ssh": 22}; print(d.get("http", 80))`?
6. ¿Qué devuelve `[x * x for x in range(4)]`?
7. ¿Qué hace `{1, 2, 3} & {2, 3, 4}`?
8. ¿Cómo recorres a la vez clave y valor de un diccionario `d`?
9. ¿Qué devuelve `sorted([3, 1, 2], reverse=True)`?
10. ¿Qué vale `"a,b,c".split(",")`?

## Parte B — Código (5 ejercicios)

1. `eliminar_duplicados(lista)` → nueva lista sin repetidos **conservando el orden** de primera aparición.
2. `contar_frecuencias(palabras)` → diccionario `{palabra: veces}`.
3. `puertos_comunes(a, b)` → lista **ordenada** de los puertos presentes en ambas listas (usa conjuntos).
4. `cuadrados_pares(n)` → con una comprensión, lista de los cuadrados de los números pares de `0` a `n` (incluido).
5. `invertir_diccionario(d)` → diccionario con claves y valores intercambiados: `{"ssh": 22}` → `{22: "ssh"}`.

Corrige con: `python corregir.py 04 facil`
