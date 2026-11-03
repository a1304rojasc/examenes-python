# Bloque 9 · Examen fácil — Soluciones (teoría)

1. Es insertar código SQL a través de la entrada del usuario para alterar la consulta. Por ejemplo `' OR '1'='1` convierte una condición en siempre verdadera y devuelve todos los registros.
2. Porque el valor viaja por un canal aparte (un `?` y una tupla de datos): la base de datos nunca lo interpreta como SQL. Concatenar lo convierte en parte de la sentencia, que es justo lo que explota la inyección.
3. Es inyectar HTML/JavaScript que la web guarda o refleja y luego ejecuta en el navegador de **otros** usuarios, pudiendo robarles la sesión o actuar en su nombre. El daño lo sufre quien visita la página, no el atacante.
4. Es sustituir los caracteres especiales (`<`, `>`, `&`, `"`, `'`) por entidades HTML (`&lt;`, `&gt;`…). Así el navegador los muestra como texto en lugar de interpretarlos como etiquetas o atributos.
5. Porque el usuario controla su navegador y puede enviar peticiones directamente (curl, un proxy), saltándose cualquier validación de JavaScript. La validación obligatoria debe estar en el servidor.
6. Es conseguir que el **servidor** haga una petición a una URL elegida por el atacante. Es peligroso porque el servidor puede alcanzar recursos internos (loopback, metadatos de la nube, servicios privados) que el atacante no alcanzaría directamente.
7. Es cuando la web redirige a una URL controlada por el usuario sin validarla. Permite enviar a la víctima a un sitio malicioso que parece legítimo (phishing), aprovechando la confianza en el dominio original.
8. Es un valor secreto, impredecible y ligado a la sesión, que el servidor exige al recibir el formulario para confirmar que la petición viene de su propia página. Suele viajar en un campo oculto (`<input type="hidden">`).
9. Porque la allowlist deniega por defecto todo lo no previsto; la denylist intenta enumerar lo malo y siempre se olvida algún caso o se evade. "Permitir solo lo conocido" es más seguro.
10. Porque se puede evadir (codificaciones, variantes, mayúsculas) y produce falsos positivos. Es una capa de alerta útil, pero la defensa real son las consultas parametrizadas, el escape de salida y la validación en el servidor.
