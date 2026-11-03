# Bloque 9 · Análisis de vulnerabilidades web — Repaso espaciado

> Mezcla 9.1 SQL Injection · 9.2 XSS · 9.3 SSRF y redirecciones abiertas · 9.4 Parsing de HTML.
> Enfoque **defensivo**: detectar, validar y corregir. Datos de ejemplo y SQLite en memoria; no se ataca ningún sitio.

**1. (9.1) ¿Por qué una consulta parametrizada frena una inyección SQL que la concatenación de cadenas no detiene?**
Porque los parámetros viajan separados del texto SQL: la base de datos trata el valor como **dato**, nunca como código. Concatenar mezcla la entrada del usuario con la sentencia, y un valor como `' OR '1'='1` cambia su significado.

**2. (9.2) El mismo texto del usuario se muestra en una página. ¿Por qué escapar la salida evita el XSS y por qué validar solo en el navegador no basta?**
Escapar convierte `<`, `>`, `"`… en entidades, así el navegador lo muestra como texto y no lo ejecuta. Validar en el navegador no basta porque el atacante puede enviar la petición saltándose el cliente; la defensa debe estar en el servidor.

**3. (9.3) ¿Qué es un SSRF y por qué `http://169.254.169.254/` o `http://127.0.0.1/` son destinos peligrosos si el servidor sigue una URL que da el usuario?**
SSRF es lograr que **el servidor** haga peticiones a destinos elegidos por el atacante. Esas direcciones internas (loopback, metadatos de la nube) no son accesibles desde fuera, pero el servidor sí las alcanza, pudiendo filtrar credenciales o servicios internos.

**4. (9.1 + 9.2) Un filtro que busca patrones de ataque (tipo WAF) ¿puede sustituir a las consultas parametrizadas y al escape de salida?**
No. Los filtros se evaden con codificaciones y variantes, y dan falsos positivos. Sirven como capa extra de alerta, pero la defensa real es parametrizar las consultas y escapar la salida: eliminan el problema de raíz.

**5. (9.3 + 9.4) En una redirección tras el login, ¿por qué hay que validar la URL de destino y qué trucos intentan saltarse el filtro?**
Si no se valida, un atacante redirige a la víctima a un sitio malicioso (redirección abierta). Hay que comprobar que el destino queda dentro del dominio permitido; los trucos típicos son `//otro.com`, `https://otro.com`, `/\otro.com` o usar `usuario@otro.com` en la parte de host.
