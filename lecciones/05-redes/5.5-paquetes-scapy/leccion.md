# 5.5 · Paquetes con Scapy (fundamentos)

## El caso: ¿quién está tocando todas las puertas?

El servidor del laboratorio va lento. Alguien grabó cinco minutos de tráfico en un archivo `captura.pcap` y te lo pasa. Con Wireshark podrías mirarlo paquete a paquete, pero son 40 000. Con Python:

```python
from collections import Counter
from scapy.all import rdpcap, IP, TCP

paquetes = rdpcap("captura.pcap")                  # lee el archivo, no la red
syn = Counter()
for p in paquetes:
    if p.haslayer(TCP) and p[TCP].flags == "S":    # SYN sin ACK: "¿estás abierto?"
        syn[p[IP].src] += 1

print(syn.most_common(3))
# [('198.51.100.7', 1012), ('192.168.1.20', 4), ('192.168.1.31', 2)]
```

Una IP que manda más de mil SYN a puertos distintos no está navegando: está **escaneando puertos**. En tres líneas pasaste de un archivo binario a un sospechoso.

## La teoría

### Un paquete son capas apiladas

Cada protocolo envuelve al siguiente, como sobres dentro de sobres:

```
Ether  (MAC origen/destino)          capa 2: enlace
└─ IP  (IP origen/destino, TTL)      capa 3: red
   └─ TCP (puertos, flags, seq)      capa 4: transporte
      └─ Raw (los datos: "GET / ...") capa 7: aplicación
```

En Scapy, el operador `/` apila capas, y los campos que no rellenas toman valores por defecto razonables:

```python
from scapy.all import Ether, IP, TCP, UDP, ICMP, Raw

p = IP(dst="127.0.0.1") / TCP(dport=22, flags="S")
p.show()            # todos los campos, capa por capa
p.summary()         # 'IP / TCP 127.0.0.1:ftp_data > 127.0.0.1:ssh S'
bytes(p)            # los bytes reales que viajarían por el cable
```

### Leer y preguntar a un paquete

```python
p.haslayer(TCP)     # ¿tiene esta capa?
p[TCP].dport        # acceder a un campo de una capa
p[IP].src
p.layers()          # [IP, TCP]
IP(bytes(p))        # reconstruir el paquete a partir de bytes (disección)
Ether(datos)        # lo mismo, empezando desde la capa de enlace
```

Las **flags TCP** se comparan como texto: `"S"` (SYN), `"SA"` (SYN+ACK), `"A"` (ACK), `"R"` (RST), `"F"` (FIN), `"PA"` (PSH+ACK, datos).

> **Trampa:** al convertir a bytes un `Ether()` sin direcciones MAC, Scapy intenta averiguar la MAC de destino preguntando por ARP en la red, y puede quedarse esperando. Si solo quieres construir tramas en memoria, dale las MAC: `Ether(src="02:00:00:00:00:01", dst="02:00:00:00:00:02")`.

### Capturar, enviar y leer archivos

| Qué | Función | ¿Requiere root? |
|---|---|---|
| Leer una captura | `rdpcap("x.pcap")` | No |
| Guardar paquetes | `wrpcap("x.pcap", lista)` | No |
| Capturar en vivo | `sniff(iface="lo", count=10, filter="tcp port 8000")` | Sí |
| Enviar (capa 3) | `send(p)` | Sí |
| Enviar y esperar respuesta | `sr1(p, timeout=2)` | Sí |

Capturar y enviar paquetes "a mano" abre un *raw socket*, y eso requiere privilegios de administrador. Por eso los ejercicios de esta lección trabajan con paquetes construidos en memoria y archivos `.pcap`.

### Ética y alcance

Enviar paquetes fabricados a redes ajenas (escanear, falsificar la IP de origen) puede ser ilegal aunque "solo sea una prueba". Practica solo contra `127.0.0.1` y tus propias máquinas virtuales. Si quieres probar `sr1` con permisos de root, hazlo contra tu propia máquina:

```python
# sudo python3   (solo en tu máquina)
sr1(IP(dst="127.0.0.1") / ICMP(), timeout=2)
```

## Ejercicios

Están en `ejercicios.py`. Los tests no necesitan root ni red.

```bash
pytest lecciones/05-redes/5.5-paquetes-scapy             # tu código
pytest lecciones/05-redes/5.5-paquetes-scapy --solucion  # la solución oficial
```

1. **Tocar la puerta sin entrar.** Para comprobar si un servicio escucha, la primera señal que se manda en una conexión TCP es "quiero conectarme", sin datos y sin confirmar nada. Escribe `construir_sonda(ip_destino, puerto, puerto_origen=40000)` que devuelva ese primer paquete, listo para enviarse: dirección de destino, puerto de destino y de origen, y solo la señal de inicio de conexión activa.

2. **Desarmar el sobre.** Te pasan un trozo de tráfico tal como llegó por el cable Ethernet: una secuencia de bytes. Escribe `capas(trama)` que devuelva la lista de nombres de los protocolos que contiene, desde el exterior hacia dentro (por ejemplo `["Ether", "IP", "TCP", "Raw"]`). Escribe también `datos_de_aplicacion(trama)` que devuelva los bytes del contenido de la aplicación, o `b""` si no hay.

3. **El que toca todas las puertas.** Te dan la ruta de un archivo de captura. Un escaneo de puertos se reconoce porque la misma IP de origen intenta iniciar conexiones (primera señal, sin confirmación) hacia muchos puertos distintos de destino. Escribe `sospechosos_de_escaneo(ruta, umbral=10)` que devuelva un diccionario `{ip_origen: número de puertos distintos}` solo con las IPs que intentaron iniciar conexión con **al menos** `umbral` puertos distintos.
