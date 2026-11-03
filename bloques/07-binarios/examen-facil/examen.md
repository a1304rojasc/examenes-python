# Bloque 7 · Análisis de datos binarios — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py` (análisis de bytes; `struct` para formatos binarios).
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué representa cada dígito hexadecimal en términos de bits y por qué el hexadecimal es cómodo para mostrar bytes?
2. Explica qué hacen los operadores a nivel de bit `&`, `|`, `^` y el desplazamiento `>>`.
3. ¿Qué es una "máscara de bits" y para qué se usa al leer banderas (flags)?
4. Explica la diferencia entre big-endian y little-endian con un ejemplo de 2 bytes.
5. ¿Para qué sirve el módulo `struct` y qué significa "empaquetar" y "desempaquetar"?
6. ¿Qué son los magic bytes de un archivo y por qué son más fiables que la extensión?
7. ¿Qué diferencia hay entre un objeto `bytes` y una cadena de texto `str`? ¿Por qué un archivo binario se abre en modo binario?
8. ¿Por qué el mismo contenido binario puede significar cosas distintas según el formato que se suponga?
9. ¿Qué es la cabecera (header) de un formato de archivo y qué tipo de información suele contener?
10. ¿Por qué analizar un archivo sospechoso leyendo sus bytes es más seguro que ejecutarlo?

## Parte B — Ejercicios (5 problemas)

1. Un sistema guarda los permisos de un recurso en un solo byte: cada bit es un permiso. Escribe `permiso_activo(permisos, posicion)` que devuelva `True` si el bit en esa posición (contando desde 0, el menos significativo) está encendido.

2. Una herramienta de análisis muestra un volcado legible de los bytes de un archivo. Escribe `a_hex(datos)` que reciba contenido en bytes y devuelva su representación hexadecimal, dos dígitos por byte, separados por un espacio (por ejemplo `b"\xde\xad"` → `"de ad"`).

3. Un sensor transmite registros binarios: 4 bytes con una marca de tiempo (entero sin signo) seguidos de 2 bytes con una temperatura (entero con signo), todo en big-endian. Escribe `leer_registro(datos)` que devuelva la pareja `(marca_de_tiempo, temperatura)`.

4. Un clasificador reconoce el formato de un archivo por su firma inicial. Escribe `identificar_formato(datos)` que devuelva `"PNG"`, `"PDF"`, `"ZIP"` o `"ELF"` según los primeros bytes, o `"desconocido"` si no reconoce ninguno.

5. Dos formatos guardan enteros con órdenes de bytes distintos. Escribe `entero_desde_bytes(datos, orden)` que convierta una secuencia de bytes en el entero que representa, donde `orden` es `"big"` o `"little"`.

Corrige con: `python corregir.py 7 facil`
