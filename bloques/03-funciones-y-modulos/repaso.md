# Bloque 03 · Funciones y módulos — Repaso

**1. ¿Qué devuelve una función que no tiene `return`?**
`None`.

**2. ¿Qué diferencia hay entre un parámetro posicional y uno con valor por defecto?**
El posicional es obligatorio; el que tiene valor por defecto (`def f(x, y=1)`) puede omitirse. Los parámetros con defecto van siempre después de los obligatorios.

**3. ¿Qué es el alcance (scope) de una variable?**
Dónde es visible. Una variable creada dentro de una función es **local** y desaparece al terminar. Para modificar una global hay que declararla con `global` (mejor evitarlo y pasar/devolver valores).

**4. ¿Diferencia entre `import math` y `from math import sqrt`?**
El primero importa el módulo y se usa `math.sqrt(...)`; el segundo trae solo el nombre `sqrt` al espacio actual.

**5. ¿Para qué sirve `if __name__ == "__main__":`?**
Para que ese código solo se ejecute al lanzar el archivo directamente, no al importarlo desde otro módulo.
