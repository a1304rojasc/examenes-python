"""5.5 · Paquetes con Scapy — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Lee los enunciados en leccion.md.
Corrige con:  pytest lecciones/05-redes/5.5-paquetes-scapy
"""


def construir_sonda(ip_destino, puerto, puerto_origen=40000):
    """Primer paquete de una conexión TCP. Ejercicio 1."""
    raise NotImplementedError("Implementa construir_sonda")


def capas(trama):
    """Lista de nombres de capas, de fuera hacia dentro. Ejercicio 2."""
    raise NotImplementedError("Implementa capas")


def datos_de_aplicacion(trama):
    """Bytes de la aplicación, o b''. Ejercicio 2."""
    raise NotImplementedError("Implementa datos_de_aplicacion")


def sospechosos_de_escaneo(ruta, umbral=10):
    """{ip: puertos distintos} de quien supera el umbral. Ejercicio 3."""
    raise NotImplementedError("Implementa sospechosos_de_escaneo")
