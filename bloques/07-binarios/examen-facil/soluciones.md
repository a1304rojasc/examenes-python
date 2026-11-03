# Bloque 7 · Examen fácil — Soluciones (teoría)

1. Cada dígito hexadecimal representa 4 bits (un "nibble"), así que dos dígitos son exactamente un byte (0–255). Por eso es cómodo: cada byte se ve siempre como dos caracteres, frente a los 8 del binario.
2. `&` (AND) deja 1 solo donde ambos bits son 1; `|` (OR) donde al menos uno es 1; `^` (XOR) donde son distintos; `>>` desplaza los bits a la derecha, descartando los de menor peso (equivale a dividir por potencias de 2).
3. Es un número con ciertos bits a 1 que se combina con `&` para aislar o comprobar bits concretos. Para leer una bandera se hace `valor & (1 << posicion)`: distinto de 0 si está activa.
4. Es el orden en que se guardan los bytes de un número. El valor 0x00FF en big-endian se almacena `00 FF`; en little-endian, `FF 00`. Leer con el orden equivocado da otro número.
5. `struct` convierte entre bytes y valores de Python según un formato. "Empaquetar" (`pack`) crea bytes a partir de valores; "desempaquetar" (`unpack`) interpreta bytes como valores (enteros, flotantes…).
6. Son los primeros bytes característicos de cada formato. Son más fiables que la extensión porque están en el propio contenido y no dependen de cómo se llame el archivo.
7. `bytes` es una secuencia de valores 0–255 (datos crudos); `str` es texto (caracteres). Un binario se abre en modo binario (`"rb"`) para no alterar los bytes con conversiones de texto o de saltos de línea.
8. Porque los bytes no tienen significado por sí mismos: el formato define cómo interpretarlos. Los mismos 4 bytes pueden ser un entero, cuatro caracteres o parte de una imagen.
9. Es el bloque inicial con metadatos del archivo: firma, versión, tamaños, offsets a otras secciones. Permite al lector saber cómo está estructurado el resto.
10. Leer los bytes no ejecuta nada; solo los inspecciona. Ejecutar un archivo sospechoso podría activar código malicioso. El análisis estático observa sin correr el riesgo.
