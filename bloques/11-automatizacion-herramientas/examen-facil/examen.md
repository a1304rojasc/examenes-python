# Bloque 11 · Automatización y herramientas — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py`. Datos de ejemplo; **sin red ni claves reales**.
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué ventajas da `argparse` frente a leer los argumentos a mano desde `sys.argv`?
2. ¿Qué diferencia hay entre un argumento posicional, una opción con valor y una bandera (flag)?
3. ¿Qué es un subcomando en una CLI y da un ejemplo de herramienta que los use?
4. ¿Por qué el logging con niveles es mejor que sembrar el código de `print`?
5. ¿Qué significan los niveles DEBUG, INFO, WARNING, ERROR y CRITICAL?
6. ¿Qué es un log con formato estructurado y por qué facilita el análisis posterior?
7. ¿Qué es una prueba automatizada y qué aporta un framework como `pytest`?
8. ¿Qué es un "mock" y por qué se usa al probar código que depende de la red?
9. ¿Por qué nunca se deben incrustar claves de API en el código fuente?
10. ¿Qué es el modelo de k-anonimato que usa "Have I Been Pwned" para comprobar contraseñas filtradas?

## Parte B — Ejercicios (5 problemas)

1. Tu herramienta de seguridad tiene dos subcomandos. Escribe `crear_parser()` que devuelva un analizador de argumentos con: un subcomando `escanear` con un argumento obligatorio `objetivo` y una opción `--puertos` (texto, por defecto `"1-1024"`); y un subcomando `reportar` con un argumento obligatorio `archivo` y una bandera `--json`. El subcomando elegido debe quedar accesible como atributo `comando`.

2. Para registrar eventos de forma uniforme, escribe `linea_log(nivel, mensaje, campos)` que devuelva una cadena con el formato `[NIVEL] mensaje` y, si el registro `campos` no está vacío, añada ` | clave=valor` por cada campo, ordenados por clave y separados por espacios. Ejemplo: `[INFO] acceso | ip=192.0.2.1 usuario=ana`.

3. Una comprobación contra una API tipo VirusTotal recibe su respuesta ya convertida en un registro anidado. Escribe `detecciones_vt(respuesta)` que devuelva cuántos motores marcaron el archivo como malicioso, leyendo `respuesta["data"]["attributes"]["last_analysis_stats"]["malicious"]`. Si falta algún nivel, devuelve 0.

4. Usando el modelo de "Have I Been Pwned", el servicio devuelve un texto con líneas `SUFIJO:conteo`. Escribe `veces_filtrada(respuesta, sufijo)` que devuelva el número de veces que aparece ese sufijo (sin distinguir mayúsculas), o 0 si no está.

5. La clave de API se lee del entorno, nunca del código. Escribe `leer_api_key(entorno, nombre)` que devuelva el valor de esa variable en el registro `entorno`, o lance un error si no existe o está vacía.

Corrige con: `python corregir.py 11 facil`
