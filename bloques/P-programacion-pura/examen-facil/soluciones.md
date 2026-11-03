# Bloque P · Examen fácil — Soluciones (teoría)

1. Los **parámetros** son los datos de entrada que recibe la función; el **valor de retorno** (`return`) es el resultado que entrega a quien la llamó. Una función sin `return` devuelve `None`.
2. Un **acumulador** es una variable que se va actualizando en cada vuelta del bucle (una suma, una cuenta, una lista que crece). Sirve para combinar todos los elementos en un resultado, p. ej. sumar importes o contar cuántos cumplen una condición.
3. Es seguir el bucle "con papel y lápiz", anotando el valor de cada variable en cada iteración. Revela errores de lógica (condiciones mal puestas, acumuladores sin inicializar) sin depender de ejecutar.
4. Por elementos (`for x in lista`) es más legible cuando solo necesitas el valor. Por índices (`for i in range(len(lista))`) conviene cuando necesitas la posición, modificar la lista o recorrer dos listas en paralelo.
5. Un corte extrae una subsecuencia. `inicio` es la primera posición incluida, `fin` la primera **excluida** y `paso` cada cuántos elementos se toma (negativo para ir hacia atrás).
6. La lista exige un índice existente: fuera de rango lanza `IndexError`. El diccionario permite `get(clave, valor_por_defecto)`, que devuelve el valor por defecto en vez de lanzar `KeyError` cuando la clave no está.
7. **Lista de diccionarios**: muchos registros con los mismos campos (p. ej. una tabla de clientes). **Diccionario de listas**: agrupar valores bajo una clave (p. ej. las notas de cada asignatura). La primera modela "filas"; el segundo, "grupos".
8. Por filas se recorre cada sublista completa (`for fila in matriz`). Por columnas se fija una posición `j` y se recorren todas las filas tomando `fila[j]`.
9. La imagen es una cuadrícula de píxeles; cada número es la intensidad de un píxel. En escala de grises, 0 es negro, 255 es blanco y los intermedios son tonos de gris.
10. Predecir obliga a entender el código y detecta malentendidos: si la predicción falla, aprendes exactamente qué concepto no dominabas, en lugar de "probar hasta que funcione".
