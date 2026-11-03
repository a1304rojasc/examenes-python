# Bloque P · Programación Pura — Examen difícil

Mismo formato que el fácil, pero los problemas combinan sub-temas (recursión, backtracking, eficiencia, búsqueda y ordenamiento).
**Predice** el resultado y tu confianza en % antes de ejecutar cada ejercicio.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica con tus palabras qué mide la complejidad algorítmica (Big O) y por qué se ignoran las constantes y los términos de menor orden.
2. ¿Por qué la búsqueda binaria es O(log n)? ¿Qué condición deben cumplir los datos para poder aplicarla?
3. Compara selection sort, insertion sort y bubble sort: ¿en qué coinciden en eficiencia en el peor caso y en qué se diferencia su comportamiento?
4. Explica de dónde sale el factor `log n` que hace a merge sort O(n log n) frente al O(n²) de bubble sort.
5. ¿Qué es el caso base de una recursión y qué ocurre si falta o nunca se alcanza?
6. Explica qué es el backtracking y por qué necesita "deshacer" decisiones. Da un ejemplo de problema que lo requiera.
7. ¿Por qué una solución recursiva puede ser más clara pero consumir más memoria que una iterativa equivalente?
8. Una imagen es una matriz de numpy. Explica qué operación produce su "negativo" y por qué recortar una región es, en el fondo, seleccionar un rango de filas y de columnas.
9. Deduce la fórmula del número de parejas distintas que se forman con `n` elementos y explica por qué compararlas todas es O(n²).
10. Si el mismo error lógico aparece dos veces, ¿qué conviene hacer antes de seguir y por qué repasar el concepto es mejor que parchear el síntoma?

## Parte B — Ejercicios (5 problemas)

1. El disco de un equipo se describe como carpetas anidadas: cada carpeta es un registro donde cada entrada es, o bien el tamaño en bytes de un archivo (un número), o bien otra carpeta (otro registro igual). Escribe `tamano_total(carpeta)` que devuelva la suma de bytes de todo lo que contiene, a cualquier profundidad.

2. Un cajero debe entregar un **monto exacto** combinando las denominaciones disponibles (puede usar cada denominación tantas veces como haga falta). Escribe `cambio_exacto(monto, denominaciones)` que devuelva una lista de valores que sumen exactamente el monto, o `None` si con esas denominaciones es imposible. (`monto` 0 → lista vacía.)

3. Una campaña antifraude compara cada pareja de clientes una sola vez para detectar cuentas duplicadas. Antes de lanzarla, el equipo quiere estimar el trabajo. Escribe `comparaciones_todos_los_pares(n)` que devuelva cuántas comparaciones se harán con `n` clientes.

4. El padrón de socios está ordenado de menor a mayor por número de carné y puede tener carnés repetidos (por renovaciones). Escribe `primera_aparicion(ordenada, objetivo)` que devuelva la posición de la **primera** vez que aparece `objetivo`, o `-1` si no está. Debe aprovechar que la lista ya está ordenada para no recorrerla entera.

5. Dos rankings parciales de una competición ya vienen ordenados de menor a mayor tiempo. Escribe `fusionar_ordenadas(a, b)` que los combine en un único ranking ordenado, sin reordenar desde cero (aprovecha que cada lista ya está ordenada).

Corrige con: `python corregir.py P dificil`
