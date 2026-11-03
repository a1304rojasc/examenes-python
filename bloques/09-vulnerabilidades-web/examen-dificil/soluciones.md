# Bloque 9 · Examen difícil — Soluciones (teoría)

1. Porque `%` y `_` son **comodines de LIKE**, no de SQL: si el usuario los envía, cambian qué coincide (p. ej. `%` casa con todo). Se escapan y se declara el carácter de escape con `ESCAPE`.
2. Los parámetros sustituyen **valores**, no partes de la estructura de la consulta. Un nombre de columna u `ORDER BY` es estructura; se protege con una **lista blanca** de valores permitidos y se rechaza cualquier otro.
3. Un XSS reflejado devuelve en la respuesta, sin escapar, algo que vino en la petición. Para detectarlo se envía (en pruebas autorizadas) un marcador con `<`/`>` y se comprueba si aparece **literal** en la respuesta; si está escapado, la salida es segura.
4. Cada contexto interpreta caracteres distintos: en HTML peligran `<`/`>`, en un atributo las comillas, en JavaScript las comillas y barras, en una URL hace falta *url-encoding*. Escapar para el contexto equivocado deja huecos explotables.
5. Porque esas direcciones solo son accesibles desde dentro: el servidor podría alcanzar servicios internos o el endpoint de **metadatos de la nube** (`169.254.169.254`), que entrega credenciales. Un atacante externo las usa a través del SSRF.
6. `//host` y `https://host` hacen que el navegador vaya a otro dominio; `/\host` lo interpretan algunos navegadores como `//host`; `@host` coloca el dominio real tras un `usuario@`, engañando a validaciones que miran el principio de la cadena.
7. Porque `example.com.evil.com` **empieza por**/`contiene` `example.com` pero es otro dominio controlado por el atacante. Hay que comparar el host de forma **exacta**, no por subcadena.
8. Campos ocultos y tokens revelan cómo funciona el formulario y su protección CSRF; los comentarios HTML a veces filtran rutas, credenciales o notas de desarrollo. Todo eso ayuda a un atacante a planear el ataque.
9. Para no filtrar si un usuario existe o por qué falló: "credenciales incorrectas" en vez de "usuario no existe" evita la enumeración de cuentas y da menos pistas al atacante.
10. Es combinar varias capas de defensa para que, si una falla, otra contenga el daño. Para SQLi: parametrizar + validar + mínimos privilegios de la cuenta BD. Para XSS: escapar salida + CSP + cookies HttpOnly. Para SSRF: allowlist de destinos + bloqueo de IPs internas + segmentación de red.
