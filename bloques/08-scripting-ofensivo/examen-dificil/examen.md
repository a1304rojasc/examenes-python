# Bloque 8 · Scripting ofensivo (enfoque defensivo) — Examen difícil

Combina reconocimiento, estimación de fuerza bruta, fuzzing del propio código, análisis de formularios y revisión de APIs.
**Todo es local y con datos de ejemplo.** Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica por qué el coste de la fuerza bruta es exponencial en la longitud y cómo esto justifica exigir contraseñas largas.
2. ¿Qué es la entropía de una contraseña (en bits) y por qué sirve para comparar su resistencia?
3. ¿Por qué un ataque de diccionario con reglas (mutaciones comunes) suele ser más eficaz que la fuerza bruta pura contra contraseñas humanas?
4. Explica cómo, como defensor, el límite de intentos y el retardo creciente (rate limiting / backoff) encarecen un ataque de fuerza bruta.
5. ¿Qué es el fuzzing basado en mutación y en qué se diferencia del basado en generación? ¿Qué buscas en las entradas que provocan fallos?
6. Al automatizar la extracción de formularios de una web, ¿por qué interesan también los campos ocultos y el token CSRF?
7. ¿Por qué una API debe aplicar control de acceso en el servidor y no confiar en que el cliente "no llame" a ciertos endpoints?
8. ¿Qué es el versionado de una API y por qué los endpoints antiguos y olvidados son un riesgo frecuente?
9. En recon, ¿por qué conviene deduplicar y normalizar los datos (dominios, URLs) antes de analizarlos?
10. ¿Qué diferencia ética y legal hay entre encontrar un fallo en un programa de *bug bounty* autorizado y probar la misma técnica contra un sistema sin permiso?

## Parte B — Ejercicios (5 problemas)

1. Para una charla de concienciación necesitas estimar el peor caso de adivinar una contraseña por fuerza bruta. Escribe `tiempo_fuerza_bruta(longitud, tamano_alfabeto, intentos_por_segundo)` que devuelva cuántos **segundos** tardaría probar todas las combinaciones a esa velocidad. Si la velocidad no es positiva, debe fallar.

2. Un medidor de contraseñas estima su fortaleza. Escribe `entropia_bits(password)` que devuelva la entropía aproximada en bits: la longitud multiplicada por el logaritmo en base 2 del tamaño del alfabeto que **realmente** usa (minúsculas aportan 26, mayúsculas 26, dígitos 10 y símbolos 32). Una cadena vacía vale 0.

3. Antes de publicar tu propio analizador quieres comprobar que no se rompe con entradas raras. Escribe `fuzzear(funcion, entradas)` que pruebe la función con cada entrada de la lista y devuelva la lista de las entradas que provocan una excepción (un "crash").

4. Para auditar un formulario de login necesitas sus detalles. Escribe `analizar_formulario(html)` que devuelva un registro con la `accion` (atributo `action`), el `metodo` en minúsculas (`get` si no se indica) y la lista `campos` con los nombres (`name`) de todos los campos de entrada, incluidos los ocultos, en orden.

5. Revisando la configuración de una API recibes una lista de endpoints, cada uno con su `ruta`, su `metodo` y si `requiere_auth`. Escribe `endpoints_inseguros(endpoints)` que devuelva, ordenadas, las rutas de los endpoints que permiten **modificar datos** (métodos POST, PUT, PATCH o DELETE) **sin** requerir autenticación.

Corrige con: `python corregir.py 8 dificil`
