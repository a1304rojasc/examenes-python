# 5.5 · Soluciones explicadas

## Ejercicio 1 · Tocar la puerta sin entrar

```python
return IP(dst=ip_destino) / TCP(sport=puerto_origen, dport=puerto, flags="S")
```

- "Quiero conectarme, sin confirmar nada" es el **SYN**, el primer paso del *three-way handshake* (SYN → SYN-ACK → ACK).
- Si el puerto está abierto, el servidor responde **SYN-ACK**; si está cerrado, **RST**. Así funciona el escaneo "SYN" de nmap (`-sS`).
- No hace falta capa `Ether`: si se envía con `send()`, el sistema operativo pone la de enlace.

## Ejercicio 2 · Desarmar el sobre

```python
p = Ether(trama)
[capa.__name__ for capa in p.layers()]
bytes(p[Raw].load) if p.haslayer(Raw) else b""
```

- Como los bytes vienen "del cable Ethernet", la disección empieza en `Ether(...)`. Scapy mira el campo *EtherType* (0x0800 = IPv4) para saber que lo siguiente es IP, el campo *protocol* de IP (6 = TCP) para saber que sigue TCP, etc.
- Si empezaras con `IP(trama)`, interpretaría las direcciones MAC como si fueran la cabecera IP: todo saldría mal.

## Ejercicio 3 · El que toca todas las puertas

```python
puertos = defaultdict(set)
for p in rdpcap(str(ruta)):
    if p.haslayer(IP) and p.haslayer(TCP) and p[TCP].flags == "S":
        puertos[p[IP].src].add(p[TCP].dport)
return {ip: len(ps) for ip, ps in puertos.items() if len(ps) >= umbral}
```

- `flags == "S"` exige **solo** SYN. Un `"SA"` (SYN-ACK) es la respuesta de un servidor, no un intento de conexión: contarlo culparía a los servidores que contestan.
- Se usa un **conjunto** de puertos: diez SYN repetidos al puerto 443 son reintentos de un cliente normal, no un escaneo. Lo que delata el escaneo es la *variedad* de puertos.
- Es la misma idea que Centinela aplica a los logs de SSH, pero con paquetes.
