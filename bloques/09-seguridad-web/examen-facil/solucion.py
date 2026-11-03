"""Bloque 09 · Examen fácil — soluciones comentadas."""
import html
import re

COLUMNAS_PERMITIDAS = {"id", "nombre", "email"}


def validar_usuario(nombre):
    """True si nombre tiene 3-16 caracteres de [a-z0-9_]."""
    # fullmatch: TODO el texto debe encajar (no basta con una parte).
    return re.fullmatch(r"[a-z0-9_]{3,16}", nombre) is not None


def escapar_html(texto):
    """Escapa &, <, >, " y ' para insertar texto en HTML de forma segura."""
    return html.escape(texto, quote=True)


def crear_tabla(con):
    """Crea la tabla usuarios(id, nombre UNIQUE NOT NULL, email)."""
    con.execute(
        "CREATE TABLE IF NOT EXISTS usuarios ("
        " id INTEGER PRIMARY KEY,"
        " nombre TEXT UNIQUE NOT NULL,"
        " email TEXT)"
    )
    con.commit()


def insertar_usuario(con, nombre, email):
    """Inserta un usuario con parámetros, hace commit y devuelve su id."""
    # Los ? se rellenan con la tupla: los datos NUNCA se mezclan con el SQL.
    cur = con.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
    con.commit()
    return cur.lastrowid


def buscar_usuario(con, nombre):
    """(id, nombre, email) del usuario o None. Consulta parametrizada."""
    cur = con.execute("SELECT id, nombre, email FROM usuarios WHERE nombre = ?", (nombre,))
    return cur.fetchone()


def columna_orden(campo):
    """Devuelve campo si está en la allowlist; si no, ValueError."""
    # Los identificadores (columnas, ORDER BY) no se pueden parametrizar:
    # se comparan contra una lista cerrada de valores permitidos.
    if campo not in COLUMNAS_PERMITIDAS:
        raise ValueError(f"columna no permitida: {campo!r}")
    return campo
