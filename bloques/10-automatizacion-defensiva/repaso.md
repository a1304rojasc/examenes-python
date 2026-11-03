# Bloque 10 · Automatización defensiva — Repaso

**1. ¿Qué es detectar fuerza bruta "con ventana de tiempo"?**
Contar fallos de login de una misma IP dentro de un intervalo (p. ej. ≥ 5 fallos en 60 s). Contar el total sin ventana da falsos positivos (un usuario que falla una vez al día).

**2. ¿Cómo se implementa una ventana deslizante eficiente?**
Ordenando los tiempos y usando dos índices (inicio y fin): se avanza el fin y, mientras `t[fin] - t[inicio] > ventana`, se avanza el inicio. El tamaño de la ventana es `fin - inicio + 1`.

**3. ¿Para qué sirve `argparse`?**
Para crear interfaces de línea de comandos: argumentos posicionales, opciones (`--umbral 5`), tipos, valores por defecto y ayuda automática (`-h`).

**4. ¿Qué es un test con `pytest`?**
Una función `test_*` con `assert`. `pytest` la descubre y ejecuta; fixtures como `tmp_path` o `capsys` dan archivos temporales o capturan la salida.

**5. ¿Por qué un script defensivo debe devolver un código de salida?**
Para integrarlo en automatizaciones (cron, CI, SIEM): `0` = sin alertas, distinto de `0` = hay algo que revisar.
