# Bloque 06 · Texto y expresiones regulares — Repaso

**1. ¿Qué hacen `strip()`, `split()` y `join()`?**
`strip()` quita espacios en los extremos; `split()` parte en una lista (por espacios si no se indica separador); `"-".join(lista)` une con el separador.

**2. ¿Diferencia entre `re.search`, `re.match` y `re.fullmatch`?**
`search` busca en cualquier parte; `match` solo al **inicio**; `fullmatch` exige que **todo** el texto coincida.

**3. ¿Qué significan `\d`, `\s`, `\S`, `+` y `?`?**
Dígito, espacio en blanco, no-espacio, "uno o más", "cero o uno" (opcional).

**4. ¿Por qué se escriben los patrones como `r"..."`?**
Cadena *raw*: la barra invertida no se interpreta como escape de Python (`r"\d"` en lugar de `"\\d"`).

**5. ¿Qué es un grupo con nombre?**
`(?P<ip>\S+)`: luego se lee con `m.group("ip")` o `m.groupdict()`. Hace los parsers de logs legibles.

Ejemplo de línea de `auth.log` (SSH) usada en los exámenes:
```
Mar 10 08:15:01 servidor sshd[1234]: Failed password for invalid user admin from 203.0.113.5 port 52211 ssh2
```
