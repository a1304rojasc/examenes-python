# Bloque 6 · Criptografía con Python — Examen fácil

Parte A: preguntas abiertas. Parte B: programa en `ejercicios.py` usando la librería **cryptography** (y `hashlib` para hashing).
Las claves se generan al vuelo; **nunca** incrustes claves privadas reales. Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. ¿Qué propiedades tiene una función hash criptográfica como SHA-256 (tamaño, reversibilidad, sensibilidad al cambio)?
2. ¿Por qué publicar la huella SHA-256 de un archivo descargable ayuda a los usuarios, y qué NO garantiza por sí sola?
3. Explica la diferencia entre *codificar* (p. ej. base64), *hashear* y *cifrar*.
4. ¿Qué significa que un cifrado sea "simétrico"? ¿Qué problema aparece al tener que compartir la clave?
5. ¿Para qué sirve el IV o nonce en un cifrado simétrico y por qué no debe repetirse con la misma clave?
6. ¿Qué es el "cifrado autenticado" y qué protege además de la confidencialidad?
7. En el cifrado asimétrico, ¿qué papel cumple la clave pública y cuál la privada al **cifrar un mensaje para alguien**?
8. ¿Por qué no se deben guardar contraseñas con un simple SHA-256? ¿Qué se usa en su lugar?
9. Explica en qué consiste la esteganografía LSB sobre una imagen y por qué el cambio es casi imperceptible.
10. ¿Por qué la recomendación profesional es "no inventes tu propia criptografía" y usar bibliotecas auditadas?

## Parte B — Ejercicios (5 problemas)

1. Un repositorio de descargas publica, junto a cada archivo, su huella para que cualquiera compruebe que no se corrompió. Escribe `huella_sha256(datos)` que reciba el contenido en bytes y devuelva su huella SHA-256 en hexadecimal.

2. El verificador del repositorio debe decir si un archivo descargado coincide con la huella publicada, sin que importe si la huella viene en mayúsculas o minúsculas y comparándola de forma segura. Escribe `coincide_huella(datos, huella_hex)` que devuelva `True`/`False`.

3. Una aplicación de notas privadas guarda cada nota cifrada en disco con el cifrado autenticado de alto nivel de la librería (Fernet). Escribe `cifrar_nota(clave, texto)` que devuelva el token cifrado (bytes) y `descifrar_nota(clave, token)` que recupere el texto original.

4. Dos compañeros quieren intercambiar un mensaje confidencial: el receptor publica su clave pública y el emisor cifra solo para él. Usando RSA, escribe `cifrar_para(publica, mensaje)` que devuelva el criptograma (bytes) y `descifrar_con(privada, criptograma)` que recupere el mensaje en bytes.

5. Para ocultar información en una imagen con la técnica LSB necesitas manipular el bit menos significativo de cada píxel (un entero 0–255). Escribe `esconder_bit(valor, bit)` que devuelva el valor con su bit menos significativo igualado a `bit` (0 o 1), y `extraer_bit(valor)` que devuelva ese bit.

Corrige con: `python corregir.py 6 facil`
