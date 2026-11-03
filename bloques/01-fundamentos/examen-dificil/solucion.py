"""Bloque 01 · Examen difícil — soluciones comentadas."""


def leer_entero(texto):
    """Convierte texto de usuario a int: " 42\n" -> 42, "3.9" -> 3 (trunca)."""
    # strip() elimina espacios y saltos; float() acepta "42" y "3.9";
    # int() sobre un float trunca hacia cero.
    return int(float(texto.strip()))


def dividir_cuenta(total, personas, propina_pct):
    """Importe por persona con la propina (%) incluida, redondeado a 2 decimales."""
    total_con_propina = total * (1 + propina_pct / 100)
    return round(total_con_propina / personas, 2)


def fila_puerto(servicio, puerto):
    """Devuelve "servicio" alineado a la izquierda (8) + "|" + puerto a la derecha (5)."""
    # <8 : izquierda en 8 caracteres; >5 : derecha en 5.
    return f"{servicio:<8}|{puerto:>5}"


def hosts_por_prefijo(prefijo):
    """Hosts usables de una red IPv4 /prefijo: 2**(32-prefijo) - 2."""
    # Se restan 2 direcciones: la de red y la de broadcast.
    return 2 ** (32 - prefijo) - 2


def enmascarar(secreto):
    """Deja visibles el primer y el último carácter y cambia el resto por "*"."""
    # secreto[0] primero, secreto[-1] último, len(secreto) - 2 asteriscos en medio.
    return secreto[0] + "*" * (len(secreto) - 2) + secreto[-1]
