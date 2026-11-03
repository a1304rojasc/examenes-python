"""Bloque 04 · Examen fácil — soluciones comentadas."""


def eliminar_duplicados(lista):
    """Devuelve una lista nueva sin repetidos, conservando el orden."""
    vistos = set()        # pertenencia rápida
    resultado = []        # conserva el orden
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado
    # Alternativa en una línea: list(dict.fromkeys(lista))


def contar_frecuencias(palabras):
    """Devuelve {palabra: número de apariciones}."""
    frecuencias = {}
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias


def puertos_comunes(a, b):
    """Lista ordenada de los puertos que están en a y en b."""
    return sorted(set(a) & set(b))  # & = intersección de conjuntos


def cuadrados_pares(n):
    """Cuadrados de los pares de 0 a n (incluido), con una comprensión."""
    return [x * x for x in range(n + 1) if x % 2 == 0]


def invertir_diccionario(d):
    """Intercambia claves y valores: {"ssh": 22} -> {22: "ssh"}."""
    return {valor: clave for clave, valor in d.items()}
