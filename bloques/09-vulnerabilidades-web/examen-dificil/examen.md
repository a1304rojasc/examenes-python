# Bloque 9 · Análisis de vulnerabilidades web — Examen difícil

Combina SQLi, XSS, SSRF/redirección abierta y parsing de HTML, con las ideas de redes del Bloque 5 (`ipaddress`).
Enfoque **defensivo**; datos de ejemplo. Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. En una búsqueda con `LIKE`, ¿por qué hay que escapar `%` y `_` aunque la consulta esté parametrizada?
2. ¿Por qué parametrizar protege los **valores** pero no sirve para nombres de columna o `ORDER BY`, y cómo se protege eso?
3. ¿Qué es un XSS reflejado y cómo detectarías, desde el lado defensivo, que un parámetro se refleja sin escapar?
4. Explica por qué el contexto (HTML, atributo, JavaScript, URL) determina cómo hay que escapar una salida.
5. ¿Por qué un filtro anti-SSRF debe bloquear direcciones privadas, de loopback y de enlace local (como `169.254.169.254`)?
6. ¿Qué trucos usan los atacantes para saltarse una validación ingenua de redirección (`//host`, `https://host`, `/\host`, `@host`)?
7. ¿Por qué validar un host por "empieza por" o "contiene" el dominio permitido es inseguro? Da un ejemplo que lo burle.
8. ¿Qué información sensible se extrae a veces analizando el HTML (campos ocultos, comentarios, tokens) y por qué?
9. ¿Por qué conviene devolver mensajes de error genéricos en el login y las búsquedas?
10. ¿Qué es la defensa en profundidad y cómo se aplica a la vez a SQLi, XSS y SSRF?

## Parte B — Ejercicios (5 problemas)

Las tablas las crean los tests.

1. Un catálogo busca productos cuyo nombre **contiene** un texto del usuario, ordenados por un campo elegido y con un límite. Escribe `buscar_productos(con, texto, orden="nombre", limite=10)` sobre `productos(id, nombre, precio)`: los comodines `%` y `_` del texto deben buscarse de forma literal; `orden` solo puede ser `nombre`, `precio` o `id` (si no, error); `limite` debe ser un entero entre 1 y 100 (si no, error). Devuelve tuplas `(id, nombre, precio)`.

2. Un analizador defensivo revisa si un valor del usuario se reflejó en la respuesta sin escapar. Escribe `reflejo_sin_escapar(valor, respuesta)` que devuelva `True` si el valor contiene `<` o `>` y aparece **literalmente** (sin escapar) dentro del HTML de respuesta.

3. Tras el login, la web redirige al destino que pidió el usuario. Escribe `destino_seguro(url, dominio_permitido)` que devuelva `True` solo si el destino se queda dentro del sitio: o bien es una ruta relativa que empieza por `/` (pero no `//` ni `/\`), o bien una URL absoluta http/https cuyo host es exactamente `dominio_permitido`.

4. Un filtro anti-SSRF rechaza URLs que apuntan a la propia infraestructura. Escribe `apunta_a_interno(url)` que devuelva `True` si el host de la URL es `localhost` o una dirección IP privada, de loopback, de enlace local o reservada. Si el host es un nombre de dominio normal, devuelve `False` (no se resuelve aquí).

5. Para auditar una página, escribe `inventario_formularios(html)` que devuelva una lista con un registro por cada formulario: su `accion`, su `metodo` en minúsculas (`get` por defecto), la lista `campos` de nombres de entrada y el `token_csrf` (valor del campo oculto cuyo nombre contiene `csrf`, o `None`).

Corrige con: `python corregir.py 9 dificil`
