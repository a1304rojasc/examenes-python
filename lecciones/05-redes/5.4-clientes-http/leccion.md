# 5.4 · Clientes HTTP con `requests` y `httpx`

## El caso: el panel de tickets

Tu equipo tiene un panel interno de incidencias. Cada mañana alguien entra, inicia sesión y copia a mano los tickets abiertos en un informe. Quieres automatizarlo:

1. Comprobar que el panel está vivo.
2. Iniciar sesión con usuario y contraseña.
3. Pedir la lista de tickets usando la sesión que te dio el login.

Con el navegador haces esos tres pasos sin pensar. Con Python, cada uno es una petición HTTP:

```python
import requests

BASE = "http://127.0.0.1:8000"

with requests.Session() as s:                       # guarda las cookies entre peticiones
    r = s.get(f"{BASE}/estado", timeout=5)
    r.raise_for_status()                            # lanza error si es 4xx/5xx

    r = s.post(f"{BASE}/login", json={"usuario": "ana", "clave": "s3cr3ta"}, timeout=5)
    r.raise_for_status()                            # el servidor responde con Set-Cookie

    r = s.get(f"{BASE}/tickets", timeout=5)         # la cookie viaja sola
    for t in r.json():
        print(t["id"], t["titulo"])
```

Todo lo que sigue explica por qué cada línea está ahí.

## La teoría

### Una petición = método + URL + cabeceras + cuerpo

| Método | Para qué | En `requests` |
|---|---|---|
| GET | Leer | `requests.get(url, params={...})` |
| POST | Crear / enviar datos | `requests.post(url, json={...})` o `data={...}` |
| PUT | Reemplazar | `requests.put(url, json={...})` |
| DELETE | Borrar | `requests.delete(url)` |

- `params=` construye la query string (`?q=ssh&pagina=2`) y la escapa por ti.
- `json=` serializa el diccionario y pone `Content-Type: application/json`.
- `data=` envía un formulario (`application/x-www-form-urlencoded`).
- `headers={"User-Agent": "..."}` añade o sustituye cabeceras.

### La respuesta

```python
r.status_code        # 200, 401, 404, 503...
r.headers["Content-Type"]
r.text               # cuerpo como str
r.json()             # cuerpo como objeto Python (si es JSON)
r.ok                 # True si status_code < 400
r.raise_for_status() # lanza requests.HTTPError si no es ok
```

Los códigos importan para decidir qué hacer: **2xx** todo bien, **3xx** redirección, **401** faltan credenciales, **403** no tienes permiso, **404** no existe, **429** vas demasiado rápido, **5xx** el servidor falló (a veces vale la pena reintentar).

### Cookies y sesiones

HTTP no tiene memoria: cada petición es independiente. Para que el servidor "recuerde" que ya iniciaste sesión, te devuelve una cookie (`Set-Cookie: sesion=abc123`) y tú tienes que mandarla en cada petición siguiente. `requests.Session()` (o `httpx.Client()`) lo hace solo, y además reutiliza la conexión TCP, que es más rápido.

### Autenticación básica

`auth=("usuario", "clave")` envía la cabecera `Authorization: Basic dXN1YXJpbzpjbGF2ZQ==`. Eso es **Base64, no cifrado**: cualquiera que vea el tráfico lo decodifica. Solo es aceptable sobre HTTPS.

### `timeout` siempre

Sin `timeout`, una petición a un servidor que no responde puede quedarse colgada para siempre. Un script de monitorización colgado es peor que uno que falla. Pon siempre `timeout=`.

### `httpx`: casi la misma API, y además async

```python
import httpx

with httpx.Client(base_url=BASE, timeout=5) as c:
    c.get("/estado").raise_for_status()

# versión asíncrona, para muchas peticiones a la vez
async with httpx.AsyncClient(base_url=BASE, timeout=5) as c:
    r = await c.get("/estado")
```

Diferencias que muerden: `httpx` **no sigue redirecciones** por defecto (`follow_redirects=True`), y sus excepciones son `httpx.HTTPStatusError` y `httpx.RequestError`.

### Ética y alcance

Solo haz peticiones automáticas a servidores tuyos, a `127.0.0.1` o a servicios públicos pensados para pruebas, como `https://httpbin.org` o `https://example.com`. Lanzar miles de peticiones a un sitio ajeno puede ser un ataque de denegación de servicio aunque no lo pretendas.

```python
requests.get("https://httpbin.org/get", params={"curso": "python"}, timeout=5).json()
requests.get("https://httpbin.org/basic-auth/ana/s3cr3ta", auth=("ana", "s3cr3ta"), timeout=5).status_code  # 200
```

## Ejercicios

Están en `ejercicios.py`. Los tests levantan un servidor de prueba en `127.0.0.1`, así que no necesitas internet.

```bash
pytest lecciones/05-redes/5.4-clientes-http             # tu código
pytest lecciones/05-redes/5.4-clientes-http --solucion  # la solución oficial
```

1. **El portero exigente.** El servicio de monitorización de la facultad expone su salud en la ruta `/estado` de la dirección base que te dan. Responde un JSON como `{"servicio": "biblioteca", "ok": true}`, pero el administrador configuró el servidor para rechazar con 403 a cualquier cliente que no se presente con el identificador `monitor-utec/1.0`. Escribe `consultar_estado(base_url)` que devuelva una tupla `(codigo, ok)`: el código numérico de la respuesta y el valor de `ok` (o `False` si la respuesta no fue exitosa).

2. **Entrar una vez, preguntar muchas.** El panel de incidencias tiene una puerta `/login` que recibe un JSON `{"usuario": ..., "clave": ...}`. Si las credenciales son correctas, el servidor te "recuerda", pero solo si en las visitas siguientes le demuestras que eres la misma persona que entró. En `/tickets` devuelve la lista de incidencias (cada una con `id`, `titulo` y `estado`). Escribe `titulos_abiertos(base_url, usuario, clave)` que devuelva, ordenados alfabéticamente, los títulos de las incidencias con estado `"abierto"`. Si el login falla, devuelve `None`.

3. **El archivo que a veces no está.** El servidor de informes guarda el informe semanal en una ruta que te dan, protegido con usuario y contraseña enviados del modo más simple que define HTTP. El servidor está saturado: a veces responde 503 en lugar del informe. Escribe `descargar_informe(base_url, ruta, usuario, clave, intentos=3)` que devuelva el texto del informe. Si recibe 503, vuelve a intentarlo hasta agotar `intentos` en total. Si las credenciales son incorrectas (401), o se agotan los intentos, devuelve `None`. Cada intento debe tener un límite de espera para no quedarse colgado.
