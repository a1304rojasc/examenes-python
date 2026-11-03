"""Bloque 07 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 07 dificil
"""


import struct


def parsear_cabecera(datos):
    """Cabecera propia de 12 bytes big-endian: firma, versión y total de registros."""
    raise NotImplementedError("Implementa parsear_cabecera")


def cabecera_elf(datos):
    """Clase, endianness y tipo de un encabezado ELF."""
    raise NotImplementedError("Implementa cabecera_elf")


def resumen_pcap(datos):
    """Lista de (segundos, longitud_capturada) por cada paquete del PCAP."""
    raise NotImplementedError("Implementa resumen_pcap")


def paquetes_grandes(datos, umbral):
    """Cuántos paquetes tienen longitud capturada estrictamente mayor que 'umbral'."""
    raise NotImplementedError("Implementa paquetes_grandes")


def flags_activos(valor):
    """Lista de indicadores TCP activos, en orden de bit (FIN, SYN, ...)."""
    raise NotImplementedError("Implementa flags_activos")
