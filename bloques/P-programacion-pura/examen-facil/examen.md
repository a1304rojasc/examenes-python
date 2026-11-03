# Bloque P · Programación Pura — Examen fácil

Tiempo sugerido: 60 min. Parte A: responde con tus palabras (preguntas abiertas). Parte B: programa en `ejercicios.py`.
Para cada ejercicio de la Parte B, **predice** qué devolverá tu función con un ejemplo y tu confianza en % antes de ejecutar los tests.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica la diferencia entre los parámetros de una función y su valor de retorno. ¿Qué devuelve una función que no ejecuta ningún `return`?
2. ¿Qué es un acumulador dentro de un bucle y para qué sirve? Describe un caso en el que lo necesitarías.
3. ¿En qué consiste "trazar a mano" un bucle y por qué ayuda a encontrar errores antes de ejecutar?
4. ¿Qué diferencia hay entre recorrer una lista por sus elementos y recorrerla por sus índices? ¿Cuándo conviene cada forma?
5. Describe qué es un corte (slicing) de una secuencia y qué significan los tres números en `inicio:fin:paso`.
6. Acceder a una posición inexistente de una lista detiene el programa con un error, pero consultar una clave ausente de un diccionario puede no hacerlo. Explica por qué y cómo se consulta "sin riesgo".
7. Explica la diferencia entre una lista de diccionarios y un diccionario de listas, con un ejemplo de cuándo usarías cada una.
8. En una matriz representada como lista de listas, ¿cómo se diferencia "recorrer por filas" de "recorrer por columnas"?
9. ¿Qué significa que una imagen se represente como una matriz numérica? ¿Qué representa cada número en una imagen en escala de grises?
10. ¿Por qué conviene predecir qué imprimirá o devolverá un fragmento de código antes de ejecutarlo?

## Parte B — Ejercicios (5 problemas)

Implementa las funciones en `ejercicios.py`. Decide tú qué herramientas de Python usar.

1. Una tienda registra el importe de cada venta del día en una lista. La gerencia quiere saber **cuántas** ventas superaron el promedio del día. Escribe `ventas_sobre_promedio(ventas)` que devuelva ese número (0 si no hubo ventas).

2. Una estación meteorológica vuelca las temperaturas de un día en una sola línea de texto, separadas por comas (por ejemplo `"12.5,8,20,15"`). Escribe `temperatura_extremos(linea)` que devuelva la pareja `(mínima, máxima)` como números.

3. El inventario de un almacén es una lista en la que cada artículo es un registro con su `producto` (texto) y su `cantidad` (entero). Escribe `producto_menor_stock(inventario)` que devuelva el nombre del producto con menos unidades. Si hay empate, el primero que aparezca.

4. Las notas de un curso están en una tabla: cada fila contiene las calificaciones de un estudiante. Escribe `promedio_por_estudiante(notas)` que devuelva la lista de promedios, uno por estudiante, en el mismo orden.

5. Una cámara entrega fotogramas en escala de grises como una matriz de numpy de enteros (0–255). Para compararlos con su reflejo necesitas la imagen volteada de izquierda a derecha (espejo). Escribe `espejo_horizontal(imagen)` que devuelva la imagen reflejada horizontalmente.

Corrige con: `python corregir.py P facil`
