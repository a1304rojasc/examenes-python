# Bloque 09 · Examen difícil — Soluciones (teoría)

1. Porque son **comodines de LIKE**, no de SQL: un usuario que busca `%` obtendría todo (o provocaría consultas costosas). Se escapan y se usa `ESCAPE '\'`.
2. Permite **enumerar usuarios** válidos; luego el atacante concentra la fuerza bruta en ellos. Se responde siempre "credenciales incorrectas".
3. El dato malicioso se guarda "bien" (parametrizado) pero **más tarde** otra parte del código lo concatena en una consulta y se ejecuta.
4. Los patrones se pueden **evadir** (codificaciones, comentarios, mayúsculas, sintaxis alternativa) y dan falsos positivos. La parametrización elimina el problema de raíz.
5. Una web maliciosa hace que el navegador de la víctima envíe una petición autenticada a otro sitio. El token, ligado a la sesión e incluido en el formulario, no lo conoce el atacante.
6. Para que sea **impredecible** y para evitar ataques de **temporización** al compararlo.
7. CSP limita de dónde se pueden cargar/ejecutar scripts (mitiga XSS). `HttpOnly` impide que JavaScript lea la cookie (dificulta robar la sesión con XSS).
8. Evita que una sola petición **extraiga masivamente** datos o agote recursos del servidor (DoS).
9. Todos a la vez es mejor experiencia; pero los mensajes no deben revelar información interna (consultas, rutas, si un usuario existe…).
10. La lista de los 10 riesgos web más críticos de OWASP. Inyección SQL y XSS están en **A03: Injection** (edición 2021).
