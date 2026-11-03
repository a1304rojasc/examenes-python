# Bloque 07 · Redes — Examen difícil

Combina bloques 01–06 (estructuras de datos, excepciones, texto) con redes. Todo es local (`127.0.0.1`) o IPs de documentación.

## Parte A — Teoría (10 preguntas)

1. ¿Por qué ordenar IPs como texto da `["192.0.2.10", "192.0.2.9"]`? ¿Cómo se ordenan bien?
2. ¿Cuántas subredes `/26` caben en una `/24` y cuántos hosts usables tiene cada una?
3. ¿Qué devuelve `connect_ex` y en qué se diferencia de `connect`?
4. ¿Por qué hay que poner `settimeout` a un socket cliente?
5. ¿Qué significa enlazar (`bind`) un servidor al puerto `0`?
6. En HTTP, ¿cómo se separan las cabeceras del cuerpo? ¿Son sensibles a mayúsculas los nombres de cabecera?
7. ¿Qué indica la cabecera `Content-Length` y qué riesgo hay si no se valida?
8. ¿Qué es una *allowlist* de redes y por qué es preferible a una *denylist*?
9. Diferencia entre `recv(1024)` devolviendo `b""` y lanzando `socket.timeout`.
10. ¿Por qué escanear puertos de un sistema ajeno sin permiso es un problema (legal y ético) aunque "solo mires"?

## Parte B — Código (5 ejercicios)

1. `agrupar_por_red(ips, prefijo)` → `{"a.b.c.0/prefijo": [ips]}` agrupando cada IP en su red; las IPs de cada grupo ordenadas **numéricamente**.
2. `fuera_de_allowlist(ips, redes)` → lista (en orden original) de las IPs que no pertenecen a ninguna red permitida. IPs inválidas también se consideran fuera.
3. `parsear_peticion(texto)` → dict `{"metodo", "ruta", "version", "cabeceras", "cuerpo"}` de una petición HTTP en texto con `\r\n`. Las claves de `cabeceras` en minúsculas.
4. `respuesta_http(codigo, cuerpo)` → `bytes` de una respuesta HTTP/1.1 con línea de estado (frase de `http.HTTPStatus`), cabeceras `Content-Type: text/plain; charset=utf-8` y `Content-Length` correcto **en bytes**, línea vacía y cuerpo.
5. `puerto_abierto(host, puerto, timeout=1.0)` → `True` si se puede conectar por TCP (usa `connect_ex`). Solo se prueba contra `127.0.0.1`.

Corrige con: `python corregir.py 07 dificil`
