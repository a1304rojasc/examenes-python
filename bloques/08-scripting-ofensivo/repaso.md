# Bloque 8 · Scripting ofensivo (enfoque defensivo) — Repaso espaciado

> Mezcla 8.1 Reconocimiento · 8.2 Escáneres de puertos · 8.3 Fuerza bruta · 8.4 Fuzzing · 8.5 Scraping · 8.6 APIs.
> **Ética:** solo se practica sobre sistemas propios o con permiso explícito. Aquí todo es **análisis de datos de ejemplo y pruebas locales** (`127.0.0.1`, `example.com`, IPs de documentación); nada ataca sistemas reales.

**1. (8.1 + 8.5) Al recopilar información pública (recon) y al hacer scraping, ¿por qué conviene respetar `robots.txt` y limitar la frecuencia de peticiones?**
Porque es información de terceros: respetar `robots.txt` y espaciar las peticiones evita sobrecargar el servidor (una especie de DoS involuntario), reduce el riesgo legal y es la práctica profesional correcta. El recon legítimo es discreto y respetuoso.

**2. (8.3) Una contraseña de 6 caracteres en minúsculas y otra de 12 con mayúsculas, dígitos y símbolos. ¿Por qué la segunda es astronómicamente más costosa de adivinar por fuerza bruta?**
El coste crece como (tamaño del alfabeto)^(longitud). Más longitud y un alfabeto mayor disparan el número de combinaciones; cada carácter extra multiplica el total, así que 12 con alfabeto grande supera por muchísimos órdenes de magnitud a 6 en minúsculas.

**3. (8.2 + 8.3) Como defensor, ¿qué señales delatan un escaneo de puertos o un ataque de fuerza bruta en tus propios registros?**
Un escaneo: muchas conexiones a puertos distintos desde una misma IP en poco tiempo. Fuerza bruta: muchos intentos de autenticación fallidos contra un mismo servicio/usuario en una ventana corta. Ambos se detectan agregando por IP y ventana de tiempo.

**4. (8.4) ¿Qué es el fuzzing y por qué es una técnica tanto ofensiva como de aseguramiento de calidad?**
Consiste en alimentar un programa con entradas inesperadas o malformadas para provocar fallos. Ofensivamente busca vulnerabilidades; defensivamente, se usa sobre el propio software para encontrar y corregir esos fallos antes de publicarlo.

**5. (8.6) Al revisar una API, ¿por qué un endpoint que modifica datos (POST/PUT/DELETE) sin exigir autenticación es un hallazgo grave?**
Porque permitiría a cualquiera cambiar o borrar información sin credenciales. Las operaciones de escritura deben requerir autenticación y autorización; encontrarlas abiertas es una vulnerabilidad de control de acceso que hay que reportar y cerrar.
