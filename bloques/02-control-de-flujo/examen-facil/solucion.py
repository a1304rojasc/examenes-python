"""Bloque 02 · Examen fácil — soluciones comentadas."""


def clasificar_nota(nota):
    """Devuelve "suspenso" (<5), "aprobado" (<7), "notable" (<9) o "sobresaliente"."""
    # Con elif solo se entra en la primera condición verdadera, por eso
    # basta comprobar el límite superior de cada tramo.
    if nota < 5:
        return "suspenso"
    elif nota < 7:
        return "aprobado"
    elif nota < 9:
        return "notable"
    else:
        return "sobresaliente"


def suma_hasta(n):
    """Suma 1 + 2 + ... + n con un bucle. Devuelve 0 si n < 1."""
    total = 0
    for i in range(1, n + 1):  # n + 1 porque range excluye el final
        total += i
    return total


def contar_vocales(texto):
    """Cuenta las vocales (aeiou, sin distinguir mayúsculas) del texto."""
    contador = 0
    for letra in texto.lower():  # lower() para tratar "A" igual que "a"
        if letra in "aeiou":
            contador += 1
    return contador


def primer_negativo(numeros):
    """Índice del primer número negativo, o -1 si no hay ninguno. Usa break."""
    posicion = -1
    for i in range(len(numeros)):
        if numeros[i] < 0:
            posicion = i
            break  # ya lo encontramos: no hace falta seguir
    return posicion


def suma_sin_multiplos_de_3(n):
    """Suma de 1 a n saltándose los múltiplos de 3. Usa continue."""
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            continue  # salta este número y pasa al siguiente
        total += i
    return total
