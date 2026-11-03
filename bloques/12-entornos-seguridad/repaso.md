# Bloque 12 · Python en entornos de seguridad — Repaso espaciado

> Mezcla 12.1 Kali/permisos · 12.2 Metasploit · 12.3 CTF/pwntools · 12.4 SOC/SIEM.
> Todo es **local y con datos de ejemplo**: se parsean resultados y se resuelven retos tipo CTF; no se explota ningún sistema.

**1. (12.1) ¿Por qué muchas herramientas de red necesitan privilegios de root y qué puertos se consideran privilegiados?**
Abrir sockets en bruto (raw) o enlazar servicios en puertos por debajo de 1024 requiere privilegios de administrador en sistemas tipo Unix. Por eso herramientas de captura o que escuchan en puertos bajos piden `sudo`.

**2. (12.3) En un reto CTF, un texto está cifrado con XOR usando una clave de un byte. ¿Por qué se puede romper probando las 256 claves posibles?**
Porque el espacio de claves es diminuto (256). Se prueban todas, se descifra con cada una y se elige la que produce texto legible o que contiene una pista conocida (p. ej. `FLAG{`). Es fuerza bruta trivial por lo pequeño del espacio.

**3. (12.2 + 12.4) Al automatizar una herramienta (Metasploit) o un SIEM, ¿por qué el valor está en parsear y correlacionar su salida en vez de solo lanzarla?**
Porque la información útil está en los resultados: qué servicios hay, qué eventos se repiten, qué IPs concentran actividad. Parsear y correlacionar convierte texto crudo en hallazgos accionables (alertas, informes), que es el trabajo real del analista.

**4. (12.4) En un SOC, ¿qué es correlacionar eventos y por qué una ventana de tiempo es clave para detectar un ataque de fuerza bruta?**
Correlacionar es relacionar eventos individuales para ver un patrón (muchos logins fallidos de una IP). La ventana de tiempo distingue "5 fallos en 30 segundos" (ataque) de "5 fallos en una semana" (despistes normales).

**5. (12.1 + 12.3) ¿Por qué se practican estas técnicas solo en laboratorios propios, CTF o con permiso, y nunca contra sistemas de terceros?**
Porque usar exploits o escaneos contra sistemas ajenos sin autorización es ilegal y dañino. Los entornos de CTF y los laboratorios propios están pensados para practicar legalmente; fuera de ellos hace falta un contrato y un alcance autorizados.
