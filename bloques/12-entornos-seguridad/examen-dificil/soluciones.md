# Bloque 12 · Examen difícil — Soluciones (teoría)

1. Se prueban las 256 claves de un byte; para cada una se hace XOR de todo el mensaje y se obtiene un candidato de texto claro. Se elige el candidato que contiene el "crib" conocido (`FLAG{`); como el espacio es minúsculo, el proceso es instantáneo y casi siempre hay una única clave que encaja.
2. La ventana deslizante recorre los eventos ordenados por tiempo con dos índices, contando cuántos caben en un intervalo; es O(n log n) por la ordenación, frente a O(n²) de comparar todos los pares. Además refleja bien la idea de "muchos intentos en poco tiempo".
3. Porque un mismo problema puede disparar cientos de alertas idénticas y saturar al analista (fatiga de alertas). Agruparlas con un contador y el rango temporal da una visión clara sin perder información.
4. Un falso positivo es una alerta sin ataque real. Subir el umbral reduce falsos positivos pero aumenta los falsos negativos (ataques que pasan); bajarlo hace lo contrario. Hay que equilibrarlo según el contexto.
5. Porque la salida real contiene cabeceras, líneas en blanco, mensajes y formatos que cambian entre versiones. Si el parser no es tolerante, una línea inesperada lo rompe; conviene saltarse lo que no encaja en lugar de fallar.
6. Se envía como entrada un patrón donde cada tramo de 4 caracteres es único. Cuando el programa falla, el valor que quedó en el registro o la pila corresponde a un tramo concreto; buscar ese tramo en el patrón da la posición exacta (el offset) de la entrada.
7. Porque generar alertas es fácil y el volumen abruma; el valor está en relacionar señales, descartar ruido y priorizar lo que de verdad importa, que es donde se toman decisiones.
8. Un CTF está diseñado y autorizado para ser atacado: es legal y educativo. Usar la misma técnica contra un sistema real sin permiso es acceso no autorizado: ilegal y potencialmente dañino, por buena que sea la intención.
9. Porque cada fuente puede usar husos horarios, formatos de fecha o notaciones de IP distintos. Sin normalizar, los eventos no se alinean en el tiempo ni se reconoce que dos registros hablan de la misma IP, y la correlación falla.
10. Porque en un incidente real se depende de ella bajo presión: si no es reproducible o tiene errores, puede dar resultados falsos, perder evidencia o empeorar la situación. Las pruebas dan confianza en que hace lo que promete.
