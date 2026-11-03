# Bloque 7 · Análisis de datos binarios — Repaso espaciado

> Mezcla 7.1 Binario/hex y bitwise · 7.2 struct y endianness · 7.3 Magic bytes y headers · 7.4 PCAP.
> Blurting primero. Todo es **análisis local** de datos de ejemplo; no se captura tráfico real.

**1. (7.1) Los permisos de un recurso se guardan en un byte donde cada bit es un permiso. ¿Cómo compruebas si un permiso concreto está activo y por qué se usa una máscara en vez de comparar el número entero?**
Se desplaza el bit a la posición 0 y se aplica `& 1`, o se compara `valor & (1 << pos)`. Una máscara aísla **ese** bit sin que importen los demás; comparar el entero completo mezclaría todos los permisos.

**2. (7.2) ¿Qué diferencia hay entre big-endian y little-endian, y por qué `struct` necesita que le indiques el orden al desempaquetar?**
Es el orden en que se almacenan los bytes de un número: big-endian pone primero el más significativo; little-endian, el menos significativo. Los mismos bytes dan números distintos según el orden, así que `struct` debe saberlo (`>` o `<`) para interpretarlos bien.

**3. (7.3) ¿Qué son los "magic bytes" y por qué identificar un formato por su firma es más fiable que por la extensión del archivo?**
Son los primeros bytes característicos de cada formato (p. ej. `%PDF`, `PK\x03\x04`). La extensión la pone el usuario y se puede falsificar o equivocar; la firma está en el propio contenido.

**4. (7.2 + 7.4) Un archivo PCAP empieza con una cabecera global y luego una serie de registros, cada uno con su propia cabecera de longitud. ¿Por qué necesitas leer la longitud de cada paquete para llegar al siguiente?**
Los paquetes tienen tamaños distintos. La cabecera de cada registro dice cuántos bytes ocupa su contenido; sumando esa longitud (más el tamaño de la cabecera) saltas exactamente al inicio del siguiente registro.

**5. (7.1 + 7.3) El magic de un PCAP permite deducir el endianness del archivo. ¿Cómo lo usas para decidir si lo lees como big o little-endian?**
El magic es un valor fijo (0xA1B2C3D4). Si los primeros bytes son `a1 b2 c3 d4` el archivo es big-endian; si son `d4 c3 b2 a1`, little-endian. A partir de ahí lees el resto con ese mismo orden.
