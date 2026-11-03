# Bloque 11 · Automatización y herramientas — Examen difícil

Combina validación en la CLI, filtrado de logs por nivel, cacheo con mocks y parseo/consolidación de respuestas de APIs de seguridad.
Datos de ejemplo; **sin red ni claves**. Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Por qué conviene validar los argumentos de la CLI con un "tipo" propio en `argparse` en lugar de comprobarlos después?
2. ¿Qué diferencia hay entre que una validación falle con un mensaje claro y que el programa reviente a mitad de ejecución?
3. ¿Por qué el orden de los niveles de log (DEBUG < INFO < WARNING < ERROR < CRITICAL) permite filtrar por un umbral?
4. ¿Qué es la rotación de logs y qué problema evita?
5. ¿Por qué cachear respuestas de una API reduce coste y es, además, más amable con el servicio?
6. Al escribir un test con un cliente simulado que cuenta llamadas, ¿qué te permite verificar sobre el cacheo?
7. ¿Por qué hay que validar y normalizar los datos que vienen de una API externa antes de usarlos?
8. ¿Qué riesgos hay si confías ciegamente en que una respuesta de API tendrá siempre todos los campos esperados?
9. Al consolidar indicadores (IOC) de varias fuentes, ¿por qué conviene deduplicar y descartar los inválidos?
10. ¿Por qué una herramienta de seguridad debe limitar su frecuencia de peticiones (rate limit) a las APIs que consulta?

## Parte B — Ejercicios (5 problemas)

1. Tu CLI acepta un rango de puertos como `"inicio-fin"`. Escribe `rango_de_puertos(texto)` que devuelva la pareja `(inicio, fin)` como enteros, validando que ambos estén entre 1 y 65535 y que `inicio <= fin`. Si el formato o los valores no son válidos, debe lanzar `argparse.ArgumentTypeError`.

2. Para revisar un log, quieres quedarte solo con lo importante. Dadas unas líneas con el formato `[NIVEL] mensaje...`, escribe `filtrar_por_nivel(lineas, minimo)` que devuelva, en orden, las líneas cuyo nivel sea igual o superior a `minimo` según el orden DEBUG < INFO < WARNING < ERROR < CRITICAL.

3. Para no consultar dos veces lo mismo a una API, escribe `consultar_con_cache(cliente, clave, cache)` que, si `clave` ya está en el registro `cache`, devuelva el valor guardado sin llamar; y si no, llame a `cliente(clave)`, guarde el resultado en `cache` y lo devuelva.

4. La respuesta de una API tipo Shodan para un host trae una lista `ports` y una lista `data` de servicios, cada uno con `port` y `product`. Escribe `resumen_shodan(respuesta)` que devuelva un registro con `puertos` (lista ordenada y sin repetir de los puertos) y `servicios` (un registro `puerto -> product`).

5. Recibes indicadores de varias fuentes, cada una con listas `ips` y `dominios`. Escribe `consolidar_iocs(feeds)` que devuelva un registro con `ips` (direcciones IP válidas, sin repetir, ordenadas numéricamente) y `dominios` (en minúsculas, sin repetir, ordenados), descartando las IPs que no sean válidas.

Corrige con: `python corregir.py 11 dificil`
