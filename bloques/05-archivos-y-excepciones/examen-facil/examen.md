# Bloque 05 · Archivos y excepciones — Examen fácil

## Parte A — Teoría (10 preguntas)

1. ¿Qué modo de `open` borra el contenido previo del archivo? a) `"r"` b) `"a"` c) `"w"` d) `"x"`
2. ¿Qué excepción lanza `int("hola")`?
3. ¿Qué excepción lanza `open("no_existe.txt")`?
4. ¿Qué devuelve `f.read()` y qué devuelve `f.readlines()`?
5. ¿Qué hace el bloque `finally`?
6. ¿Por qué es mala práctica `except:` sin tipo?
7. ¿Qué hace `raise ValueError("puerto inválido")`?
8. ¿Qué devuelve `Path("informe.TXT").suffix`?
9. ¿Por qué conviene indicar `encoding="utf-8"` al abrir archivos de texto?
10. ¿Qué imprime?
    ```python
    try:
        x = 1 / 0
    except ZeroDivisionError:
        print("A")
    else:
        print("B")
    finally:
        print("C")
    ```

## Parte B — Código (5 ejercicios)

1. `contar_lineas(ruta)` → número de líneas del archivo.
2. `escribir_lineas(ruta, lineas)` → escribe cada cadena de la lista en una línea (terminada en `"\n"`), sobrescribiendo el archivo.
3. `dividir_seguro(a, b)` → `a / b`, o `None` si `b` es 0 (captura la excepción, no uses `if`).
4. `leer_config(ruta)` → lee líneas `clave=valor` y devuelve un diccionario (sin espacios sobrantes). Ignora líneas vacías y las que empiezan por `#`. Si el archivo no existe devuelve `{}`.
5. `extension(ruta)` → extensión en minúsculas sin el punto usando `pathlib`: `"logs/Auth.LOG"` → `"log"`; sin extensión → `""`.

Corrige con: `python corregir.py 05 facil`
