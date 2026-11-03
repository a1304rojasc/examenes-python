# Bloque 7 · Examen difícil — Soluciones (teoría)

1. Se desplaza el valor a la derecha hasta llevar el campo al bit 0 y se aplica una máscara con tantos unos como bits tenga el campo. Para los bits 4–7: `(valor >> 4) & 0b1111`.
2. Si la firma no coincide, el archivo no es del tipo esperado y seguir interpretándolo daría valores sin sentido o provocaría leer fuera de rango. Validar primero es una comprobación barata que evita errores y entradas maliciosas.
3. Un offset es la posición (en bytes, desde el inicio) donde empieza algo. Los formatos los usan para colocar secciones de tamaño variable y poder saltar directamente a cada una sin recorrer todo.
4. La cabecera global indica, entre otras cosas, el endianness y la versión; sin ella no sabrías cómo leer los números de las cabeceras de cada paquete.
5. El magic es el valor fijo 0xA1B2C3D4. Si los primeros bytes son `a1 b2 c3 d4`, el archivo es big-endian; si son `d4 c3 b2 a1`, little-endian. Se usa ese orden para todo lo demás.
6. Una longitud manipulada puede hacer que el programa intente leer gigabytes (agotar memoria), leer fuera de los datos o entrar en un bucle. Hay que validar que la longitud sea razonable y que realmente queden esos bytes.
7. La clase determina el tamaño de varios campos (direcciones de 4 u 8 bytes) y el orden determina cómo leer cada número. Sin esos dos datos no se sabe ni cuántos bytes ocupa cada campo ni cómo interpretarlos.
8. El estático lee los bytes sin ejecutar; el dinámico corre el archivo y observa su comportamiento. El estático es el primer paso seguro porque no activa código potencialmente dañino.
9. Porque son un conjunto pequeño de condiciones de sí/no; cada bit representa una. Se decodifican comprobando cada bit con una máscara (`valor & (1 << i)`).
10. Porque un archivo truncado o manipulado puede no tener los bytes que su cabecera promete. Desempaquetar sin comprobarlo lanzaría un error o leería datos de otro registro; comprobarlo permite parar de forma controlada.
