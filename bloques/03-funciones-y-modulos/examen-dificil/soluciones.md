# Bloque 03 · Examen difícil — Soluciones (teoría)

1. **`[1, 1]`**. El valor por defecto se crea **una sola vez** al definir la función y se comparte entre llamadas. Solución: `def f(lista=None): if lista is None: lista = []`.
2. `*args` es una **tupla** con los posicionales extra; `**kwargs` un **diccionario** con los argumentos por nombre extra.
3. Una función interna que **recuerda** variables del ámbito donde se creó: `def sumador(n): return lambda x: x + n`.
4. **`10`**. `b` toma el defecto 2.
5. Una función que se llama a sí misma; necesita un **caso base** que no recurra.
6. `random` es un generador **predecible** (pseudoaleatorio, reproducible con la semilla); `secrets` usa la fuente criptográfica del sistema operativo.
7. Se importa **tu** archivo (el directorio actual va primero en `sys.path`), "sombreando" el módulo estándar.
8. **`2`**. `nonlocal` permite modificar la `x` de `externa`.
9. `return` **devuelve** un valor al que llama (se puede usar después); `print` solo lo muestra por pantalla y la función devuelve `None`.
10. Calcula **3⁴ mod 5 = 1** de forma eficiente sin construir el número enorme; RSA y Diffie-Hellman usan exponenciación modular.
