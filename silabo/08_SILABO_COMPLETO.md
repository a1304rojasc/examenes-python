# SÍLABO: PYTHON 0 → CIBERSEGURIDAD (Bloques 0–12)
 
> Referencia de contenido del proyecto "Programación". Súbelo al proyecto equivalente en ChatGPT. **Estado a la fecha del traspaso:** Bloques 0–5 cerrados. Siguiente: Bloque 6\. **Orden recomendado por el autor del sílabo:** 0 → 1 → 2 → 3 → 5 → 6 → 7 → 4 → 8 → 9 → 10 → 11 → 12\. Los Bloques 4 y 11 pueden intercalarse cuando se necesiten en práctica. **Nota:** Human avanzó en orden 0→1→2→3→4→5, así que el Bloque 4 (Concurrencia) ya está hecho antes de lo que sugiere el orden recomendado. Tras el Bloque 5, lo que sigue es **6 → 7 → 8** (el 4 ya está cerrado).
 
---
 
## BLOQUE 0 — FUNDAMENTOS DE PYTHON ✅
 
- **0.1 Entorno y herramientas** — Instalación Python, pip, venv, VS Code/PyCharm, REPL, ejecución de scripts.  
- **0.2 Tipos de datos primitivos** — int, float, str, bool. Conversión de tipos. Representación en memoria.  
- **0.3 Variables y operadores** — Asignación, aritméticos, comparación, lógicos, bitwise, precedencia.  
- **0.4 Strings a fondo** — Indexing, slicing, métodos, f-strings, encoding (ASCII, UTF-8, bytes vs str).  
- **0.5 Condicionales** — if/elif/else, expresiones ternarias, short-circuit evaluation.  
- **0.6 Bucles** — for, while, break, continue, else en bucles, range(), enumerate(), zip().  
- **0.7 Funciones** — Definición, parámetros, \*args/\*\*kwargs, valores por defecto, scope, retorno múltiple.  
- **0.8 Manejo de errores** — try/except/finally, tipos de excepciones, raise, excepciones personalizadas.
 
## BLOQUE 1 — ESTRUCTURAS DE DATOS ✅
 
- **1.1 Listas** — Operaciones, métodos, list comprehensions, slicing profundo.  
- **1.2 Tuplas** — Inmutabilidad, unpacking, uso como clave de dict.  
- **1.3 Diccionarios** — CRUD, métodos, dict comprehensions, defaultdict, Counter.  
- **1.4 Conjuntos (sets)** — Operaciones de conjuntos, diferencia simétrica, frozenset.  
- **1.5 Pilas, colas y deque** — collections.deque, implementación manual de stack/queue.
 
## BLOQUE 2 — MÓDULOS Y ARCHIVOS ✅
 
- **2.1 Sistema de módulos** — import, from-import, módulos propios, **name**, packages, **init**.py.  
- **2.2 Archivos de texto** — open(), modos, with statement, lectura/escritura/append.  
- **2.3 Archivos binarios** — Lectura/escritura en binario, struct, bytearray.  
- **2.4 JSON y CSV** — json module, csv module, serialización/deserialización.  
- **2.5 Paths y sistema de archivos** — os, pathlib, shutil, manipulación de rutas multiplataforma.
 
## BLOQUE 3 — PYTHON INTERMEDIO ✅
 
- **3.1 Orientación a objetos** — Clases, objetos, **init**, self, métodos, atributos de clase vs instancia.  
- **3.2 Herencia y polimorfismo** — Herencia simple/múltiple, MRO, super(), métodos abstractos (ABC).  
- **3.3 Dunder methods** — **str**, **repr**, **len**, **eq**, **iter**, **enter**/**exit**.  
- **3.4 Decoradores** — Funciones de orden superior, closures, @staticmethod, @classmethod, decoradores propios.  
- **3.5 Iteradores y generadores** — **iter**/**next**, yield, generator expressions, lazy evaluation.  
- **3.6 Expresiones regulares** — re module, patrones, grupos, search/match/findall/sub, flags.
 
## BLOQUE 4 — CONCURRENCIA Y SISTEMA ✅
 
- **4.1 Procesos y subprocesos** — subprocess module, comunicación con shell, capture output.  
- **4.2 Threading** — threading module, locks, race conditions, GIL.  
- **4.3 Multiprocessing** — multiprocessing module, Pool, Queue entre procesos, IPC.  
- **4.4 Asyncio** — async/await, event loop, coroutines, aiohttp básico.  
- **4.5 Señales y OS** — signal module, manipulación de PID, variables de entorno, sys module.
 
## BLOQUE 5 — REDES EN PYTHON ✅ *(entregado de golpe; ver nota de consolidación en el handoff)*
 
