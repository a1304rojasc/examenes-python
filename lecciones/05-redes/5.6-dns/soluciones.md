# 5.6 · Soluciones explicadas

## Ejercicio 1 · El inventario del laboratorio

```python
try:
    infos = socket.getaddrinfo(nombre, None, family=socket.AF_INET)
except socket.gaierror:
    resultado[nombre] = []
    continue
resultado[nombre] = sorted({info[4][0] for info in infos})
```

- "La configuración del propio equipo, la misma que usa el navegador" es el resolvedor del sistema: **`socket.getaddrinfo`**. Respeta `/etc/hosts`, que es donde vive `localhost`.
- `family=socket.AF_INET` pide solo IPv4.
- `getaddrinfo` devuelve una entrada por cada combinación de tipo de socket (TCP, UDP…), así que la misma IP sale repetida: el **conjunto** quita los duplicados.
- Un nombre inexistente lanza `socket.gaierror`. Capturarlo es lo que permite seguir con el resto de la lista.

## Ejercicio 2 · Leer la respuesta grabada

```python
mensaje = dns.message.from_wire(respuesta_binaria)
for rrset in mensaje.answer:
    nombre = rrset.name.to_text(omit_final_dot=True)
    tipo = dns.rdatatype.to_text(rrset.rdtype)
    for rdata in rrset:
        filas.append((nombre, tipo, rdata.to_text(), rrset.ttl))
```

- "Tal como viajó por la red" es el **formato wire**: `dns.message.from_wire` lo decodifica sin hacer ninguna consulta.
- Una respuesta tiene cuatro secciones: *question*, *answer*, *authority* y *additional*. Solo nos piden *answer*.
- Un **RRset** agrupa los registros con el mismo nombre y tipo, y comparten TTL. Por eso el TTL se lee del `rrset` y el valor de cada `rdata`.
- Los nombres DNS terminan en un punto (`example.com.` es el nombre absoluto). `omit_final_dot=True` lo quita.

## Ejercicio 3 · La política de correo de un dominio

```python
zona = dns.zone.from_text(texto_zona, origin=origen, relativize=False)
raiz = zona.get_node(dns.name.from_text(origen))
conjunto_mx = raiz.get_rdataset(dns.rdataclass.IN, dns.rdatatype.MX)
mx = [r.exchange.to_text(omit_final_dot=True) for r in sorted(conjunto_mx, key=lambda r: r.preference)]
```

- Los **MX** se ordenan por `preference`: **menor número = más preferido**. Es un error común ordenarlos al revés.
- La política de remitentes autorizados es el **SPF**, que se publica como un registro **TXT** que empieza por `v=spf1`. Un TXT puede venir partido en varios trozos de hasta 255 bytes, por eso se unen con `b"".join(rdata.strings)`.
- El riesgo lo decide el último mecanismo, `all`:
  - `-all` (*fail*): rechazar a quien no esté en la lista → **bajo**;
  - `~all` (*softfail*) o `?all` (*neutral*): aceptar pero marcar → **medio**;
  - `+all` (*pass*), o no tener SPF: cualquiera puede suplantar el dominio → **alto**.
- En el mundo real se completa con **DMARC** (un TXT en `_dmarc.dominio`) y **DKIM**, que es lo que analiza el detector de phishing.
