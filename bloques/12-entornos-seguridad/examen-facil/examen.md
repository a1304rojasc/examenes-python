# Bloque 12 · Python en entornos de seguridad — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py`. **Local y con datos de ejemplo**; retos tipo CTF y parseo de resultados.
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué caracteriza a una distribución como Kali o Parrot y para qué se usan?
2. ¿Por qué ciertas operaciones de red (sockets en bruto, puertos bajos) requieren privilegios de root?
3. ¿Por qué conviene trabajar con el mínimo privilegio y no ejecutarlo todo como root?
4. ¿Qué es un CTF y qué tipo de habilidades entrena?
5. ¿Por qué XOR con una clave de un byte es fácil de romper?
6. ¿Qué es `pwntools` y en qué contexto legítimo se usa?
7. ¿Qué papel cumple Python al automatizar herramientas como Metasploit (parsear, orquestar)?
8. ¿Qué es un SOC y qué es un SIEM?
9. ¿Qué significa "correlacionar" eventos de seguridad?
10. ¿Por qué estas técnicas solo se practican en laboratorios propios, CTF o con autorización?

## Parte B — Ejercicios (5 problemas)

1. Al preparar una herramienta que escucha en un puerto, quieres avisar si hará falta `sudo`. Escribe `necesita_privilegios(puerto)` que devuelva `True` si el puerto es "privilegiado" (por debajo de 1024) y `False` en caso contrario.

2. Un reto CTF te da datos cifrados con XOR usando una clave que se repite. Escribe `xor_repetida(datos, clave)` que devuelva el resultado de aplicar XOR byte a byte entre `datos` y la `clave` repetida tantas veces como haga falta (ambos en bytes). La misma función sirve para cifrar y descifrar.

3. En la salida de un reto buscas la bandera. Escribe `buscar_flag(texto)` que devuelva la primera cadena con el formato `FLAG{...}` (contenido cualquiera sin `}`) que aparezca en el texto, o `None` si no hay.

4. Un panel de SOC resume los eventos por severidad. Escribe `contar_por_severidad(eventos)` que, dada una lista de registros con un campo `severidad`, devuelva un registro `{severidad: número de eventos}`.

5. Para automatizar la configuración de un módulo (estilo Metasploit) parseas sus órdenes. Escribe `opciones_modulo(lineas)` que, dadas líneas como `set RHOSTS 192.0.2.10`, devuelva un registro `{OPCION: valor}` con cada opción configurada (si una se repite, vale la última). Ignora las líneas que no empiecen por `set`.

Corrige con: `python corregir.py 12 facil`
