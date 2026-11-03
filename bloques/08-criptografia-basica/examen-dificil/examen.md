# Bloque 08 · Criptografía básica — Examen difícil

Combina bloques 01–07 (funciones, diccionarios, archivos, texto) con criptografía. **Regla de oro**: en producción usa siempre bibliotecas estándar; César y Vigenère son solo didácticos.

## Parte A — Teoría (10 preguntas)

1. ¿Qué es la *sal* (salt) de una contraseña y qué ataque evita?
2. ¿Por qué PBKDF2 usa muchas iteraciones? ¿Qué pasa con el coste para el atacante?
3. ¿Por qué comparar hashes con `==` puede filtrar información y qué se usa en su lugar?
4. ¿Qué garantiza un HMAC que no garantiza un hash simple?
5. ¿Por qué `sha256(clave + mensaje)` no es un buen MAC? (pista: *length extension*)
6. ¿Cómo se rompe César con análisis de frecuencias? ¿Qué letra es la más frecuente en español?
7. En Vigenère, si la clave es tan larga como el mensaje, aleatoria y nunca se reutiliza, ¿qué sistema obtienes?
8. ¿Qué es el principio de Kerckhoffs?
9. Un compañero propone "cifrar" contraseñas con XOR y una clave fija en el código. Da dos motivos por los que es mala idea.
10. ¿Por qué auditar las contraseñas de **tus** usuarios contra un diccionario de contraseñas filtradas es una práctica defensiva legítima, y qué límites tiene?

## Parte B — Código (5 ejercicios)

1. `vigenere(texto, clave, descifrar=False)` → cifra/descifra Vigenère sobre letras `A–Z`/`a–z` (conserva mayúsculas); la clave (solo letras, sin distinguir mayúsculas) **solo avanza con letras**; los demás caracteres no cambian.
2. `romper_cesar(cifrado)` → `(desplazamiento, texto_claro)` probando los 26 desplazamientos y eligiendo el de menor chi-cuadrado frente a las frecuencias del español (se dan en `FRECUENCIAS_ES`).
3. `hash_password(password, sal=None, iteraciones=100_000)` → cadena `"pbkdf2_sha256$<iter>$<sal_hex>$<hash_hex>"` con `hashlib.pbkdf2_hmac`; si no hay sal, genera 16 bytes con `secrets`/`os.urandom`. `verificar_password(password, almacenado)` → `bool` usando `hmac.compare_digest`.
4. `firmar(mensaje, clave)` → HMAC-SHA256 en hex. `verificar_firma(mensaje, clave, firma)` → `bool` en tiempo constante.
5. `auditar_debiles(hashes, diccionario)` → recibe `{usuario: sha256_hex}` de **tu propio** sistema de pruebas y una lista de contraseñas débiles; devuelve `{usuario: contraseña}` de los que usan una débil (precalcula los hashes una sola vez).

Corrige con: `python corregir.py 08 dificil`
