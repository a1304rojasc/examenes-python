# 5.6 · DNS y resolución de nombres

## El caso: el correo que dice venir de la universidad

Llega un correo de `soporte@utec-campus.example` pidiendo "verificar tu cuenta". Antes de abrir nada, preguntas al DNS qué sabe de ese dominio:

```python
import dns.resolver

for tipo in ("A", "MX", "TXT"):
    try:
        respuesta = dns.resolver.resolve("example.com", tipo, lifetime=5)
        for r in respuesta:
            print(tipo, r.to_text())
    except dns.resolver.NoAnswer:
        print(tipo, "— sin registros")
```

Una salida típica (las IP de `example.com` cambian con el tiempo, así que las tuyas pueden ser otras):

```
A    <una o varias IPv4>
MX   0 .
TXT  "v=spf1 -all"
```

Leído en voz alta: `example.com` tiene IPs, **no recibe correo** (`MX 0 .` es el "null MX") y su SPF (`v=spf1 -all`) dice que **ningún servidor está autorizado a enviar correo en su nombre**. Si te llega un correo "de" ese dominio, es falso. El DNS es la guía telefónica de internet, y también un registro público de la política de cada dominio.

## La teoría

### Qué hace el DNS

Traduce nombres a datos. Cuando escribes `example.com`, tu sistema pregunta a un **resolvedor** (el de tu router, tu ISP o 1.1.1.1), que pregunta a los servidores raíz, luego a los de `.com` y por último a los **servidores autoritativos** de `example.com`. La respuesta se guarda en caché durante su **TTL** (en segundos).

### Tipos de registro que más vas a ver

| Tipo | Qué guarda | Ejemplo |
|---|---|---|
| A | IPv4 | `192.0.2.80` |
| AAAA | IPv6 | `2001:db8::80` |
| CNAME | Alias de otro nombre | `www → example.com.` |
| MX | Servidor de correo, con prioridad (menor = preferido) | `10 mail.example.com.` |
| TXT | Texto libre: SPF, verificación de dominios | `"v=spf1 include:_spf.example.com -all"` |
| NS | Servidores autoritativos de la zona | `a.iana-servers.net.` |
| PTR | Inverso: IP → nombre | `8.8.8.8.in-addr.arpa → dns.google.` |

### Dos formas de resolver en Python

**1. La del sistema operativo, `socket.getaddrinfo`.** Usa la misma configuración que el resto de programas (`/etc/hosts`, el resolvedor del sistema). Solo da direcciones, no MX ni TXT:

```python
import socket
{info[4][0] for info in socket.getaddrinfo("localhost", None)}
# {'127.0.0.1', '::1'}
```

**2. `dnspython`, cuando necesitas cualquier tipo de registro** o hablar con un servidor DNS concreto:

```python
import dns.resolver, dns.reversename

dns.resolver.resolve("example.com", "MX", lifetime=5)
dns.resolver.resolve(dns.reversename.from_address("8.8.8.8"), "PTR")  # dns.google.
```

`dnspython` también entiende el formato binario de los mensajes DNS (`dns.message.from_wire`) y los archivos de zona (`dns.zone.from_text`), así que puedes analizar tráfico capturado o configuraciones **sin hacer ninguna consulta**.

### Por qué le importa a seguridad

- **SPF** (TXT que empieza por `v=spf1`): qué servidores pueden enviar correo del dominio. Termina en `-all` (rechazar el resto), `~all` (marcar como sospechoso) o `+all` (**permitir a cualquiera**, un error grave).
- **Phishing y typosquatting:** un dominio parecido recién creado y sin MX ni SPF es una mala señal.
- **Exfiltración por DNS:** el malware a veces esconde datos en subdominios larguísimos (`aGVsbG8.evil.example`). Nombres anormalmente largos o con mucha entropía merecen una mirada.
- **Reconocimiento:** los registros DNS son públicos. Antes de un pentest autorizado, son lo primero que se mira.

### Ética y alcance

Consultar registros públicos es legal y normal, pero no automatices miles de consultas contra servidores ajenos. Para practicar usa `localhost` y dominios reservados para documentación: `example.com`, `example.org` y `*.example`.

## Ejercicios

Están en `ejercicios.py`. Los tests no hacen consultas a internet: usan `localhost`, mensajes DNS construidos en memoria y un archivo de zona de ejemplo.

```bash
pytest lecciones/05-redes/5.6-dns             # tu código
pytest lecciones/05-redes/5.6-dns --solucion  # la solución oficial
```

1. **El inventario del laboratorio.** El administrador te pasa una lista de nombres de máquinas y quiere saber a qué direcciones IPv4 apunta cada una según la configuración del propio equipo (la misma que usa el navegador). Escribe `direcciones_ipv4(nombres)` que devuelva un diccionario `{nombre: lista ordenada de IPv4 sin repetir}`. Si un nombre no existe, su lista queda vacía en vez de detener el programa.

2. **Leer la respuesta grabada.** En una captura de tráfico encontraste la respuesta de un servidor DNS, tal como viajó por la red: una secuencia de bytes. Escribe `registros(respuesta_binaria)` que devuelva la lista de tuplas `(nombre, tipo, valor, ttl)` de la sección de respuestas, con el nombre sin el punto final, el tipo como texto (`"A"`, `"MX"`...) y el valor como texto. Ordénala para que el resultado no dependa del orden en que llegaron.

3. **La política de correo de un dominio.** Te dan el contenido de un archivo de zona y su dominio de origen. Escribe `politica_correo(texto_zona, origen)` que devuelva un diccionario con:
   - `"mx"`: los servidores de correo del dominio (sin punto final), del más preferido al menos preferido;
   - `"spf"`: el texto de la política de remitentes autorizados (el registro de texto que empieza por `v=spf1`), o `None` si no hay;
   - `"riesgo"`: `"alto"` si no hay política o si la política permite enviar a cualquiera (`+all`); `"medio"` si solo marca como sospechoso (`~all` o `?all`); `"bajo"` si rechaza al resto (`-all`).
