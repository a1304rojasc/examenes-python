# Bloque 06 · Texto y expresiones regulares — Examen fácil

Líneas de ejemplo (`auth.log` ficticio):
```
Mar 10 08:15:01 servidor sshd[1234]: Failed password for root from 203.0.113.5 port 52211 ssh2
Mar 10 08:15:09 servidor sshd[1234]: Failed password for invalid user admin from 198.51.100.7 port 40022 ssh2
Mar 10 08:16:00 servidor sshd[1240]: Accepted password for ana from 192.0.2.10 port 50000 ssh2
```

## Parte A — Teoría (10 preguntas)

1. ¿Qué devuelve `"  ssh  ".strip()`?
2. ¿Qué devuelve `"a b  c".split()`? ¿Y `"a b  c".split(" ")`?
3. ¿Qué devuelve `"-".join(["192", "0", "2"])`?
4. ¿Qué coincide con `\d+`? a) letras b) uno o más dígitos c) un espacio d) nada
5. ¿Qué diferencia hay entre `re.search` y `re.match`?
6. ¿Qué devuelve `re.findall(r"\d+", "puerto 22 y 443")`?
7. ¿Qué devuelve `re.search` si no encuentra nada?
8. ¿Para qué sirve `\.` en un patrón?
9. ¿Qué devuelve `"Failed" in linea` para la primera línea de ejemplo?
10. ¿Qué hace `re.IGNORECASE`?

## Parte B — Código (5 ejercicios)

1. `normalizar_espacios(texto)` → quita espacios en los extremos y deja un solo espacio entre palabras.
2. `extraer_ips(texto)` → lista (en orden) de todas las cadenas con forma IPv4 (`n.n.n.n`, 1 a 3 dígitos por bloque) usando `re.findall`.
3. `es_linea_fallida(linea)` → `True` si la línea contiene `"Failed password"`.
4. `extraer_usuario(linea)` → usuario de una línea `Failed`/`Accepted ... for [invalid user] USUARIO from ...`, o `None`.
5. `es_email_valido(texto)` → `True` si `texto` es *completo* `algo@dominio.tld` (sin espacios, un solo `@`, al menos un punto en el dominio y TLD de 2+ letras). Usa `re.fullmatch`.

Corrige con: `python corregir.py 06 facil`
