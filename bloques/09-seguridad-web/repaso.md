# Bloque 09 · Seguridad web — Repaso

**1. ¿Qué es la inyección SQL?**
Cuando la entrada del usuario se **concatena** en una consulta y cambia su significado: `"... WHERE nombre = '" + x + "'"` con `x = "' OR '1'='1"` devuelve todos los registros.

**2. ¿Cómo se evita?**
Con **consultas parametrizadas**: `cur.execute("SELECT * FROM u WHERE nombre = ?", (x,))`. La base de datos trata `x` siempre como dato, nunca como código SQL.

**3. ¿Se pueden parametrizar nombres de columnas o `ORDER BY`?**
No: los parámetros solo sustituyen **valores**. Para identificadores se usa una **lista blanca** (allowlist) de valores permitidos.

**4. ¿Validar en el cliente (JavaScript) es suficiente?**
No. El cliente lo controla el usuario; hay que validar **siempre en el servidor**. Mejor allowlist (lo que se permite) que denylist (lo que se prohíbe).

**5. ¿Qué es XSS y cómo se mitiga?**
Inyectar HTML/JS en una página que verán otros usuarios. Se mitiga **escapando la salida** según el contexto (`html.escape`), y con cabeceras como Content-Security-Policy.
