"""Bloque 12 · Examen difícil — ejercicios

Implementa cada función. No cambies los nombres ni los parámetros.
Corrige con:  python corregir.py 12 dificil
"""


import re


def romper_xor_un_byte(cifrado, pista):
    """Prueba las 256 claves de un byte; devuelve (clave, texto) que contiene 'pista'."""
    raise NotImplementedError("Implementa romper_xor_un_byte")


def alertas_fuerza_bruta(eventos, umbral, ventana):
    """IPs (ordenadas) con >= umbral eventos 'login_fallido' en alguna ventana."""
    raise NotImplementedError("Implementa alertas_fuerza_bruta")


def agrupar_alertas(alertas):
    """Agrupa por (tipo, origen) con conteo y rango temporal, ordenado."""
    raise NotImplementedError("Implementa agrupar_alertas")


def parsear_servicios(texto):
    """Lista de {puerto, servicio} para cada línea 'PUERTO/tcp open SERVICIO'."""
    raise NotImplementedError("Implementa parsear_servicios")


def generar_ciclico(longitud, n=4):
    """Cadena de 'longitud' donde cada subcadena de n (4) caracteres es única."""
    raise NotImplementedError("Implementa generar_ciclico")


def posicion_ciclico(patron, fragmento):
    """Índice donde aparece 'fragmento' en el patrón, o -1."""
    raise NotImplementedError("Implementa posicion_ciclico")
