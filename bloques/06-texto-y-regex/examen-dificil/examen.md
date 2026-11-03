# Bloque 06 · Texto y expresiones regulares — Examen difícil

Combina bloques 01–05 (control de flujo, funciones, diccionarios, conjuntos, archivos) con regex sobre `auth.log`.

## Parte A — Teoría (10 preguntas)

1. ¿Qué diferencia hay entre `.*` (codicioso) y `.*?` (perezoso)? Ejemplo con `<a><b>` y `<.*>`.
2. ¿Qué devuelve `re.findall(r"(\d+)\.(\d+)", "1.2 y 3.4")`?
3. ¿Qué hace `(?:...)` y en qué se diferencia de `(...)`?
4. ¿Por qué `\d{1,3}(\.\d{1,3}){3}` acepta `999.999.999.999`? ¿Cómo validarías bien una IP?
5. ¿Qué hace `re.sub(r"(\d+)\.(\d+)", r"\2.\1", "1.2")`?
6. ¿Qué ventaja tiene `re.compile` cuando procesas un log de 1 millón de líneas?
7. ¿Qué es *ReDoS* y qué tipo de patrón lo provoca (p. ej. `(a+)+$`)?
8. ¿Qué devuelve `m.groupdict()` para `re.match(r"(?P<u>\w+)@(?P<d>\S+)", "ana@example.com")`?
9. ¿Qué hacen `^` y `$` con la bandera `re.MULTILINE`?
10. ¿Por qué hay que anonimizar IPs y usuarios antes de compartir logs (p. ej. con un proveedor)?

## Parte B — Código (5 ejercicios)

1. `parsear_linea(linea)` → para líneas `Failed`/`Accepted` de sshd devuelve un dict con: `fecha` (`"Mar 10 08:15:01"`), `host`, `pid` (int), `evento` (`"Failed"` o `"Accepted"`), `metodo` (`"password"`, `"publickey"`…), `usuario`, `invalido` (bool), `ip`, `puerto` (int). Otras líneas → `None`. Usa grupos con nombre.
2. `fallos_por_ip(lineas)` → `{ip: nº de Failed}` (usa `parsear_linea`).
3. `usuarios_invalidos(lineas)` → lista ordenada y sin repetidos de los usuarios de líneas `invalid user`.
4. `ips_validas(texto)` → extrae candidatas IPv4 y devuelve solo las de octetos 0–255 (sin repetir, en orden de aparición).
5. `anonimizar(linea)` → sustituye el último octeto de cada IPv4 por `x` (`203.0.113.5` → `203.0.113.x`) con `re.sub` y grupos.

Corrige con: `python corregir.py 06 dificil`
