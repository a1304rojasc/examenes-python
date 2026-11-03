# Bloque 02 · Control de flujo — Repaso

**1. ¿Qué diferencia hay entre `if/elif/else` y varios `if` seguidos?**
Con `elif` solo se ejecuta la **primera** rama verdadera; con varios `if` se evalúan todos de forma independiente.

**2. ¿Cuándo usar `for` y cuándo `while`?**
`for` para recorrer una secuencia o un rango conocido; `while` cuando repites *mientras* se cumpla una condición (p. ej. hasta que el usuario acierte).

**3. ¿Qué hacen `break` y `continue`?**
`break` sale del bucle por completo; `continue` salta al siguiente ciclo sin ejecutar el resto del cuerpo.

**4. ¿Qué valores recorre `range(2, 10, 3)`?**
`2, 5, 8`. Empieza en 2, termina antes de 10, paso 3.

**5. ¿Para qué sirve el `else` de un bucle?**
Se ejecuta si el bucle terminó **sin** `break`. Útil para "busqué y no encontré".
