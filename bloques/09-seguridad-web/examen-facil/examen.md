# Bloque 09 · Seguridad web — Examen fácil

Todo se hace con una base de datos SQLite **en memoria** (`sqlite3.connect(":memory:")`).

## Parte A — Teoría (10 preguntas)

1. ¿Qué devuelve la consulta `SELECT * FROM usuarios WHERE nombre = '' OR '1'='1'`?
2. ¿Qué marcador de posición usa `sqlite3` para parámetros? a) `%s` b) `?` c) `{}` d) `$1`
3. ¿Por qué `cur.execute(f"... WHERE id = {id}")` es peligroso aunque `id` "debería" ser un número?
4. ¿Qué diferencia hay entre una *allowlist* y una *denylist*?
5. ¿Qué hace `html.escape("<b>")`?
6. ¿Por qué no basta con validar los formularios en el navegador?
7. ¿Qué método confirma los cambios en una conexión `sqlite3`?
8. ¿Qué devuelve `cur.fetchone()` si no hay resultados?
9. ¿Qué es el principio de mínimo privilegio aplicado a la cuenta de base de datos de una web?
10. ¿Por qué en `execute(sql, (x,))` se escribe la coma tras `x`?

## Parte B — Código (5 ejercicios)

1. `validar_usuario(nombre)` → `True` si tiene de 3 a 16 caracteres y solo `a-z`, `0-9` o `_` (allowlist con `re.fullmatch`).
2. `escapar_html(texto)` → texto seguro para insertar en HTML (escapa también comillas).
3. `crear_tabla(con)` crea `usuarios(id INTEGER PRIMARY KEY, nombre TEXT UNIQUE NOT NULL, email TEXT)`; `insertar_usuario(con, nombre, email)` inserta **con parámetros**, hace `commit` y devuelve el `id` nuevo.
4. `buscar_usuario(con, nombre)` → tupla `(id, nombre, email)` o `None`, con consulta **parametrizada** (resistente a `' OR '1'='1`).
5. `columna_orden(campo)` → devuelve `campo` si está en la allowlist `{"id", "nombre", "email"}`; si no, lanza `ValueError`.

Corrige con: `python corregir.py 09 facil`
