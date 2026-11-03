"""5.6 · DNS y resolución de nombres — solución oficial."""

import socket

import dns.message
import dns.rdatatype
import dns.zone


def direcciones_ipv4(nombres):
    """{nombre: IPv4 ordenadas y sin repetir} usando el resolvedor del sistema."""
    resultado = {}
    for nombre in nombres:
        try:
            infos = socket.getaddrinfo(nombre, None, family=socket.AF_INET)
        except socket.gaierror:
            resultado[nombre] = []
            continue
        resultado[nombre] = sorted({info[4][0] for info in infos})
    return resultado


def registros(respuesta_binaria):
    """(nombre, tipo, valor, ttl) de la sección answer de un mensaje DNS en binario."""
    mensaje = dns.message.from_wire(respuesta_binaria)
    filas = []
    for rrset in mensaje.answer:
        nombre = rrset.name.to_text(omit_final_dot=True)
        tipo = dns.rdatatype.to_text(rrset.rdtype)
        for rdata in rrset:
            filas.append((nombre, tipo, rdata.to_text(), rrset.ttl))
    return sorted(filas)


def _texto_txt(rdata):
    return b"".join(rdata.strings).decode()


def politica_correo(texto_zona, origen):
    """MX por preferencia, SPF y nivel de riesgo según el mecanismo 'all'."""
    zona = dns.zone.from_text(texto_zona, origin=origen, relativize=False)
    raiz = zona.get_node(dns.name.from_text(origen))

    mx = []
    spf = None
    if raiz is not None:
        conjunto_mx = raiz.get_rdataset(dns.rdataclass.IN, dns.rdatatype.MX)
        if conjunto_mx:
            mx = [r.exchange.to_text(omit_final_dot=True) for r in sorted(conjunto_mx, key=lambda r: r.preference)]
        conjunto_txt = raiz.get_rdataset(dns.rdataclass.IN, dns.rdatatype.TXT)
        for r in conjunto_txt or []:
            texto = _texto_txt(r)
            if texto.lower().startswith("v=spf1"):
                spf = texto
                break

    if spf is None:
        riesgo = "alto"
    else:
        final = spf.split()[-1].lower()
        if final in ("+all", "all"):
            riesgo = "alto"
        elif final in ("~all", "?all"):
            riesgo = "medio"
        elif final == "-all":
            riesgo = "bajo"
        else:
            riesgo = "medio"  # sin mecanismo 'all' explícito: se comporta como neutral
    return {"mx": mx, "spf": spf, "riesgo": riesgo}
