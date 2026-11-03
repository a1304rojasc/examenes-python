"""Bloque P · Examen difícil — soluciones comentadas."""


def tamano_total(carpeta):
    """Suma de bytes de una carpeta anidada (archivos = números, carpetas = dicts)."""
    total = 0
    for entrada in carpeta.values():
        if isinstance(entrada, dict):
            total += tamano_total(entrada)   # recursión: sumamos la subcarpeta
        else:
            total += entrada                 # caso base: un archivo (número de bytes)
    return total


def cambio_exacto(monto, denominaciones):
    """Lista de valores que suman 'monto' usando las denominaciones, o None."""
    # Probamos de mayor a menor para hallar combinaciones compactas primero.
    denoms = sorted(set(denominaciones), reverse=True)

    def backtrack(restante, inicio, actual):
        if restante == 0:
            return list(actual)              # caso base: lo logramos
        for i in range(inicio, len(denoms)):
            valor = denoms[i]
            if valor <= restante:
                actual.append(valor)
                # i (no i+1) permite repetir la misma denominación.
                solucion = backtrack(restante - valor, i, actual)
                if solucion is not None:
                    return solucion
                actual.pop()                 # deshacemos la decisión (backtracking)
        return None

    return backtrack(monto, 0, [])


def comparaciones_todos_los_pares(n):
    """Número de parejas distintas de n clientes: n*(n-1)/2."""
    return n * (n - 1) // 2


def primera_aparicion(ordenada, objetivo):
    """Posición de la primera aparición de 'objetivo' (búsqueda binaria), o -1."""
    lo, hi = 0, len(ordenada)
    while lo < hi:
        medio = (lo + hi) // 2
        if ordenada[medio] < objetivo:
            lo = medio + 1                   # el objetivo está a la derecha
        else:
            hi = medio                       # puede estar aquí o a la izquierda
    # lo apunta al primer elemento >= objetivo.
    if lo < len(ordenada) and ordenada[lo] == objetivo:
        return lo
    return -1


def fusionar_ordenadas(a, b):
    """Fusiona dos listas ya ordenadas en una sola ordenada (paso de merge sort)."""
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    # Una de las dos ya se agotó; añadimos el resto de la otra.
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado
