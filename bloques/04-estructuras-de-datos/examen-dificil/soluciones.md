# Bloque 04 · Examen difícil — Soluciones (teoría)

1. **`[1, 2, 3]`**. `b` y `a` son la misma lista y `+=` la modifica *in situ*.
2. Las claves deben ser **hashables** (inmutables); la lista es mutable, la tupla no.
3. **`[("c", 5), ("a", 2), ("b", 2)]`**. Primero por número descendente (`-t[1]`), luego por letra.
4. `sort()` ordena **la propia lista** y devuelve `None`; `sorted()` devuelve **una lista nueva**.
5. **`{0, 1, 2}`**. Comprensión de conjunto: se quedan los restos distintos.
6. Un diccionario especializado en contar. **`[("a", 2)]`**.
7. Crea `d["k"] = []` y añade 1 → `{"k": [1]}`.
8. **`[[0, 0], [0, 0]]`**, pero ambas filas son **la misma lista**: tras `m[0][0] = 9` queda `[[9, 0], [9, 0]]`. Usa `[[0] * 2 for _ in range(2)]`.
9. Asignar varios nombres desde una secuencia: `a = 1`, `b = [2, 3]`.
10. **`set`**: la búsqueda es O(1) de media (tabla hash), frente a O(n) en la lista.
