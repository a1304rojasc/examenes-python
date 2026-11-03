# Bloque 08 · Examen difícil — Soluciones (teoría)

1. Un valor aleatorio único por usuario que se mezcla con la contraseña antes de hashear. Evita las **tablas precalculadas (rainbow tables)** y que dos usuarios con la misma contraseña tengan el mismo hash.
2. Para que cada intento sea **lento**: al usuario legítimo le cuesta milisegundos una vez, al atacante le multiplica el coste de probar millones de contraseñas.
3. `==` puede terminar antes en el primer byte distinto (**ataque de temporización**). Se usa `hmac.compare_digest`, de tiempo constante.
4. **Autenticidad**: solo quien conoce la clave pudo generarlo (además de integridad).
5. Con SHA-256 (Merkle–Damgård) un atacante puede **extender** el mensaje y calcular un hash válido sin conocer la clave. HMAC está diseñado para evitarlo.
6. Se cuentan las letras del cifrado y se prueba qué desplazamiento hace coincidir su distribución con la del idioma. En español la más frecuente es la **E** (seguida de la A).
7. El **one-time pad** (cifrado de Vernam), con secreto perfecto.
8. Un sistema debe ser seguro aunque **todo sea público excepto la clave**.
9. XOR con clave fija es **reversible** (y la clave en el código se puede extraer); además las contraseñas no deben poder recuperarse: se **hashean** con una KDF lenta y sal. Y el XOR repetido se rompe con análisis de frecuencias.
10. Porque detecta cuentas en riesgo **antes** que un atacante y permite forzar un cambio. Límites: solo sobre sistemas propios/autorizados, sin exponer las contraseñas encontradas y cumpliendo la política de privacidad (lo ideal es comprobarlo en el momento del cambio de contraseña).
