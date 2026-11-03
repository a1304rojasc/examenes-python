"""Bloque P · Examen fácil — soluciones comentadas."""
import numpy as np


def ventas_sobre_promedio(ventas):
    """Cuántas ventas superan el promedio del día (0 si la lista está vacía)."""
    if not ventas:
        return 0
    promedio = sum(ventas) / len(ventas)
    # Acumulador: contamos 1 por cada venta estrictamente mayor que el promedio.
    return sum(1 for v in ventas if v > promedio)


def temperatura_extremos(linea):
    """Devuelve (mínima, máxima) de las temperaturas separadas por comas."""
    # Partimos el texto por comas y convertimos cada trozo a número.
    temperaturas = [float(x) for x in linea.split(",")]
    return (min(temperaturas), max(temperaturas))


def producto_menor_stock(inventario):
    """Nombre del producto con menos unidades (el primero en caso de empate)."""
    # min con clave: compara por "cantidad" y, al empatar, conserva el primero.
    articulo = min(inventario, key=lambda a: a["cantidad"])
    return articulo["producto"]


def promedio_por_estudiante(notas):
    """Lista de promedios, uno por fila (estudiante), en el mismo orden."""
    return [sum(fila) / len(fila) for fila in notas]


def espejo_horizontal(imagen):
    """Imagen volteada de izquierda a derecha (espejo)."""
    # Invertir el orden de las columnas equivale a reflejar horizontalmente.
    return imagen[:, ::-1]
