"""Bloque 02 · Examen difícil — soluciones comentadas."""


def validar_puerto(texto):
    """Devuelve "inválido", "reservado" (<1024) o "válido" para un puerto en texto."""
    texto = texto.strip()
    # isdigit() falla con "", "-1", "8o80"... así evitamos el ValueError de int().
    if not texto.isdigit():
        return "inválido"
    puerto = int(texto)
    if puerto < 1 or puerto > 65535:
        return "inválido"
    if puerto < 1024:
        return "reservado"   # puertos "bien conocidos" (requieren privilegios)
    return "válido"


def intento_exitoso(intentos, correcta, max_intentos=3):
    """Número de intento (desde 1) que acierta, o 0 si se bloquea o se acaban."""
    numero = 0
    for clave in intentos:
        numero += 1
        if numero > max_intentos:
            return 0          # bloqueado: se superó el máximo
        if clave == correcta:
            return numero
    return 0                  # la lista terminó sin acertar


def es_primo(n):
    """True si n es primo. Prueba divisores impares hasta la raíz cuadrada."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:   # equivale a divisor <= sqrt(n)
        if n % divisor == 0:
            return False
        divisor += 2                # solo impares
    return True


def fortaleza(password):
    """Puntuación 0-4: longitud>=8, mayúscula, dígito y símbolo (+1 cada uno)."""
    tiene_mayus = tiene_digito = tiene_simbolo = False
    for c in password:
        if c.isupper():
            tiene_mayus = True
        elif c.isdigit():
            tiene_digito = True
        elif not c.isalnum():
            tiene_simbolo = True
    # True vale 1 y False vale 0 al sumar.
    return (len(password) >= 8) + tiene_mayus + tiene_digito + tiene_simbolo


def tabla_multiplicar(n, hasta):
    """Líneas "n x i = r" de 1 a hasta, unidas con "\\n" (sin salto final)."""
    texto = ""
    for i in range(1, hasta + 1):
        if i > 1:
            texto += "\n"   # separador solo entre líneas
        texto += f"{n} x {i} = {n * i}"
    return texto
