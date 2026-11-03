"""Bloque 07 · Examen fácil — soluciones comentadas."""
import ipaddress
import socket
from urllib.parse import urlsplit

PUERTOS_POR_DEFECTO = {"http": 80, "https": 443}


def es_ip_valida(texto):
    """True si texto es una IPv4 o IPv6 válida."""
    try:
        ipaddress.ip_address(texto)   # acepta v4 y v6
        return True
    except ValueError:
        return False


def en_red(ip, cidr):
    """True si la IP pertenece a la red CIDR."""
    # El operador "in" está definido entre direcciones y redes.
    return ipaddress.ip_address(ip) in ipaddress.ip_network(cidr, strict=False)


def info_red(cidr):
    """{"red", "broadcast", "mascara", "hosts"} de una red CIDR."""
    # strict=False permite "192.0.2.77/24" (pone a 0 los bits de host).
    red = ipaddress.ip_network(cidr, strict=False)
    return {
        "red": str(red.network_address),
        "broadcast": str(red.broadcast_address),
        "mascara": str(red.netmask),
        "hosts": sum(1 for _ in red.hosts()),   # hosts() excluye red y broadcast
    }


def eco_socketpair(mensaje):
    """Envía mensaje por un socket de un par conectado y devuelve lo recibido."""
    a, b = socket.socketpair()      # dos sockets ya conectados entre sí (local)
    with a, b:                      # with cierra ambos al terminar
        a.sendall(mensaje.encode("utf-8"))   # por la red viajan bytes, no str
        datos = b.recv(4096)
    return datos.decode("utf-8")


def parsear_url(url):
    """(esquema, host, puerto) de una URL; puerto 80/443 por defecto."""
    partes = urlsplit(url)
    puerto = partes.port or PUERTOS_POR_DEFECTO.get(partes.scheme)
    return partes.scheme, partes.hostname, puerto
