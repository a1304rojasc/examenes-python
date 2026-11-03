"""Bloque 03 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 03 dificil
"""


import random


def crear_validador(minimo, maximo):
    """Devuelve una función que dice si un número está en [minimo, maximo]."""
    raise NotImplementedError("Implementa crear_validador")


def construir_url(host, ruta="/", **params):
    """Construye "https://host/ruta" + "?k=v&..." si hay parámetros extra."""
    raise NotImplementedError("Implementa construir_url")


def reintentar(funcion, max_intentos):
    """Llama a funcion() hasta que devuelva True; nº de llamadas o -1."""
    raise NotImplementedError("Implementa reintentar")


def potencia_mod(base, exp, mod):
    """base**exp % mod por exponenciación rápida recursiva."""
    raise NotImplementedError("Implementa potencia_mod")


def generar_pin(longitud, semilla):
    """PIN de 'longitud' dígitos reproducible con random.Random(semilla).

    Solo para ejercicios: un PIN real se generaría con el módulo secrets.
    """
    raise NotImplementedError("Implementa generar_pin")
