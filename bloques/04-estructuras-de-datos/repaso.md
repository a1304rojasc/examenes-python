# Bloque 04 · Estructuras de datos — Repaso

**1. ¿Diferencia entre lista y tupla?**
La lista es **mutable** (`append`, cambiar elementos); la tupla es **inmutable**. Las tuplas pueden ser claves de diccionario; las listas no.

**2. ¿Cómo obtengo un valor de un diccionario sin error si la clave no existe?**
Con `d.get(clave, valor_por_defecto)`. `d[clave]` lanza `KeyError` si no existe.

**3. ¿Qué ventaja tiene un conjunto (`set`)?**
No admite duplicados y comprobar pertenencia (`x in s`) es muy rápido. Permite unión `|`, intersección `&` y diferencia `-`.

**4. Traduce a comprensión:** `r = []; for x in datos: if x > 0: r.append(x * 2)`
`r = [x * 2 for x in datos if x > 0]`

**5. ¿Qué pasa con `b = a` si `a` es una lista y luego hago `b.append(1)`?**
`a` también cambia: ambas variables apuntan a **la misma** lista. Para copiar: `b = a.copy()` o `b = list(a)`.
