"""Bloque 08 · Examen difícil — soluciones comentadas."""
import hashlib
import hmac
import secrets

# Frecuencia aproximada (%) de las letras en español (sin ñ ni tildes).
FRECUENCIAS_ES = {
    "a": 12.5, "b": 1.4, "c": 4.7, "d": 5.9, "e": 13.7, "f": 0.7, "g": 1.0, "h": 0.7,
    "i": 6.3, "j": 0.4, "k": 0.1, "l": 5.0, "m": 3.2, "n": 6.7, "o": 8.7, "p": 2.5,
    "q": 0.9, "r": 6.9, "s": 8.0, "t": 4.6, "u": 3.9, "v": 0.9, "w": 0.1, "x": 0.2,
    "y": 0.9, "z": 0.5,
}


def _desplazar(c, d):
    """Desplaza una letra ASCII d posiciones (auxiliar)."""
    base = ord("a") if c.islower() else ord("A")
    return chr((ord(c) - base + d) % 26 + base)


def vigenere(texto, clave, descifrar=False):
    """Cifra (o descifra) Vigenère; la clave solo avanza con letras A-Z/a-z."""
    desplazamientos = [ord(k) - ord("a") for k in clave.lower()]
    signo = -1 if descifrar else 1
    resultado, i = [], 0
    for c in texto:
        if c.isascii() and c.isalpha():
            resultado.append(_desplazar(c, signo * desplazamientos[i % len(desplazamientos)]))
            i += 1                     # solo avanzamos la clave con letras
        else:
            resultado.append(c)
    return "".join(resultado)


def romper_cesar(cifrado):
    """(desplazamiento, texto_claro) con menor chi-cuadrado frente al español."""
    mejor = None
    for d in range(26):
        candidato = "".join(_desplazar(c, -d) if c.isascii() and c.isalpha() else c for c in cifrado)
        letras = [c for c in candidato.lower() if c in FRECUENCIAS_ES]
        total = len(letras) or 1
        chi2 = 0.0
        for letra, esperado_pct in FRECUENCIAS_ES.items():
            esperado = total * esperado_pct / 100
            observado = letras.count(letra)
            chi2 += (observado - esperado) ** 2 / esperado
        if mejor is None or chi2 < mejor[0]:
            mejor = (chi2, d, candidato)
    return mejor[1], mejor[2]


def hash_password(password, sal=None, iteraciones=100_000):
    """Devuelve "pbkdf2_sha256$iter$sal_hex$hash_hex" usando PBKDF2-HMAC-SHA256."""
    if sal is None:
        sal = secrets.token_bytes(16)    # sal aleatoria y única por contraseña
    derivada = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), sal, iteraciones)
    return f"pbkdf2_sha256${iteraciones}${sal.hex()}${derivada.hex()}"


def verificar_password(password, almacenado):
    """True si password corresponde al hash almacenado (tiempo constante)."""
    try:
        algoritmo, iteraciones, sal_hex, _ = almacenado.split("$")
    except ValueError:
        return False
    if algoritmo != "pbkdf2_sha256":
        return False
    recalculado = hash_password(password, bytes.fromhex(sal_hex), int(iteraciones))
    return hmac.compare_digest(recalculado, almacenado)


def firmar(mensaje, clave):
    """HMAC-SHA256 en hexadecimal del mensaje con la clave."""
    return hmac.new(clave.encode("utf-8"), mensaje.encode("utf-8"), hashlib.sha256).hexdigest()


def verificar_firma(mensaje, clave, firma):
    """True si la firma es válida (comparación en tiempo constante)."""
    return hmac.compare_digest(firmar(mensaje, clave), firma)


def auditar_debiles(hashes, diccionario):
    """{usuario: contraseña débil} para usuarios cuyo sha256 está en el diccionario."""
    # Precalcular: un hash por palabra (no uno por palabra y usuario).
    tabla = {hashlib.sha256(p.encode("utf-8")).hexdigest(): p for p in diccionario}
    return {usuario: tabla[h] for usuario, h in hashes.items() if h in tabla}
