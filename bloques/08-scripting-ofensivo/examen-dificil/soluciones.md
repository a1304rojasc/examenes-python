# Bloque 8 · Examen difícil — Soluciones (teoría)

1. El número de combinaciones es (alfabeto)^(longitud); cada carácter extra multiplica el total por el tamaño del alfabeto. Ese crecimiento exponencial hace que unas pocas posiciones más vuelvan el ataque inviable, por eso se exigen contraseñas largas.
2. La entropía en bits mide la incertidumbre: aproximadamente `longitud × log2(tamaño del alfabeto)`. Cuantos más bits, más combinaciones equiprobables y más cuesta adivinarla; permite comparar contraseñas de forma homogénea.
3. Las personas eligen contraseñas predecibles (palabras, nombres, años, sustituciones típicas como `a→@`). Un diccionario con reglas prueba primero esas variantes, mucho menos numerosas que todo el espacio, así que acierta antes.
4. Limitar los intentos por unidad de tiempo y aumentar el retardo tras cada fallo reduce drásticamente los intentos/segundo efectivos. Un ataque que sería horas pasa a ser años, y además genera alertas.
5. El de **mutación** parte de entradas válidas y las altera; el de **generación** crea entradas desde cero según un modelo del formato. En ambos buscas entradas que provoquen fallos (excepciones, cuelgues, corrupción) que delaten errores o vulnerabilidades.
6. Los campos ocultos y el token CSRF forman parte de lo que el servidor espera recibir; para enviar una petición válida (en pruebas autorizadas) hay que incluirlos. Además revelan cómo protege el formulario contra CSRF.
7. Porque el cliente está bajo control del usuario: puede llamar a cualquier endpoint directamente (curl, scripts). La única frontera fiable es la comprobación de permisos en el servidor.
8. Es mantener varias versiones de la API (v1, v2…) para no romper clientes. Las versiones antiguas suelen quedar sin mantenimiento ni los últimos controles de seguridad, y siguen accesibles: un objetivo fácil.
9. Los mismos datos llegan en formas distintas (mayúsculas, `www`, barras finales, duplicados). Normalizar y deduplicar evita contar lo mismo varias veces y hace fiables los análisis posteriores.
10. En un *bug bounty* hay **autorización** y reglas: buscar y reportar el fallo es legal y bienvenido. La misma técnica sin permiso es acceso no autorizado: ilegal, aunque la intención sea "ayudar".
