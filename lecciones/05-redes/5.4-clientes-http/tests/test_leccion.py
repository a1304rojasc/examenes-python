"""Tests de la lección 5.4. Levantan un servidor HTTP local en 127.0.0.1."""

import base64
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

import pytest

TICKETS = [
    {"id": 1, "titulo": "VPN caída en el lab 3", "estado": "abierto"},
    {"id": 2, "titulo": "Cambiar tóner", "estado": "cerrado"},
    {"id": 3, "titulo": "Alerta de fuerza bruta en ssh", "estado": "abierto"},
    {"id": 4, "titulo": "Certificado TLS caduca", "estado": "abierto"},
]


class Manejador(BaseHTTPRequestHandler):
    fallos_pendientes = {}  # ruta -> cuántos 503 quedan
    peticiones = []

    def log_message(self, *args):
        pass

    def _responder(self, codigo, cuerpo="", tipo="application/json", extra=None):
        datos = cuerpo.encode() if isinstance(cuerpo, str) else cuerpo
        self.send_response(codigo)
        self.send_header("Content-Type", tipo)
        self.send_header("Content-Length", str(len(datos)))
        for k, v in (extra or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(datos)

    def do_GET(self):
        Manejador.peticiones.append(self.path)
        if self.path == "/estado":
            if self.headers.get("User-Agent") != "monitor-utec/1.0":
                return self._responder(403, '{"error": "cliente no autorizado"}')
            return self._responder(200, json.dumps({"servicio": "biblioteca", "ok": True}))
        if self.path == "/tickets":
            if "sesion=token-ana" not in (self.headers.get("Cookie") or ""):
                return self._responder(401, '{"error": "inicia sesion"}')
            return self._responder(200, json.dumps(TICKETS))
        if self.path.startswith("/informes/"):
            esperado = "Basic " + base64.b64encode(b"ana:s3cr3ta").decode()
            if self.headers.get("Authorization") != esperado:
                return self._responder(401, "", extra={"WWW-Authenticate": 'Basic realm="informes"'})
            if Manejador.fallos_pendientes.get(self.path, 0) > 0:
                Manejador.fallos_pendientes[self.path] -= 1
                return self._responder(503, "saturado", tipo="text/plain")
            return self._responder(200, "Informe semanal: 3 incidencias abiertas", tipo="text/plain; charset=utf-8")
        self._responder(404, "{}")

    def do_POST(self):
        largo = int(self.headers.get("Content-Length", 0))
        cuerpo = self.rfile.read(largo)
        if self.path == "/login":
            if not (self.headers.get("Content-Type") or "").startswith("application/json"):
                return self._responder(415, '{"error": "se espera JSON"}')
            datos = json.loads(cuerpo or b"{}")
            if datos == {"usuario": "ana", "clave": "s3cr3ta"}:
                return self._responder(200, '{"ok": true}', extra={"Set-Cookie": "sesion=token-ana; HttpOnly; Path=/"})
            return self._responder(401, '{"ok": false}')
        self._responder(404, "{}")


@pytest.fixture(scope="module")
def base():
    servidor = ThreadingHTTPServer(("127.0.0.1", 0), Manejador)
    hilo = threading.Thread(target=servidor.serve_forever, daemon=True)
    hilo.start()
    yield f"http://127.0.0.1:{servidor.server_address[1]}"
    servidor.shutdown()


def test_ej1_estado_con_agente(m, base):
    assert m.consultar_estado(base) == (200, True)


def test_ej1_devuelve_tupla_de_int_y_bool(m, base):
    codigo, ok = m.consultar_estado(base)
    assert type(codigo) is int and type(ok) is bool


def test_ej2_titulos_abiertos(m, base):
    assert m.titulos_abiertos(base, "ana", "s3cr3ta") == [
        "Alerta de fuerza bruta en ssh",
        "Certificado TLS caduca",
        "VPN caída en el lab 3",
    ]


def test_ej2_login_incorrecto(m, base):
    assert m.titulos_abiertos(base, "ana", "mala") is None


def test_ej3_descarga_directa(m, base):
    assert m.descargar_informe(base, "/informes/s1", "ana", "s3cr3ta") == "Informe semanal: 3 incidencias abiertas"


def test_ej3_reintenta_ante_503(m, base):
    Manejador.fallos_pendientes["/informes/s2"] = 2
    assert m.descargar_informe(base, "/informes/s2", "ana", "s3cr3ta", intentos=3) == "Informe semanal: 3 incidencias abiertas"


def test_ej3_se_rinde_al_agotar_intentos(m, base):
    Manejador.fallos_pendientes["/informes/s3"] = 5
    Manejador.peticiones.clear()
    assert m.descargar_informe(base, "/informes/s3", "ana", "s3cr3ta", intentos=3) is None
    assert Manejador.peticiones.count("/informes/s3") == 3


def test_ej3_no_reintenta_con_clave_mala(m, base):
    Manejador.peticiones.clear()
    assert m.descargar_informe(base, "/informes/s4", "ana", "mala", intentos=3) is None
    assert Manejador.peticiones.count("/informes/s4") == 1
