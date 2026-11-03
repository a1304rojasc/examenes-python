# Bloque 9 · Análisis de vulnerabilidades web — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py`. Enfoque **defensivo**; SQLite en memoria, datos de ejemplo.
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué es una inyección SQL y cómo cambia el significado de una consulta?
2. Explica por qué una consulta parametrizada es la defensa correcta frente a concatenar la entrada en el SQL.
3. ¿Qué es el XSS y por qué es un problema que afecta a **otros** usuarios de la web?
4. ¿En qué consiste "escapar" la salida HTML y qué caracteres se transforman?
5. ¿Por qué validar la entrada solo en el navegador (JavaScript) no es suficiente?
6. ¿Qué es un SSRF (Server-Side Request Forgery) y por qué es peligroso que el servidor siga una URL dada por el usuario?
7. ¿Qué es una redirección abierta y qué daño permite?
8. ¿Qué es un token CSRF y dónde suele viajar dentro de un formulario?
9. ¿Por qué conviene una lista blanca (allowlist) de hosts permitidos en vez de una lista negra?
10. ¿Por qué un detector de patrones de ataque no debe ser la única defensa?

## Parte B — Ejercicios (5 problemas)

1. Una tienda busca clientes por nombre en su base de datos. La tabla `usuarios(id, nombre, email)` la crean los tests. Escribe `buscar_usuario(con, nombre)` que devuelva la tupla `(id, nombre, email)` del usuario con ese nombre exacto, o `None`, de forma que una entrada como `' OR '1'='1` no devuelva registros.

2. Un sistema de alertas marca entradas sospechosas de inyección SQL para revisión humana. Escribe `parece_sqli(entrada)` que devuelva `True` si el texto contiene patrones típicos: una comilla simple seguida de `OR`/`AND`, el comentario `--`, un `;`, el inicio de comentario `/*`, o una secuencia `UNION ... SELECT` (sin distinguir mayúsculas).

3. Un foro muestra los comentarios de los usuarios. Para evitar XSS, escribe `escapar_html(texto)` que devuelva el texto seguro para insertar en HTML, transformando también las comillas.

4. Para auditar la protección CSRF de un formulario necesitas su token. Escribe `extraer_token_csrf(html)` que devuelva el valor del primer campo oculto cuyo nombre contenga `csrf` (sin distinguir mayúsculas), o `None` si no hay.

5. Antes de que el servidor siga una URL proporcionada por el usuario, hay que validarla. Escribe `url_permitida(url, hosts_permitidos)` que devuelva `True` solo si el esquema es `http`/`https` y el host está en el conjunto de hosts permitidos.

Corrige con: `python corregir.py 9 facil`
