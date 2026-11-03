# Bloque 6 · Criptografía con Python — Examen difícil

Combina sub-temas de criptografía (y las imágenes-matriz del Bloque P). Usa **cryptography**; claves generadas al vuelo, **nunca reales**.
Predice el resultado y tu confianza antes de ejecutar.

## Parte A — Teoría (10 preguntas abiertas)

1. Explica qué añade el cifrado autenticado (AES-GCM) frente a un cifrado que solo da confidencialidad, y qué es el "dato adicional autenticado" (AAD).
2. ¿Por qué reutilizar el mismo nonce con la misma clave en AES-GCM es catastrófico?
3. En una firma digital RSA-PSS, ¿qué se firma exactamente y qué demuestra la verificación con la clave pública?
4. ¿Por qué firmar y cifrar son operaciones distintas aunque ambas usen pares de claves? ¿Qué clave interviene en cada una?
5. Explica qué logra un intercambio de claves ECDH y por qué un espía que ve ambas claves públicas no obtiene el secreto compartido.
6. ¿Qué ventajas tienen las curvas elípticas frente a RSA para la misma seguridad?
7. Al validar un certificado TLS, ¿qué tres comprobaciones mínimas hace un cliente y qué ataque evita cada una?
8. ¿Qué significa que un certificado sea "autofirmado" y por qué un navegador lo rechaza por defecto?
9. La esteganografía LSB oculta pero no cifra. ¿Cómo combinarías cifrado y esteganografía para que ocultar el mensaje no baste para leerlo?
10. ¿Por qué la seguridad debe depender solo de la clave y no del secreto del algoritmo (principio de Kerckhoffs)?

## Parte B — Ejercicios (5 problemas)

1. Un servicio guarda expedientes cifrados y quiere que, además, no se puedan manipular ni mover a otro expediente. Usando AES-GCM, escribe `cifrar_gcm(clave, datos, aad)` que devuelva un bloque con el nonce por delante del criptograma, y `descifrar_gcm(clave, bloque, aad)` que recupere los datos. Si el criptograma o el dato adicional (`aad`) han sido alterados, descifrar debe fallar.

2. Un emisor quiere que el receptor pueda comprobar que un comunicado es auténtico y no fue modificado. Con RSA, escribe `firmar(privada, mensaje)` que devuelva la firma (bytes) y `verificar(publica, mensaje, firma)` que devuelva `True` si la firma corresponde a ese mensaje y a esa clave, o `False` en caso contrario.

3. Dos servicios que nunca se han hablado necesitan acordar una clave común por un canal público, sin enviarla. Usando curvas elípticas, escribe `derivar_secreto_compartido(mi_privada, su_publica)` que devuelva el secreto compartido en bytes. Debe cumplirse que ambas partes, con su propia privada y la pública de la otra, obtienen el mismo secreto.

4. Una herramienta de auditoría inspecciona certificados. Escribe `datos_certificado(pem)` que reciba un certificado en formato PEM (bytes) y devuelva un registro con, al menos: el nombre común del sujeto (`sujeto_cn`), el del emisor (`emisor_cn`), el número de serie (`numero_serie`) y las fechas de inicio y fin de validez (`no_antes`, `no_despues`).

5. Para ocultar un aviso dentro de una foto de vigilancia (imagen en escala de grises como matriz de numpy), escribe `ocultar_texto(imagen, texto)` que devuelva una copia de la imagen con el texto escondido en los bits menos significativos, y `revelar_texto(imagen)` que lo recupere. Si la imagen no tiene capacidad suficiente, `ocultar_texto` debe fallar con un error.

Corrige con: `python corregir.py 6 dificil`
