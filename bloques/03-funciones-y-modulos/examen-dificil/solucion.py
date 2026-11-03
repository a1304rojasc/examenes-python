"""Bloque 03 · Examen difícil — soluciones comentadas."""
import random


def crear_validador(minimo, maximo):
    """Devuelve una función que dice si un número está en [minimo, maximo]."""
    def validar(numero):
        # 'minimo' y 'maximo' se recuerdan gracias a la closure.
        return minimo <= numero <= maximo
    return validar


def construir_url(host, ruta="/", **params):
    """Construye "https://host/ruta" + "?k=v&..." si hay parámetros extra."""
    url = f"https://{host}{ruta}"
    if params:
        # kwargs conserva el orden en que se pasaron los argumentos.
        partes = [f"{clave}={valor}" for clave, valor in params.items()]
        url += "?" + "&".join(partes)
    return url


def reintentar(funcion, max_intentos):
    """Llama a funcion() hasta que devuelva True; nº de llamadas o -1."""
    for intento in range(1, max_intentos + 1):
        if funcion():
            return intento
    return -1


def potencia_mod(base, exp, mod):
    """base**exp % mod por exponenciación rápida recursiva."""
    if exp == 0:               # caso base: b^0 = 1
        return 1 % mod
    mitad = potencia_mod(base, exp // 2, mod)
    resultado = (mitad * mitad) % mod
    if exp % 2 == 1:           # exponente impar: falta un factor base
        resultado = (resultado * base) % mod
    return resultado


def generar_pin(longitud, semilla):
    """PIN de 'longitud' dígitos reproducible con random.Random(semilla).

    Solo para ejercicios: un PIN real se generaría con el módulo secrets.
    """
    rng = random.Random(semilla)   # generador propio: no toca el global
    pin = ""
    for _ in range(longitud):
        pin += str(rng.randint(0, 9))
    return pin
