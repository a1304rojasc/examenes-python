# Bloque P · Programación Pura — Repaso espaciado

> 3–5 preguntas que mezclan sub-temas. Responde de memoria (blurting) antes de mirar.

**1. (P.2 + P.4) Recorres una lista de registros de ventas, cada uno con su `monto`, para acumular el total por vendedor en un diccionario. ¿Qué papel cumple el diccionario como acumulador y por qué `get(clave, 0)` evita un error la primera vez que aparece un vendedor?**
El diccionario guarda un subtotal por clave; se va sumando en cada vuelta. `get(clave, 0)` devuelve 0 cuando la clave aún no existe, así la primera suma parte de 0 en lugar de lanzar `KeyError`.

**2. (P.3 + P.5) ¿Qué diferencia hay entre `fila[1:3]` sobre una fila de una matriz y recorrer una columna completa? ¿Por qué la columna no se obtiene con un corte simple?**
`fila[1:3]` toma elementos contiguos de **una** fila (misma sublista). Una columna atraviesa **todas** las filas en la misma posición `j`, así que hay que recorrer fila por fila (`[fila[j] for fila in matriz]`); no son contiguos en memoria como para un corte directo.

**3. (P.7 + P.9) Una función recursiva calcula el tamaño de carpetas anidadas. ¿Cuál es su caso base y por qué su coste crece con el número total de archivos, no con la profundidad?**
Caso base: una entrada que es un archivo (un número) se suma directamente; no genera más llamadas. Visita cada archivo y cada carpeta exactamente una vez, por eso el coste es O(nº de entradas), independientemente de cuán anidadas estén.

**4. (P.10 + P.11) Tienes una lista ordenada y buscas un valor. ¿Por qué la búsqueda binaria es mucho mejor que recorrerla entera, y qué pasaría si la lista no estuviera ordenada?**
La binaria descarta la mitad en cada paso → O(log n) frente a O(n) de la lineal. Si la lista no está ordenada, la binaria da resultados incorrectos: su lógica depende de que lo descartado no pueda contener el objetivo.

**5. (P.6 + P.9) Una imagen es una matriz de numpy. Obtener su negativo es `255 - imagen`. ¿Por qué esta operación es O(n) sobre el número de píxeles y por qué numpy la hace sin un bucle explícito en Python?**
Toca cada píxel una vez (O(nº de píxeles)). numpy aplica la resta de forma vectorizada en código compilado, evitando el bucle `for` de Python, que sería mucho más lento.
