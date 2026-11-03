# Bloque 10 · Automatización defensiva — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Qué módulo de la biblioteca estándar se usa para fechas y horas?
2. ¿Qué devuelve restar dos `datetime`? ¿Cómo obtienes los segundos?
3. ¿Qué significan `%b`, `%d` y `%H` en `strptime`?
4. ¿Por qué 5 fallos en 30 segundos son más sospechosos que 5 fallos en un día?
5. En `argparse`, ¿diferencia entre un argumento posicional y una opción `--umbral`?
6. ¿Qué hace `action="store_true"`?
7. ¿Cómo indica pytest que un test ha fallado?
8. ¿Para qué sirve `pytest.raises`?
9. ¿Qué hace la fixture `tmp_path`?
10. ¿Qué código de salida indica éxito en un programa de línea de comandos?

## Parte B — Código (5 ejercicios)

1. `parsear_marca_tiempo(texto, anio=2026)` → `datetime` desde el formato de syslog `"Mar 10 08:15:01"` (también `"Mar  9 ..."` con dos espacios).
2. `dentro_de_ventana(t1, t2, segundos)` → `True` si entre los dos `datetime` hay como mucho `segundos` (en cualquier orden).
3. `max_en_ventana(tiempos, ventana)` → recibe tiempos en segundos (enteros, **desordenados**) y devuelve el mayor número de eventos dentro de cualquier intervalo de `ventana` segundos (`t_final - t_inicial <= ventana`).
4. `crear_parser()` → `argparse.ArgumentParser` con: posicional `archivo`; `--umbral` (int, por defecto 5); `--ventana` (int, por defecto 60); `--json` (bandera).
5. `es_fuerza_bruta(tiempos, umbral, ventana)` → `True` si `max_en_ventana(...) >= umbral`.

Corrige con: `python corregir.py 10 facil`
