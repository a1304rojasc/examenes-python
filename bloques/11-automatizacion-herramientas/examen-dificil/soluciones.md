# Bloque 11 · Examen difícil — Soluciones (teoría)

1. Porque el tipo propio valida en el momento de parsear: si el valor es inválido, `argparse` lo rechaza con un mensaje de uso claro antes de que el programa haga nada. Comprobarlo después dispersa la validación y permite que lleguen datos malos al núcleo.
2. Un fallo de validación temprano es controlado: explica qué está mal y no deja el sistema a medias. Reventar a mitad puede dejar archivos o estados inconsistentes y da un error confuso para el usuario.
3. Porque son niveles con un orden de severidad. Fijar un umbral (p. ej. WARNING) significa "muéstrame todo lo que sea igual o más grave": basta comparar la posición de cada nivel en ese orden.
4. Es cerrar el archivo de log actual y empezar otro (por tamaño o por fecha), archivando o borrando los antiguos. Evita que el log crezca sin límite y llene el disco.
5. Evita repetir trabajo y peticiones idénticas: ahorra tiempo, cuota y dinero, y reduce la carga sobre el servicio externo. Es más rápido y más respetuoso.
6. Permite comprobar que, tras varias llamadas con la misma clave, el cliente real solo se invocó **una vez**: así verificas que el cacheo funciona sin depender de la API real.
7. Porque los datos externos pueden venir con formatos inesperados, campos ausentes, tipos distintos o valores maliciosos. Validar y normalizar evita errores y entradas peligrosas aguas abajo.
8. Si falta un campo, acceder a él lanza una excepción y la herramienta falla; peor aún, un valor manipulado podría provocar comportamientos no previstos. Hay que acceder de forma defensiva y comprobar.
9. Las fuentes solapan indicadores y a veces incluyen errores (IPs mal formadas, dominios en mayúsculas). Deduplicar evita contar lo mismo varias veces y descartar los inválidos evita falsos positivos y fallos.
10. Para no saturar la API (que puede bloquearte o cobrarte de más) y para comportarse como un buen cliente. Además muchas APIs imponen límites y devuelven errores si se superan.
