import struct

import pytest


def test_ej1_cabecera(m):
    datos = struct.pack(">IHHI", 0x1A2B3C4D, 2, 5, 128) + b"resto"
    assert m.parsear_cabecera(datos) == {"version": (2, 5), "total": 128}
    with pytest.raises(ValueError):
        m.parsear_cabecera(struct.pack(">IHHI", 0xDEADBEEF, 1, 0, 1))
    with pytest.raises(ValueError):
        m.parsear_cabecera(b"\x1a\x2b")


def test_ej2_elf(m):
    elf64 = b"\x7fELF" + bytes([2, 1]) + b"\x00" * 10 + struct.pack("<H", 2)
    assert m.cabecera_elf(elf64) == {"clase": 64, "endian": "little", "tipo": 2}
    elf32be = b"\x7fELF" + bytes([1, 2]) + b"\x00" * 10 + struct.pack(">H", 3)
    assert m.cabecera_elf(elf32be) == {"clase": 32, "endian": "big", "tipo": 3}
    with pytest.raises(ValueError):
        m.cabecera_elf(b"MZ\x90\x00 no soy elf")


def _pcap(orden, paquetes):
    cab = struct.pack(orden + "IHHiIII", 0xA1B2C3D4, 2, 4, 0, 0, 65535, 1)
    cuerpo = b""
    for ts, datos in paquetes:
        cuerpo += struct.pack(orden + "IIII", ts, 0, len(datos), len(datos)) + datos
    return cab + cuerpo


def test_ej3_pcap(m):
    for orden in (">", "<"):
        datos = _pcap(orden, [(100, b"abc"), (200, b"hola mundo"), (300, b"")])
        assert m.resumen_pcap(datos) == [(100, 3), (200, 10), (300, 0)]
    assert m.resumen_pcap(_pcap(">", [])) == []


def test_ej3_magic_invalido(m):
    with pytest.raises(ValueError):
        m.resumen_pcap(b"\x00\x11\x22\x33" + b"\x00" * 40)


def test_ej4_grandes(m):
    datos = _pcap("<", [(1, b"x" * 100), (2, b"y" * 40), (3, b"z" * 1500), (4, b"w" * 41)])
    assert m.paquetes_grandes(datos, 40) == 3
    assert m.paquetes_grandes(datos, 100) == 1
    assert m.paquetes_grandes(datos, 2000) == 0


def test_ej5_flags(m):
    assert m.flags_activos(0b000010) == ["SYN"]
    assert m.flags_activos(0b010010) == ["SYN", "ACK"]
    assert m.flags_activos(0b000000) == []
    assert m.flags_activos(0b111111) == ["FIN", "SYN", "RST", "PSH", "ACK", "URG"]
