# Bloque 02 · Control de flujo — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Cuántas veces se ejecuta el cuerpo de `for i in range(5):`?
2. ¿Qué imprime `for i in range(1, 4): print(i, end=" ")`?
3. ¿Qué palabra clave sale de un bucle inmediatamente? a) `continue` b) `pass` c) `break` d) `return`
4. ¿Qué imprime este código?
   ```python
   x = 7
   if x > 10: print("A")
   elif x > 5: print("B")
   else: print("C")
   ```
5. ¿Qué peligro tiene `while True:` sin `break`?
6. ¿Qué valores produce `range(10, 0, -3)`?
7. ¿Qué hace `continue`?
8. ¿Qué imprime `print(3 < 5 < 4)`?
9. Verdadero o falso: un `if` siempre necesita un `else`.
10. ¿Para qué sirve la instrucción `pass`?

## Parte B — Código (5 ejercicios)

1. `clasificar_nota(nota)` → `"suspenso"` (< 5), `"aprobado"` (< 7), `"notable"` (< 9) o `"sobresaliente"`.
2. `suma_hasta(n)` → suma de 1 a `n` usando un bucle (0 si `n` < 1).
3. `contar_vocales(texto)` → cuántas vocales (`aeiou`, mayúsculas o minúsculas) tiene el texto.
4. `primer_negativo(numeros)` → índice del primer número negativo o `-1` si no hay. Usa `break`.
5. `suma_sin_multiplos_de_3(n)` → suma de 1 a `n` saltándose los múltiplos de 3. Usa `continue`.

Corrige con: `python corregir.py 02 facil`
