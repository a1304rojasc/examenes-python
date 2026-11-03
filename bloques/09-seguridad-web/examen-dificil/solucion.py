"""Bloque 09 · Examen difícil — soluciones comentadas."""
import hashlib
import hmac
import re
import secrets

ITERACIONES = 10_000
ORDEN_PERMITIDO = {"nombre", "precio", "id"}
PATRON_SQLI = re.compile(r"'\s*(or|and)\b|--|;|/\*|\bunion\b.*\bselect\b", re.IGNORECASE)
PATRON_USUARIO = re.compile(r"[a-z0-9_]{3,16}")
PATRON_EMAIL = re.compile(r"[^@\s]+@[^@\s]+\.[A-Za-z]{2,}")
# Hash "señuelo" para que login tarde lo mismo aunque el usuario no exista.
_HASH_FALSO = "pbkdf2_sha256$10000$" + "00" * 16 + "$" + "00" * 32


def _hash(password, sal, iteraciones=ITERACIONES):
    derivada = hashlib.pbkdf2_hmac("sha256", password.encode(), sal, iteraciones)
    return f"pbkdf2_sha256${iteraciones}${sal.hex()}${derivada.hex()}"


def registrar(con, nombre, password):
    """Guarda el usuario con hash PBKDF2-SHA256 y sal aleatoria."""
    con.execute("INSERT INTO usuarios (nombre, hash) VALUES (?, ?)",
                (nombre, _hash(password, secrets.token_bytes(16))))
    con.commit()


def login(con, nombre, password):
    """True si las credenciales son correctas. No revela si el usuario existe."""
    fila = con.execute("SELECT hash FROM usuarios WHERE nombre = ?", (nombre,)).fetchone()
    almacenado = fila[0] if fila else _HASH_FALSO
    _, iteraciones, sal_hex, _ = almacenado.split("$")
    recalculado = _hash(password, bytes.fromhex(sal_hex), int(iteraciones))
    # Se calcula siempre el hash (mismo tiempo) y se compara en tiempo constante.
    return hmac.compare_digest(recalculado, almacenado) and fila is not None


def buscar_productos(con, texto, orden="nombre", limite=10):
    """Productos cuyo nombre contiene texto, con orden (allowlist) y límite 1-100."""
    if orden not in ORDEN_PERMITIDO:
        raise ValueError("orden no permitido")
    if not isinstance(limite, int) or isinstance(limite, bool) or not 1 <= limite <= 100:
        raise ValueError("límite fuera de rango")
    # Escapar los comodines de LIKE (\ primero) para que se busquen literalmente.
    seguro = texto.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_")
    sql = (f"SELECT id, nombre, precio FROM productos WHERE nombre LIKE ? ESCAPE '\\' "
           f"ORDER BY {orden}, id LIMIT ?")   # 'orden' ya está validado por allowlist
    return con.execute(sql, (f"%{seguro}%", limite)).fetchall()


def parece_sqli(entrada):
    """True si la entrada contiene patrones típicos de SQLi (solo para alertas)."""
    return PATRON_SQLI.search(entrada) is not None


def validar_formulario(datos):
    """{campo: mensaje} con los errores de usuario, email y edad (vacío si todo OK)."""
    errores = {}
    usuario = datos.get("usuario")
    if not isinstance(usuario, str) or not PATRON_USUARIO.fullmatch(usuario):
        errores["usuario"] = "Usuario: 3-16 caracteres a-z, 0-9 o _"
    email = datos.get("email")
    if not isinstance(email, str) or not PATRON_EMAIL.fullmatch(email):
        errores["email"] = "Email no válido"
    try:
        edad = int(str(datos.get("edad")).strip())
        if not 18 <= edad <= 120:
            raise ValueError
    except ValueError:
        errores["edad"] = "La edad debe ser un número entre 18 y 120"
    return errores


def generar_token_csrf():
    """Token aleatorio URL-safe con 32 bytes de entropía."""
    return secrets.token_urlsafe(32)


def verificar_csrf(token_sesion, token_enviado):
    """True si ambos tokens existen y coinciden (comparación en tiempo constante)."""
    if not token_sesion or not token_enviado:
        return False
    return hmac.compare_digest(token_sesion, token_enviado)
