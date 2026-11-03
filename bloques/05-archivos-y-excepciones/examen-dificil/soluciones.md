# Bloque 05 · Examen difícil — Soluciones (teoría)

1. Imprime **`finally`** y después **`try`**. `finally` se ejecuta antes de que la función devuelva realmente.
2. Primero la **más específica** (`ValueError`); si `Exception` va antes, la captura siempre y la otra nunca se alcanza.
3. **Relanza** la excepción actual (tras registrarla, por ejemplo).
4. Captura cualquiera de las dos; `e` es el **objeto excepción** (`str(e)` da el mensaje).
5. `class PuertoInvalido(ValueError): pass` (heredar de `Exception` o de una más concreta).
6. Usar `..` en un nombre de archivo controlado por el usuario para salir del directorio permitido. Se previene **resolviendo** la ruta final y comprobando que sigue dentro de la base.
7. Convierte la ruta en **absoluta** y normalizada (resuelve `..` y enlaces simbólicos).
8. `glob` busca solo en ese directorio; `rglob` es **recursivo** (todas las subcarpetas).
9. **Capturar la excepción** (estilo EAFP): entre comprobar y abrir el archivo puede cambiar (Time-Of-Check to Time-Of-Use).
10. `"w"` lo **trunca** y se pierden registros. Para añadir: modo **`"a"`**.
