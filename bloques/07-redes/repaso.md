# Bloque 07 · Redes — Repaso

**1. ¿Qué significa `192.0.2.0/24`?**
Notación CIDR: los primeros 24 bits son la red (máscara `255.255.255.0`); quedan 8 bits para hosts → 256 direcciones, 254 usables.

**2. ¿Qué hace el módulo `ipaddress`?**
Valida y opera con IPs y redes: `ip_address("192.0.2.1")`, `ip_network("192.0.2.0/24")`, `ip in red`, `.hosts()`, `.broadcast_address`.

**3. ¿TCP o UDP?**
TCP es orientado a conexión y fiable (SSH, HTTP); UDP no garantiza entrega pero es más ligero (DNS, streaming).

**4. ¿Qué es un socket?**
Un extremo de comunicación (IP + puerto). En Python: `socket.socket(AF_INET, SOCK_STREAM)` para TCP; `connect`, `sendall`, `recv`, `close`.

**5. ¿Cómo es una petición HTTP?**
Texto: una línea `METODO RUTA VERSION`, cabeceras `Nombre: valor`, una línea vacía (`\r\n\r\n`) y el cuerpo opcional.

> Ética: solo se escanea/prueba lo que es tuyo o tienes permiso escrito para probar. Aquí todo es `127.0.0.1` o IPs de documentación (`192.0.2.0/24`, `198.51.100.0/24`, `203.0.113.0/24`).
