# Bloque 12 · Examen fácil — Soluciones (teoría)

1. Son distribuciones de Linux orientadas a seguridad que vienen con cientos de herramientas de pentesting y análisis preinstaladas y configuradas. Se usan en auditorías autorizadas, laboratorios y formación.
2. Porque dan acceso de bajo nivel al sistema: crear paquetes en bruto o escuchar en puertos privilegiados (<1024) podría afectar a la red y a otros servicios, así que el sistema operativo lo restringe a administradores.
3. Para limitar el daño si algo falla o es comprometido: un proceso con privilegios mínimos no puede tocar más de lo necesario. Ejecutar todo como root convierte cualquier error o exploit en un compromiso total.
4. Un "Capture The Flag" es una competición de retos de seguridad donde se buscan "banderas" resolviendo problemas de criptografía, web, reversing, forense, etc. Entrena resolución de problemas y técnicas en un entorno legal y controlado.
5. Porque solo hay 256 claves posibles; se prueban todas en un instante y se reconoce la correcta porque produce texto legible o la bandera esperada.
6. Es una biblioteca de Python para escribir exploits y resolver retos (sobre todo de CTF): construye payloads, se conecta a procesos o servicios y automatiza la interacción. Su uso legítimo es CTF, investigación y pruebas autorizadas.
7. Python actúa de "pegamento": lanza módulos, les pasa opciones y, sobre todo, **parsea** y correlaciona sus resultados para generar informes o encadenar pasos de forma automática.
8. Un SOC (Security Operations Center) es el equipo/centro que vigila la seguridad de una organización. Un SIEM es la plataforma que recoge, normaliza y correlaciona los registros y eventos para generar alertas.
9. Es relacionar eventos individuales (de distintas fuentes o momentos) para reconocer un patrón que por separado no se vería: p. ej. muchos fallos de login de una IP seguidos de un acceso correcto.
10. Porque aplicarlas contra sistemas de terceros sin permiso es ilegal y puede causar daños. Los CTF y los laboratorios propios ofrecen un espacio seguro y legal; fuera de ahí se necesita autorización por escrito.
