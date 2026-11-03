# Bloque 7 · Análisis de datos binarios — Examen difícil

Combina bits/hex, `struct`, cabeceras y PCAP (con el endianness del Bloque 7 y las ideas de filtrado del Bloque P).
Todo es análisis de datos de ejemplo construidos en el propio test. Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica cómo, a partir de un valor de 32 bits, aislar un campo de varios bits (por ejemplo los bits 4 a 7) usando desplazamiento y máscara.
2. ¿Por qué validar la firma (magic) de una cabecera antes de interpretar el resto evita errores y riesgos?
3. En un formato con cabecera, ¿qué es un "offset" y por qué los formatos usan offsets en lugar de colocar todo seguido?
4. ¿Por qué un archivo PCAP necesita que primero leas su cabecera global para saber cómo interpretar los paquetes?
5. Explica cómo el valor del magic de un PCAP te dice si debes leerlo en big o little-endian.
6. ¿Qué peligros tiene confiar en un campo de "longitud" que viene dentro de un archivo que analizas (por ejemplo, una longitud enorme o negativa)?
7. En el encabezado ELF, los primeros bytes indican la clase (32/64 bits) y el orden de bytes. ¿Por qué el resto del encabezado no se puede leer sin conocer antes esos dos datos?
8. ¿Qué diferencia hay entre análisis estático (leer los bytes) y dinámico (ejecutar) de un archivo, y por qué el estático es el primer paso seguro?
9. ¿Por qué los indicadores (flags) de un protocolo caben en un solo byte y cómo se decodifican?
10. Al procesar muchos registros binarios en secuencia, ¿por qué conviene comprobar que quedan suficientes bytes antes de desempaquetar cada uno?

## Parte B — Ejercicios (5 problemas)

1. Un formato propio de capturas empieza con una cabecera de 12 bytes en big-endian: una firma de 4 bytes que debe valer `0x1A2B3C4D`, dos enteros de 2 bytes con la versión mayor y menor, y un entero de 4 bytes con el número de registros. Escribe `parsear_cabecera(datos)` que devuelva un registro con `version` (pareja mayor, menor) y `total`. Si la firma no coincide o faltan bytes, debe fallar con un error.

2. Una herramienta forense inspecciona ejecutables ELF. Los primeros bytes del encabezado son la firma `\x7fELF`, luego un byte de clase (1 = 32 bits, 2 = 64 bits), un byte de orden (1 = little-endian, 2 = big-endian), y en el offset 16 hay un entero de 2 bytes con el tipo de objeto. Escribe `cabecera_elf(datos)` que devuelva un registro con `clase`, `endian` (`"little"`/`"big"`) y `tipo`. Si no es un ELF válido, debe fallar.

3. Un archivo PCAP empieza con una cabecera global de 24 bytes; después, cada paquete tiene una cabecera de 16 bytes (segundos, microsegundos, longitud capturada, longitud original) seguida de la longitud capturada en bytes de datos. El endianness se deduce del magic inicial (`0xA1B2C3D4`). Escribe `resumen_pcap(datos)` que devuelva una lista con, por cada paquete, la pareja `(segundos, longitud_capturada)`, en orden.

4. Para un informe de tráfico necesitas cuántos paquetes superan cierto tamaño. Escribe `paquetes_grandes(datos, umbral)` que, sobre un PCAP como el del ejercicio anterior, devuelva cuántos paquetes tienen una longitud capturada **estrictamente mayor** que `umbral`.

5. Un analizador muestra los indicadores de un segmento TCP, codificados en un byte donde el bit 0 es FIN, el 1 SYN, el 2 RST, el 3 PSH, el 4 ACK y el 5 URG. Escribe `flags_activos(valor)` que devuelva la lista de nombres de los indicadores activos, en ese orden de bits.

Corrige con: `python corregir.py 7 dificil`
