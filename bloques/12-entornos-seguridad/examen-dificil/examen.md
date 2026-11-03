# Bloque 12 · Python en entornos de seguridad — Examen difícil (final del sílabo)

Integra CTF (XOR y patrones), automatización de resultados y correlación de eventos de SOC con ventana de tiempo.
**Local y con datos de ejemplo.** Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica el procedimiento para romper un XOR de un solo byte cuando conoces una parte del texto claro (un "crib" como `FLAG{`).
2. ¿Por qué una ventana de tiempo deslizante es la forma correcta de detectar fuerza bruta, y qué complejidad tiene frente a comparar todos los pares de eventos?
3. En un SOC, ¿por qué conviene agrupar (deduplicar) alertas repetidas en vez de mostrarlas una a una?
4. ¿Qué es un falso positivo en una alerta y cómo afecta subir o bajar el umbral de detección?
5. Al automatizar el parseo de la salida de una herramienta, ¿por qué hay que ser tolerante a líneas con formato inesperado?
6. En depuración de un fallo propio, ¿cómo ayuda un "patrón cíclico" a localizar en qué posición de la entrada ocurrió el problema?
7. ¿Por qué el trabajo de un analista está más en correlacionar y priorizar que en generar más alertas?
8. ¿Qué diferencia hay, ética y legalmente, entre resolver un CTF y usar la misma técnica contra un sistema real sin permiso?
9. ¿Por qué conviene normalizar las marcas de tiempo y las IPs antes de correlacionar eventos de varias fuentes?
10. ¿Por qué una buena herramienta de seguridad debe ser reproducible y estar bien probada (tests) antes de usarse en un incidente real?

## Parte B — Ejercicios (5 problemas)

1. Un reto te da un mensaje cifrado con XOR de **un solo byte** y sabes que el texto claro contiene una pista (por ejemplo `FLAG{`). Escribe `romper_xor_un_byte(cifrado, pista)` que pruebe las 256 claves y devuelva la pareja `(clave, texto)` cuya descodificación (en latin-1) contenga la pista. Si ninguna la contiene, devuelve `None`.

2. Un SIEM recibe eventos, cada uno con `ts` (segundos), `ip` y `tipo`. Escribe `alertas_fuerza_bruta(eventos, umbral, ventana)` que devuelva, ordenadas, las IPs que acumulen al menos `umbral` eventos de tipo `"login_fallido"` dentro de alguna ventana de `ventana` segundos.

3. Para no saturar al analista, agrupa alertas repetidas. Dada una lista de alertas con `tipo`, `origen` y `ts`, escribe `agrupar_alertas(alertas)` que devuelva una lista de registros `{tipo, origen, conteo, primero, ultimo}` (con la marca de tiempo mínima y máxima de cada grupo), ordenada por `tipo` y luego por `origen`.

4. Automatizas la lectura de un informe de servicios con líneas tipo `22/tcp open ssh`. Escribe `parsear_servicios(texto)` que devuelva, en orden, un registro `{puerto, servicio}` por cada línea cuyo estado sea `open` (ignora las demás y las líneas que no encajen en el formato `PUERTO/tcp ESTADO SERVICIO`).

5. Al depurar un fallo de tu propio programa, un patrón cíclico te dice en qué posición cayó tu entrada. Escribe `generar_ciclico(longitud)` que devuelva una cadena de esa longitud en la que cada subcadena de 4 caracteres es única, y `posicion_ciclico(patron, fragmento)` que devuelva el índice donde aparece `fragmento` en el patrón, o `-1` si no está.

Corrige con: `python corregir.py 12 dificil`
