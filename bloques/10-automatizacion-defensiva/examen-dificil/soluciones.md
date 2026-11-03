# Bloque 10 · Examen difícil — Soluciones (teoría)

1. **O(n log n)** (por la ordenación; el recorrido es O(n)) frente a **O(n²)** comparando todos los pares.
2. **No**, ningún IP supera el umbral. Agregar por **usuario objetivo**, por **red** (/24) o el total global de fallos en la ventana (ataque distribuido / *password spraying*).
3. Porque te quedarías **sin acceso** para responder al incidente. Con una **allowlist** de redes que se excluyen siempre antes de generar reglas.
4. El atacante podría provocar el bloqueo de IPs **legítimas** (denegación de servicio inducida). Hay que parsear con regex estrictas, validar con `ipaddress`, usar allowlist y caducidad de bloqueos.
5. Se puede **probar** fácilmente (pasar listas en los tests) y reutilizar desde otro código.
6. Para que otros programas (SIEM, scripts, `jq`) lo **consuman automáticamente**.
7. FP: alerta sin ataque real; FN: ataque sin alerta. Subir el umbral **reduce FP** pero **aumenta FN**.
8. Introducir errores deliberados (mutantes) en el código y comprobar que los tests **los detectan**; mide la calidad de los tests, no solo su cobertura.
9. Porque los errores de límite solo aparecen **en el valor exacto del límite**; hay que probar justo en, por debajo y por encima.
10. **fail2ban**, **sshguard** (o CrowdSec). Limitación: solo ven lo que se registra, reaccionan **después** de los intentos y son evadibles con ataques lentos o distribuidos.
