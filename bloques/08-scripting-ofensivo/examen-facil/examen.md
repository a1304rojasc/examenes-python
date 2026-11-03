# Bloque 8 · Scripting ofensivo (enfoque defensivo) — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py`.
**Todo es local y con datos de ejemplo**: se analizan textos y resultados ya obtenidos; no se contacta ningún sistema real.
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué es la fase de reconocimiento (recon) en una evaluación de seguridad y qué distingue el recon pasivo del activo?
2. ¿Por qué el recon y el scraping responsables respetan `robots.txt` y limitan la frecuencia de peticiones?
3. ¿Qué información revela una consulta WHOIS y por qué es útil en una auditoría autorizada?
4. ¿Qué significa que un puerto esté "abierto", "cerrado" o "filtrado"?
5. ¿Por qué escanear puertos de un sistema sin autorización puede ser ilegal aunque "solo se mire"?
6. ¿Qué es un ataque de fuerza bruta y qué es un ataque de diccionario? ¿En qué se diferencian?
7. ¿Cómo influyen la longitud y el tamaño del alfabeto en el número de contraseñas posibles?
8. ¿Qué es "web scraping" y en qué se diferencia de "crawling"?
9. ¿Qué riesgos tiene ejecutar directamente un script de recon encontrado en internet sin leerlo?
10. ¿Por qué un pentester trabaja siempre con un alcance (scope) y una autorización por escrito?

## Parte B — Ejercicios (5 problemas)

1. Una auditoría autorizada guardó la salida de una consulta WHOIS como texto, con líneas del estilo `Clave: valor`. Escribe `extraer_campos_whois(texto)` que devuelva un registro con los campos `registrar`, `creation date` y `registry expiry date` (claves en minúsculas), tomando la primera aparición de cada uno e ignorando el resto.

2. Un inventario de activos parte del HTML de una página interna. Escribe `extraer_enlaces(html)` que devuelva, en orden de aparición, las direcciones de todos los enlaces (`href`) que contenga.

3. Un rastreador respetuoso consulta las reglas de exclusión antes de visitar una ruta. Dada la lista de rutas prohibidas (`Disallow`) para todos los agentes, escribe `permitido_por_robots(reglas, ruta)` que devuelva `True` si la ruta **no** empieza por ninguna regla prohibida.

4. Tras un escaneo autorizado de tu propia máquina obtienes un registro `{puerto: estado}`. Escribe `puertos_abiertos(resultado)` que devuelva la lista ordenada de los puertos cuyo estado es `"open"`.

5. Para concienciar sobre contraseñas débiles, necesitas estimar cuántas combinaciones hay. Escribe `combinaciones_posibles(longitud, tamano_alfabeto)` que devuelva el número de contraseñas distintas de esa longitud sobre un alfabeto de ese tamaño.

Corrige con: `python corregir.py 8 facil`
