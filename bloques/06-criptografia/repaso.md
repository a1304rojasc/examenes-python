# Bloque 6 · Criptografía con Python — Repaso espaciado

> Mezcla 6.1 Hashing · 6.2 Simétrico · 6.3 Asimétrico · 6.4 Curvas elípticas · 6.5 TLS · 6.6 Esteganografía.
> Blurting primero. **Nunca uses claves privadas reales**: en estos ejercicios se generan al vuelo con la librería.

**1. (6.1 + 6.2) Un hash SHA-256 y un cifrado AES protegen cosas distintas. ¿Qué garantiza cada uno y por qué un hash no sirve para "guardar un secreto y recuperarlo"?**
El hash garantiza **integridad** (detectar cambios) y es de un solo sentido: no se puede revertir. AES garantiza **confidencialidad** reversible: con la clave se descifra. Guardar un secreto para recuperarlo necesita cifrado, no hashing.

**2. (6.2) ¿Por qué el IV/nonce de un cifrado simétrico debe ser único por mensaje y por qué no es secreto?**
Reutilizar el nonce con la misma clave filtra información (en GCM, puede romper toda la seguridad). No es secreto porque su función es solo garantizar que dos cifrados de un mismo texto salgan distintos; se envía junto al criptograma.

**3. (6.3 + 6.4) RSA y las curvas elípticas resuelven lo mismo con tamaños muy distintos. ¿Qué ventaja tienen las curvas elípticas y para qué se usa un intercambio ECDH?**
Las curvas elípticas dan la misma seguridad con claves mucho más cortas (p. ej. 256 bits ≈ RSA 3072), más rápidas y ligeras. ECDH permite que dos partes acuerden un **secreto compartido** por un canal público sin enviarlo nunca.

**4. (6.1 + 6.3) En una firma digital, ¿por qué se firma el hash del mensaje y no el mensaje entero, y qué demuestra verificar la firma con la clave pública?**
Se firma el hash por eficiencia (tamaño fijo y pequeño). Verificar con la pública demuestra **autenticidad e integridad**: el mensaje lo firmó quien tiene la privada y no se alteró.

**5. (6.5 + 6.6) ¿Qué comprueba un cliente al validar un certificado TLS, y en qué se diferencia eso de la esteganografía LSB?**
En TLS valida que el certificado no haya caducado, que lo firme una CA de confianza y que el nombre coincida con el host. La esteganografía LSB no cifra ni autentica: **oculta** la existencia del mensaje cambiando el bit menos significativo de los píxeles; sin cifrado, cualquiera que sepa dónde mirar lo lee.
