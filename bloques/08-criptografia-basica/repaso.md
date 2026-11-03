# Bloque 08 · Criptografía básica — Repaso

**1. ¿Base64 es cifrado?**
**No.** Es una *codificación* para representar bytes como texto; cualquiera la revierte sin clave.

**2. ¿Qué propiedades tiene un hash criptográfico (SHA-256)?**
Tamaño fijo, determinista, irreversible en la práctica, y un cambio mínimo en la entrada cambia totalmente la salida (efecto avalancha). Resistente a colisiones.

**3. ¿Por qué no se guardan contraseñas con `sha256(password)`?**
Es demasiado rápido y sin sal: permite ataques de diccionario y tablas precalculadas. Se usa una función lenta con sal: PBKDF2, bcrypt, scrypt o Argon2.

**4. ¿Por qué César y Vigenère no son seguros?**
César tiene solo 25 claves (fuerza bruta inmediata); ambos conservan patrones del idioma (análisis de frecuencias, Kasiski).

**5. ¿Por qué "no inventar tu propia cripto"?**
Diseñar e implementar cripto segura es extremadamente difícil; los errores no se ven hasta que alguien los explota. Usa bibliotecas auditadas (`hashlib`, `hmac`, `secrets`, `cryptography`) y algoritmos estándar. Principio de Kerckhoffs: la seguridad debe depender solo de la clave, no del secreto del algoritmo.
