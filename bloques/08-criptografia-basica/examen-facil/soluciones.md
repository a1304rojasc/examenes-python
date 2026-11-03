# Bloque 08 · Examen fácil — Soluciones (teoría)

1. **No**. Es una codificación reversible sin clave; solo cambia la representación.
2. **64** (256 bits / 4 bits por carácter hex).
3. **`.encode()`** (normalmente `"utf-8"`).
4. Dos entradas **distintas** que producen **el mismo** hash.
5. Se conocen ataques prácticos para **generar colisiones**; ya no garantizan integridad.
6. **25**.
7. **`"DEF"`**.
8. Codificar: cambiar representación (reversible, sin secreto). Hashear: resumen de un solo sentido. Cifrar: transformación reversible **solo con la clave**.
9. Para que el usuario compruebe la **integridad**: si su hash coincide, el archivo no se ha corrompido ni alterado (siempre que el hash venga de una fuente confiable).
10. **`secrets`** (p. ej. `secrets.token_hex(16)`).
