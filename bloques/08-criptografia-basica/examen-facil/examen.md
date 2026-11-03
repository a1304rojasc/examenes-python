# Bloque 08 · Criptografía básica — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Base64 protege la confidencialidad de un dato? Justifica.
2. ¿Cuántos caracteres hexadecimales tiene un hash SHA-256?
3. ¿Qué método convierte un `str` en `bytes` antes de hashearlo?
4. ¿Qué es una colisión de hash?
5. ¿Por qué MD5 y SHA-1 se consideran rotos para seguridad?
6. ¿Cuántas claves posibles tiene el cifrado César sobre el alfabeto inglés (26 letras), sin contar la clave 0?
7. Cifra `"ABC"` con César desplazamiento 3.
8. ¿Qué diferencia hay entre *codificar*, *hashear* y *cifrar*?
9. ¿Para qué sirve publicar el SHA-256 de un archivo descargable?
10. ¿Qué módulo de Python se usa para generar tokens aleatorios seguros?

## Parte B — Código (5 ejercicios)

1. `codificar_b64(texto)` y `decodificar_b64(b64)` → convierten texto UTF-8 ⇄ Base64 (ambas devuelven `str`).
2. `sha256_hex(texto)` → hash SHA-256 en hexadecimal del texto en UTF-8.
3. `cesar(texto, desplazamiento)` → desplaza letras `A–Z` y `a–z` conservando mayúsculas; el resto de caracteres no cambia. Admite desplazamientos negativos o mayores que 26.
4. `descifrar_cesar(texto, desplazamiento)` → deshace `cesar` (reutiliza tu función).
5. `verificar_integridad(ruta, hash_esperado)` → `True` si el SHA-256 del archivo (leído en binario y **por bloques**) coincide con el esperado (sin distinguir mayúsculas).

Corrige con: `python corregir.py 08 facil`
