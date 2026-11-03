"""Bloque 03 · Examen fácil — soluciones comentadas."""
import math

EVENTOS = 0


def area_rectangulo(base, altura=1):
    """Devuelve base * altura (altura vale 1 si no se indica)."""
    return base * altura


def estadisticas(numeros):
    """Devuelve (mínimo, máximo, media) de una lista no vacía."""
    # min, max, sum y len son funciones integradas (built-ins).
    media = sum(numeros) / len(numeros)
    return min(numeros), max(numeros), media  # se empaqueta como tupla


def aplicar(funcion, valor, veces=1):
    """Aplica funcion a valor 'veces' veces seguidas y devuelve el resultado."""
    # Las funciones son valores: se pueden pasar como argumento y llamar.
    for _ in range(veces):
        valor = funcion(valor)
    return valor


def registrar_evento():
    """Suma 1 a la variable global EVENTOS y devuelve el nuevo valor."""
    global EVENTOS  # sin esto, EVENTOS += 1 daría UnboundLocalError
    EVENTOS += 1
    return EVENTOS


def reiniciar_eventos():
    """Pone la variable global EVENTOS a 0."""
    global EVENTOS
    EVENTOS = 0


def hipotenusa(a, b):
    """Devuelve la raíz cuadrada de a² + b² usando el módulo math."""
    return math.sqrt(a ** 2 + b ** 2)  # también vale math.hypot(a, b)
