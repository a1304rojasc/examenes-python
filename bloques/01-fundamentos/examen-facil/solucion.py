"""Bloque 01 · Examen fácil — soluciones comentadas."""


def celsius_a_fahrenheit(c):
    """Convierte grados Celsius a Fahrenheit: F = C * 9/5 + 32."""
    # La división / siempre da float, así que el resultado es float.
    return c * 9 / 5 + 32


def saludar():
    """Pide el nombre con input("Nombre: ") e imprime "Hola, <nombre>!"."""
    nombre = input("Nombre: ").strip()  # strip() quita espacios y saltos sobrantes
    print(f"Hola, {nombre}!")


def es_par(n):
    """Devuelve True si n es par y False si es impar."""
    # Un número es par si el resto de dividir entre 2 es 0.
    return n % 2 == 0


def formatear_precio(cantidad):
    """Devuelve la cantidad con 2 decimales y " €": 3.5 -> "3.50 €"."""
    # :.2f -> coma flotante con exactamente 2 decimales.
    return f"{cantidad:.2f} €"


def segundos_a_hms(segundos):
    """Convierte segundos a "HH:MM:SS" con ceros a la izquierda (3725 -> "01:02:05")."""
    horas = segundos // 3600            # horas completas
    minutos = (segundos % 3600) // 60   # lo que sobra de las horas, en minutos
    segs = segundos % 60                # resto final
    # :02d -> entero con al menos 2 cifras, rellenando con 0.
    return f"{horas:02d}:{minutos:02d}:{segs:02d}"
