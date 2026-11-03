# Bloque 07 · Examen difícil — Soluciones (teoría)

1. Como texto se compara carácter a carácter (`"1" < "9"`). Se ordena con `key=ipaddress.ip_address`.
2. **4** subredes `/26`, con **62** hosts usables cada una (64 − 2).
3. Devuelve un **código de error** (0 = éxito) en vez de lanzar excepción como `connect`.
4. Sin timeout, un host que no responde puede **bloquear** el programa indefinidamente.
5. El sistema operativo asigna un **puerto libre** cualquiera (se lee con `getsockname()`).
6. Con una **línea vacía** (`\r\n\r\n`). Los nombres de cabecera **no** distinguen mayúsculas.
7. El tamaño del cuerpo **en bytes**. Si no se valida (negativo, enorme, no coincide) puede causar agotamiento de memoria o *request smuggling*.
8. Lista de lo **permitido**; todo lo demás se deniega. Es más segura porque lo desconocido queda bloqueado por defecto.
9. `b""` significa que el otro extremo **cerró** la conexión; `timeout` que no llegaron datos en el tiempo fijado.
10. Puede constituir **acceso o intento de intrusión** según la legislación, dispara alertas y consume recursos ajenos. Solo con autorización explícita y por escrito.
