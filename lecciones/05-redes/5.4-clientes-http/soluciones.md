# 5.4 · Soluciones explicadas

## Ejercicio 1 · El portero exigente

```python
r = requests.get(f"{base_url}/estado", headers={"User-Agent": AGENTE}, timeout=5)
if not r.ok:
    return (r.status_code, False)
return (r.status_code, bool(r.json().get("ok", False)))
```

- "Presentarse con un identificador" es la cabecera **`User-Agent`**. Sin ella, `requests` manda `python-requests/x.y` y el servidor responde 403.
- Se mira `r.ok` **antes** de `r.json()`: una respuesta de error puede no traer JSON.
- Ojo: el `User-Agent` lo escribe el cliente, así que no es seguridad real. Sirve para identificar, no para autenticar.

## Ejercicio 2 · Entrar una vez, preguntar muchas

```python
with requests.Session() as s:
    r = s.post(f"{base_url}/login", json={"usuario": usuario, "clave": clave}, timeout=5)
    if r.status_code != 200:
        return None
    r = s.get(f"{base_url}/tickets", timeout=5)
    return sorted(t["titulo"] for t in r.json() if t["estado"] == "abierto")
```

- "Demostrar que eres la misma persona" es devolver la **cookie** que el servidor puso en `Set-Cookie`. Una `Session` lo hace sola. Con dos `requests.get` sueltos, el segundo llega sin cookie y el servidor responde 401.
- `json=` serializa el diccionario y pone el `Content-Type` correcto. Con `data=` sería un formulario, y este servidor no lo acepta.

## Ejercicio 3 · El archivo que a veces no está

```python
for _ in range(intentos):
    r = requests.get(f"{base_url}{ruta}", auth=(usuario, clave), timeout=5)
    if r.status_code == 200:
        return r.text
    if r.status_code != 503:
        return None
return None
```

- "El modo más simple que define HTTP" es la **autenticación básica**: `auth=(usuario, clave)`.
- Solo se reintenta ante **503** (servicio no disponible, temporal). Reintentar un **401** no sirve, porque la contraseña no va a volverse correcta, y además en un servidor real parecería fuerza bruta.
- `timeout=5` en cada intento es el "límite de espera".
- En un script real se espera un poco entre intentos, cada vez más (*backoff* exponencial: 1 s, 2 s, 4 s…) para no saturar más al servidor.
