# Bloque 11 · Examen fácil — Soluciones (teoría)

1. `argparse` valida tipos y argumentos obligatorios, genera mensajes de error y una ayuda (`-h`) automática, soporta valores por defecto, opciones y subcomandos. Hacerlo a mano es repetitivo y propenso a errores.
2. El **posicional** se identifica por su lugar y suele ser obligatorio; la **opción con valor** (`--puertos 1-100`) lleva un valor asociado; la **bandera** (`--json`) es un sí/no: está presente o no.
3. Es una "orden" dentro de la herramienta, con sus propios argumentos (como `git commit` o `git push`). Ejemplo: `git`, `docker`, o una CLI de seguridad con `escanear` y `reportar`.
4. El logging permite activar o silenciar mensajes por nivel sin tocar el código, enviarlos a varios destinos con rotación y darles un formato consistente con metadatos. `print` siempre sale, ensucia la salida y no se filtra.
5. DEBUG: detalle para depurar; INFO: eventos normales; WARNING: algo inusual pero no fatal; ERROR: un fallo que impidió una operación; CRITICAL: un fallo grave que puede detener el programa.
6. Es un log donde cada campo está etiquetado (p. ej. `ip=... usuario=...` o JSON). Facilita el análisis porque las herramientas pueden extraer campos concretos sin adivinar su posición en el texto.
7. Es código que comprueba automáticamente que otro código se comporta como se espera. `pytest` descubre las pruebas, ejecuta los `assert`, informa de fallos con detalle y ofrece utilidades (fixtures, parametrización).
8. Un mock es un sustituto controlado de una dependencia (como un cliente de red) que devuelve respuestas predefinidas. Se usa para que las pruebas no dependan de la red, sean rápidas, deterministas y no gasten cuota.
9. Porque el código suele acabar en repositorios o paquetes que otros pueden ver; una clave incrustada se filtra y puede ser usada por terceros. Se leen de variables de entorno o de configuración externa.
10. El cliente envía solo un prefijo del hash SHA-1 de la contraseña; el servicio devuelve todos los sufijos con ese prefijo y el cliente busca el suyo localmente. Así nunca envía la contraseña ni su hash completo.
