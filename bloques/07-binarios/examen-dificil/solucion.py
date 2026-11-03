"""Bloque 7 · Examen difícil — soluciones comentadas."""
import struct

_MAGIA_CAPTURA = 0x1A2B3C4D
_FLAGS_TCP = ["FIN", "SYN", "RST", "PSH", "ACK", "URG"]


def parsear_cabecera(datos):
    """Cabecera propia de 12 bytes big-endian: firma, versión y total de registros."""
    if len(datos) < 12:
        raise ValueError("cabecera incompleta")
    firma, mayor, menor, total = struct.unpack(">IHHI", datos[:12])
    if firma != _MAGIA_CAPTURA:
        raise ValueError("firma no reconocida")
    return {"version": (mayor, menor), "total": total}


def cabecera_elf(datos):
    """Clase, endianness y tipo de un encabezado ELF."""
    if len(datos) < 18 or datos[:4] != b"\x7fELF":
        raise ValueError("no es un ELF")
    clase = {1: 32, 2: 64}.get(datos[4])
    endian = {1: "little", 2: "big"}.get(datos[5])
    if clase is None or endian is None:
        raise ValueError("ELF inválido")
    orden = "<" if endian == "little" else ">"   # el resto depende de este byte
    (tipo,) = struct.unpack(orden + "H", datos[16:18])
    return {"clase": clase, "endian": endian, "tipo": tipo}


def _orden_pcap(datos):
    """Deduce el orden de bytes de un PCAP a partir de su magic."""
    if datos[:4] == b"\xa1\xb2\xc3\xd4":
        return ">"
    if datos[:4] == b"\xd4\xc3\xb2\xa1":
        return "<"
    raise ValueError("no es un PCAP")


def resumen_pcap(datos):
    """Lista de (segundos, longitud_capturada) por cada paquete del PCAP."""
    orden = _orden_pcap(datos)
    paquetes = []
    pos = 24                                  # saltamos la cabecera global
    while pos + 16 <= len(datos):
        ts_sec, ts_usec, incluida, original = struct.unpack(orden + "IIII", datos[pos:pos + 16])
        pos += 16 + incluida                  # avanzamos al siguiente registro
        paquetes.append((ts_sec, incluida))
    return paquetes


def paquetes_grandes(datos, umbral):
    """Cuántos paquetes tienen longitud capturada estrictamente mayor que 'umbral'."""
    return sum(1 for _, incluida in resumen_pcap(datos) if incluida > umbral)


def flags_activos(valor):
    """Lista de indicadores TCP activos, en orden de bit (FIN, SYN, ...)."""
    return [nombre for i, nombre in enumerate(_FLAGS_TCP) if (valor >> i) & 1]
