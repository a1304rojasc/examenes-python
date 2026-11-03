# Bloque 11 · Automatización y herramientas — Repaso espaciado

> Mezcla 11.1 CLI (argparse) · 11.2 Logging · 11.3 Testing/mocking · 11.4 Packaging · 11.5 APIs de seguridad.
> Datos de ejemplo; **no se llama a ninguna API real ni se usan claves**.

**1. (11.1 + 11.3) ¿Por qué diseñar una herramienta con `argparse` y una función `main(argv)` facilita además las pruebas automáticas?**
`argparse` define y valida los argumentos de forma declarativa y genera ayuda. Si `main` recibe `argv` como parámetro (en vez de leer `sys.argv`), el test puede llamarla con cualquier lista de argumentos y comprobar su comportamiento sin lanzar un proceso.

**2. (11.2) ¿Qué ventaja tiene el logging con niveles y formato estructurado frente a usar `print`?**
Permite filtrar por severidad (DEBUG/INFO/WARNING/ERROR), enviar los mensajes a distintos destinos (archivo, consola) con rotación, e incluir campos (hora, módulo, IP) de forma consistente. Un formato estructurado se puede analizar luego automáticamente; `print` no ofrece nada de eso.

**3. (11.3 + 11.5) Al probar una herramienta que consulta una API de seguridad (VirusTotal, Shodan), ¿por qué se usa un "mock" en vez de llamar a la API real?**
Para que las pruebas sean rápidas, deterministas y gratis, sin depender de la red ni gastar cuota o exponer la clave. El mock simula la respuesta y así se prueba la lógica de la herramienta, no la API.

**4. (11.5) ¿Por qué el modelo de k-anonimato de "Have I Been Pwned" permite comprobar una contraseña sin enviarla?**
Se envía solo los primeros caracteres del hash SHA-1; el servicio devuelve todos los sufijos que empiezan igual. El cliente busca el suyo en esa lista localmente, de modo que la contraseña (ni su hash completo) nunca sale del equipo.

**5. (11.4) ¿Para qué sirven `pyproject.toml` y empaquetar una herramienta, y qué cuidado hay con incluir secretos?**
Definen metadatos y dependencias para instalar y distribuir la herramienta de forma reproducible. Nunca se empaquetan claves ni secretos: se leen de variables de entorno o de un archivo de configuración fuera del repositorio.
