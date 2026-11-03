# Bloque 07 · Redes — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Cuántos bits tiene una dirección IPv4?
2. ¿Cuántas direcciones totales tiene una red `/24`? ¿Cuántas usables para hosts?
3. ¿Qué máscara corresponde a `/16`?
4. ¿Qué puerto usa por defecto SSH? ¿Y HTTPS?
5. ¿Qué excepción lanza `ipaddress.ip_address("300.1.1.1")`?
6. ¿Qué es `127.0.0.1`?
7. ¿Qué protocolo de transporte usa HTTP/1.1? a) UDP b) TCP c) ICMP
8. ¿Qué dos argumentos de `socket.socket(...)` crean un socket TCP IPv4?
9. ¿Qué significa un código HTTP 404? ¿Y 500?
10. ¿Para qué están reservados los rangos `192.0.2.0/24`, `198.51.100.0/24` y `203.0.113.0/24`?

## Parte B — Código (5 ejercicios)

1. `es_ip_valida(texto)` → `True` si es una IPv4 o IPv6 válida (usa `ipaddress` y captura `ValueError`).
2. `en_red(ip, cidr)` → `True` si la IP pertenece a la red.
3. `info_red(cidr)` → dict con `"red"`, `"broadcast"`, `"mascara"` (cadenas) y `"hosts"` (nº de hosts usables). Acepta CIDR con bits de host (`"192.0.2.77/24"`).
4. `eco_socketpair(mensaje)` → crea un par de sockets conectados con `socket.socketpair()`, envía el mensaje (texto) por uno, lo recibe por el otro y devuelve el texto recibido. Cierra ambos sockets.
5. `parsear_url(url)` → tupla `(esquema, host, puerto)` con `urllib.parse`. Si no hay puerto explícito usa 80 para `http` y 443 para `https`.

Corrige con: `python corregir.py 07 facil`
