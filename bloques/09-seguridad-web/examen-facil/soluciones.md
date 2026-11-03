# Bloque 09 · Examen fácil — Soluciones (teoría)

1. **Todas las filas**: `'1'='1'` es siempre verdadero.
2. **b) `?`** (también admite `:nombre`).
3. Si el valor viene del usuario puede contener SQL (`1 OR 1=1`, `1; DROP TABLE ...`). Nunca se confía en el tipo esperado: se parametriza.
4. Allowlist: solo se acepta lo **explícitamente permitido**. Denylist: se bloquea lo conocido como malo (siempre se olvida algo).
5. Devuelve **`"&lt;b&gt;"`**: el navegador lo muestra como texto, no lo interpreta.
6. Porque el atacante puede saltarse el navegador y enviar peticiones directamente (curl, proxy, script).
7. **`con.commit()`**.
8. **`None`**.
9. La web debe conectarse con un usuario que solo tenga los permisos **imprescindibles** (p. ej. sin `DROP` ni acceso a otras bases), para limitar el daño si se compromete.
10. Porque los parámetros van en una **tupla**; `(x)` es solo `x` entre paréntesis, `(x,)` es una tupla de un elemento.
