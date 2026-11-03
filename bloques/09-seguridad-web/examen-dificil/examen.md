# Bloque 09 · Seguridad web — Examen difícil

Combina bloques anteriores (regex, excepciones, criptografía con `hashlib`/`hmac`/`secrets`) con seguridad web. SQLite en memoria.

## Parte A — Teoría (10 preguntas)

1. En una búsqueda `LIKE`, ¿por qué hay que escapar `%` y `_` aunque la consulta esté parametrizada?
2. ¿Por qué un mensaje de login "usuario no existe" vs "contraseña incorrecta" es una fuga de información?
3. ¿Qué es *second-order SQL injection*?
4. ¿Por qué un detector de patrones SQLi (tipo WAF) **no** sustituye a las consultas parametrizadas?
5. ¿Qué es un ataque CSRF y cómo lo frena un token anti-CSRF?
6. ¿Por qué el token CSRF debe generarse con `secrets` y compararse con `hmac.compare_digest`?
7. ¿Qué hace la cabecera `Content-Security-Policy`? ¿Y `HttpOnly` en una cookie?
8. ¿Por qué limitar el tamaño de `LIMIT`/paginación es una medida de seguridad?
9. Devolver todos los errores de validación a la vez o solo el primero: ¿qué es mejor para el usuario y qué cuidado hay que tener con lo que se revela?
10. ¿Qué es OWASP Top 10 y en qué categoría entran la inyección SQL y el XSS?

## Parte B — Código (5 ejercicios)

Las tablas las crean los tests: `usuarios(nombre TEXT PRIMARY KEY, hash TEXT NOT NULL)` y `productos(id INTEGER PRIMARY KEY, nombre TEXT, precio REAL)`.

1. `registrar(con, nombre, password)` guarda el usuario con un hash PBKDF2-SHA256 con sal (`"pbkdf2_sha256$iter$sal_hex$hash_hex"`, 10 000 iteraciones). `login(con, nombre, password)` → `True`/`False`; mismo resultado si el usuario no existe que si la contraseña es incorrecta.
2. `buscar_productos(con, texto, orden="nombre", limite=10)` → lista de tuplas `(id, nombre, precio)` cuyo nombre **contiene** `texto` (sin interpretar `%` ni `_` del usuario), ordenada por la columna `orden` (allowlist `nombre`, `precio`, `id`; si no, `ValueError`) y con `limite` entero entre 1 y 100 (si no, `ValueError`).
3. `parece_sqli(entrada)` → `True` si la entrada contiene patrones típicos: comilla simple seguida de `OR`/`AND`, `--`, `;`, `/*`, o `UNION ... SELECT` (sin distinguir mayúsculas). **Solo para alertas**, no como defensa.
4. `validar_formulario(datos)` → dict `{campo: mensaje}` con los errores (vacío si todo es correcto): `usuario` (3–16 de `[a-z0-9_]`), `email` (`algo@dominio.tld`), `edad` (entero de 18 a 120, puede venir como texto). Campo ausente = error.
5. `generar_token_csrf()` → token aleatorio URL-safe de al menos 32 bytes de entropía. `verificar_csrf(token_sesion, token_enviado)` → `bool`; `False` si alguno es `None` o vacío.

Corrige con: `python corregir.py 09 dificil`