- **5.1 Sockets TCP** — socket module, servidor/cliente TCP, bind/listen/accept/connect.  
- **5.2 Sockets UDP** — Diferencias TCP vs UDP, implementación básica.  
- **5.3 Protocolo HTTP a bajo nivel** — Construcción manual de peticiones HTTP, parsing de respuestas.  
- **5.4 requests y httpx** — GET/POST/PUT/DELETE, headers, cookies, sesiones, autenticación básica.  
- **5.5 Scapy — fundamentos** — Captura de paquetes, construcción de paquetes, análisis de capas.  
- **5.6 DNS y resolución de nombres** — socket.getaddrinfo, dnspython, análisis de registros DNS.
 
---
 
## BLOQUE 6 — CRIPTOGRAFÍA CON PYTHON ◀ SIGUIENTE
 
- **6.1 Hashing** — hashlib: MD5, SHA-1, SHA-256, SHA-3. Integridad de archivos.  
- **6.2 Cifrado simétrico** — cryptography library, AES (CBC, GCM), padding, IV/nonce.  
- **6.3 Cifrado asimétrico** — RSA, generación de claves, cifrado/descifrado, firma digital.  
- **6.4 Curvas elípticas** — ECDSA, ECDH, diferencia con RSA, casos de uso.  
- **6.5 TLS/SSL con Python** — ssl module, verificación de certificados, handshake, inspección de certs.  
- **6.6 Esteganografía básica** — Ocultamiento de datos en imágenes con PIL/Pillow, LSB.
 
## BLOQUE 7 — ANÁLISIS Y MANIPULACIÓN DE DATOS BINARIOS
 
- **7.1 Binario y hexadecimal** — bin(), hex(), operaciones bitwise aplicadas, máscaras.  
- **7.2 struct module** — Pack/unpack de formatos binarios, big-endian vs little-endian.  
- **7.3 Análisis de archivos** — Magic bytes, identificación de formato, parseo de headers (PE, ELF, ZIP).  
- **7.4 Análisis de tráfico (PCAP)** — Lectura de archivos .pcap con scapy/dpkt, filtrado de paquetes.
 
## BLOQUE 8 — SCRIPTING OFENSIVO
 
- **8.1 Automatización de reconocimiento** — Whois, OSINT con Python, scraping de datos públicos, shodan API.  
- **8.2 Escáneres de puertos** — Implementación con sockets, threading para velocidad, banner grabbing.  
- **8.3 Fuerza bruta y diccionario** — Ataques a servicios (SSH, FTP, HTTP) con paramiko/ftplib/requests.  
- **8.4 Fuzzing básico** — Envío de entradas malformadas, detección de crashes, boofuzz introducción.  
- **8.5 Web scraping y crawling** — BeautifulSoup, lxml, crawling de formularios, detección de parámetros.  
- **8.6 Explotación de APIs** — Enumeración de endpoints, bypass de autenticación débil, inyecciones en JSON.
 
## BLOQUE 9 — ANÁLISIS DE VULNERABILIDADES WEB
 
- **9.1 SQL Injection con Python** — Detección manual, automatización básica, comparación con sqlmap.  
- **9.2 XSS automatizado** — Detección de puntos de inyección, payloads, análisis de respuesta.  
- **9.3 SSRF y redirecciones abiertas** — Identificación, explotación con requests, bypass de filtros comunes.  
- **9.4 Parsing y análisis de HTML** — Extracción de formularios, tokens CSRF, campos ocultos.
 
## BLOQUE 10 — ANÁLISIS FORENSE Y MALWARE
 
- **10.1 Análisis estático de scripts** — Ofuscación Python, deobfuscación, ast module, análisis de imports sospechosos.  
- **10.2 Análisis de binarios PE/ELF** — pefile, pyelftools, extracción de strings, análisis de secciones.  
- **10.3 Análisis de memoria** — volatility3 con Python, extracción de procesos, análisis de dumps.  
- **10.4 Análisis de logs** — Parsing de logs de sistema/web con regex, detección de patrones de ataque.  
- **10.5 Hashing y firma de archivos** — Comparación contra bases de datos (VirusTotal API), YARA rules con Python.
 
## BLOQUE 11 — AUTOMATIZACIÓN Y HERRAMIENTAS
 
- **11.1 CLI tools con argparse** — Diseño de herramientas de línea de comandos, subcommands, validación.  
- **11.2 Logging profesional** — logging module, niveles, handlers, rotación, formato estructurado.  
- **11.3 Testing de herramientas de seguridad** — unittest, pytest, mocking de conexiones de red.  
- **11.4 Packaging y distribución** — setup.py, pyproject.toml, creación de ejecutables con PyInstaller.  
- **11.5 Interacción con APIs de seguridad** — VirusTotal, Shodan, Have I Been Pwned, Censys — autenticación y parsing.
 
## BLOQUE 12 — PYTHON EN ENTORNOS DE SEGURIDAD
 
- **12.1 Python en Kali/Parrot OS** — Diferencias de entorno, permisos, integración con herramientas nativas.  
- **12.2 Integración con Metasploit** — pymetasploit3, automatización de módulos, parseo de resultados.  
- **12.3 Scripts para CTF** — Patrones comunes en CTF, pwntools básico, resolución de challenges.  
- **12.4 Python en análisis de redes (SOC)** — Automatización de alertas, correlación de eventos, integración con SIEM.