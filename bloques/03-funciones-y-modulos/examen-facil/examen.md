# Bloque 03 · Funciones y módulos — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Con qué palabra clave se define una función?
2. ¿Qué imprime `def f(): pass` y luego `print(f())`?
3. Dada `def area(b, h=2): return b * h`, ¿qué vale `area(3)`? ¿Y `area(3, 4)`?
4. ¿Es válido `def g(a=1, b):`? ¿Por qué?
5. ¿Qué imprime?
   ```python
   x = 10
   def cambiar():
       x = 5
   cambiar()
   print(x)
   ```
6. ¿Qué hace la palabra clave `global`?
7. ¿Cómo importas solo la función `randint` del módulo `random`?
8. ¿Qué devuelve `def par(): return 1, 2` al llamar `par()`? a) `1` b) `[1, 2]` c) `(1, 2)` d) error
9. ¿Qué es un *docstring* y dónde se escribe?
10. Llamada con argumento por nombre: ¿qué vale `area(h=10, b=2)` con la función de la pregunta 3?

## Parte B — Código (5 ejercicios)

1. `area_rectangulo(base, altura=1)` → `base * altura`.
2. `estadisticas(numeros)` → devuelve **tres valores**: `(mínimo, máximo, media)` de una lista no vacía.
3. `aplicar(funcion, valor, veces=1)` → aplica `funcion` a `valor` tantas `veces` como se indique y devuelve el resultado: `aplicar(lambda x: x * 2, 3, 2) == 12`.
4. Contador global: `registrar_evento()` suma 1 a la variable global `EVENTOS` y devuelve su nuevo valor; `reiniciar_eventos()` la pone a 0.
5. `hipotenusa(a, b)` → usa el módulo `math` para devolver `√(a² + b²)`.

Corrige con: `python corregir.py 03 facil`
