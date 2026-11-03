# Bloque 6 · Examen fácil — Soluciones (teoría)

1. Produce una salida de **tamaño fijo** (256 bits), es **determinista**, es **irreversible** en la práctica (no se recupera la entrada) y tiene **efecto avalancha**: un cambio mínimo cambia toda la huella. Además es resistente a colisiones.
2. Permite comprobar la **integridad**: si la huella calculada coincide, el archivo no se corrompió ni se alteró. No garantiza autenticidad por sí sola: si el atacante controla también la página donde se publica la huella, puede cambiar ambas. La huella debe venir de una fuente confiable.
3. **Codificar** cambia la representación de los datos y es reversible sin secreto (base64). **Hashear** produce un resumen de un solo sentido. **Cifrar** transforma los datos de forma reversible, pero solo con la clave.
4. Que la **misma clave** cifra y descifra. El problema es la **distribución de la clave**: hay que hacerla llegar al otro extremo por un canal seguro sin que la intercepten.
5. El IV/nonce hace que cifrar el mismo texto dé resultados distintos y evita patrones. Si se repite con la misma clave, se filtra información; en modos como GCM, reutilizarlo rompe la seguridad por completo.
6. Es el que, además de ocultar el contenido, añade una **etiqueta de autenticación** que detecta cualquier manipulación del criptograma (integridad y autenticidad). Ejemplos: AES-GCM, Fernet.
7. Se cifra con la **clave pública** del destinatario (que es pública y la puede tener cualquiera) y solo se descifra con su **clave privada** (que guarda en secreto). Así solo él puede leerlo.
8. SHA-256 es demasiado **rápido** y sin sal, lo que facilita ataques de diccionario y tablas precalculadas. Se usan funciones lentas con sal: PBKDF2, bcrypt, scrypt o Argon2.
9. Se sustituye el **bit menos significativo** de cada píxel por un bit del mensaje. Como ese bit cambia el color en una unidad como mucho, el ojo no nota la diferencia.
10. Diseñar e implementar criptografía segura es extremadamente difícil y los errores no se ven hasta que alguien los explota. Las bibliotecas auditadas (como `cryptography`) ya resolvieron esos detalles; reinventarlo introduce fallos sutiles.
