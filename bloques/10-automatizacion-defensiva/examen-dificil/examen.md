# Bloque 10 · Automatización defensiva — Examen difícil (final)

Integra **todo** el curso: regex sobre `auth.log` (06), estructuras de datos (04), archivos (05), redes/`ipaddress` (07), CLI con `argparse` y tests con `pytest`.

## Parte A — Teoría (10 preguntas)

1. ¿Qué complejidad tiene la ventana deslizante con dos índices frente a comparar todos los pares de eventos?
2. Un atacante reparte los intentos entre 50 IPs distintas (1 intento por IP). ¿Lo detecta un detector por IP? ¿Qué otra agregación usarías?
3. ¿Por qué el script **nunca** debe bloquear automáticamente la red de administración? ¿Cómo lo garantizas?
4. ¿Qué riesgo tiene bloquear automáticamente IPs a partir de logs que un atacante puede influir (p. ej. con IPs falsificadas en un campo de texto)?
5. ¿Qué ventaja tiene que `main(argv)` reciba la lista de argumentos en lugar de leer `sys.argv` directamente?
6. ¿Por qué ofrecer salida `--json` además de texto?
7. ¿Qué es un *falso positivo* y un *falso negativo* en detección? ¿Qué efecto tiene subir el umbral?
8. ¿Qué es el *mutation testing* y qué mide?
9. ¿Por qué un test que solo comprueba el "camino feliz" no detecta errores de límite (`>` vs `>=`)?
10. Cita dos herramientas reales que hacen lo que este script (p. ej. para SSH) y una limitación de las reglas basadas solo en logs.

## Parte B — Código (5 ejercicios)

1. `detectar_fuerza_bruta(lineas, umbral=5, ventana=60, anio=2026)` → `{ip: max_fallos_en_ventana}` solo para IPs que alcanzan el umbral, a partir de líneas `Failed password` de sshd.
2. `generar_informe(alertas, como_json=False)` → texto con una línea por IP, ordenadas de más a menos fallos (empate: IP numérica) `"ALERTA <ip>: <n> fallos en ventana"`, o `"Sin alertas"` si está vacío. Con `como_json=True` devuelve `json.dumps(alertas, sort_keys=True)`.
3. `main(argv)` → CLI (`archivo`, `--umbral`, `--ventana`, `--json`): lee el log, detecta, **imprime** el informe y devuelve `1` si hay alertas o `0` si no.
4. `reglas_bloqueo(ips, allowlist)` → lista de reglas `"DENY <ip>"` ordenadas numéricamente y sin repetir, **excluyendo** cualquier IP dentro de las redes de `allowlist` (nunca te bloquees a ti mismo).
5. `verificar_detector(detector)` → escribe **tus propios tests**: recibe una función `detector(tiempos, umbral, ventana)` que debería comportarse como `es_fuerza_bruta` del examen fácil (entrada desordenada, `>= umbral`, ventana inclusiva `t_fin - t_ini <= ventana`). Tu función ejecuta `assert`s sobre ella y debe **lanzar `AssertionError`** si el detector es incorrecto y **no lanzar nada** si es correcto. El corrector la prueba contra una versión buena y varias con errores ("mutantes").

Corrige con: `python corregir.py 10 dificil`
