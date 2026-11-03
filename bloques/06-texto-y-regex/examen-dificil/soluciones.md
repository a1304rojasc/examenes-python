# Bloque 06 · Examen difícil — Soluciones (teoría)

1. El codicioso toma **lo máximo** posible (`<a><b>` entero); el perezoso **lo mínimo** (`<a>` y luego `<b>`).
2. **`[("1", "2"), ("3", "4")]`**. Con varios grupos, `findall` devuelve tuplas.
3. Agrupa **sin capturar**: no aparece en `group(n)` ni en `findall`.
4. Porque `\d{1,3}` solo mira la cantidad de dígitos, no el valor. Valida después convirtiendo cada octeto a `int` (≤ 255) o usa `ipaddress.ip_address`.
5. **`"2.1"`**. `\1` y `\2` son referencias a los grupos capturados.
6. El patrón se **compila una vez** y se reutiliza (además el código queda más legible).
7. *Regular expression Denial of Service*: patrones con cuantificadores anidados provocan **retroceso exponencial** ante entradas maliciosas, bloqueando la CPU.
8. **`{"u": "ana", "d": "example.com"}`**.
9. Coinciden con el inicio y el final de **cada línea**, no solo de todo el texto.
10. Son **datos personales/sensibles** (privacidad, RGPD) y revelan la infraestructura interna a un posible atacante.
