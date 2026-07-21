Lectura de parametros en un servlet

Resumen: explica como un servlet recoge los parametros enviados desde un formulario HTML mediante el metodo getParameter, con un ejemplo que crea un nuevo servlet a partir de uno existente y muestra los valores recibidos en la respuesta.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_06.md

Ultima actualizacion: 2026-06-24

## Objetivo

El objetivo es crear un [[td7-servlets|servlet]] capaz de leer los parametros que se envian desde un [[td6-formularios-html|formulario]] y mostrarlos en la respuesta (fuente: TD_07_06.md).

## Colocar el formulario dentro de la aplicacion

Se reutiliza un formulario HTML existente (por ejemplo, con campos de nombre y contrasena), guardando su codigo en un fichero dentro de la carpeta raiz de la aplicacion de servlets (por ejemplo, formulario.html). A diferencia de los servlets, los ficheros HTML no es necesario declararlos en el [[td7-web-xml|web.xml]]: se colocan directamente en la carpeta de la aplicacion y se accede a ellos por su nombre de fichero, sin configuracion adicional (fuente: TD_07_06.md).

Al acceder al formulario desde el navegador, conviene comprobar que los caracteres especiales se muestran correctamente, sustituyendolos por su entidad HTML correspondiente si no es asi (fuente: TD_07_06.md).

## Crear un nuevo servlet a partir de uno existente

Para crear el nuevo servlet se puede partir de una copia de un servlet anterior, cambiando el nombre del fichero y de la clase, y compilandolo de nuevo. En el formulario HTML, el atributo action debe apuntar a la direccion que respondera a este nuevo servlet. En el web.xml, hay que repetir el bloque completo servlet y servlet-mapping con el nuevo nombre; para simplificar, se puede usar el mismo nombre para la clase, el servlet-name y el url-pattern (fuente: TD_07_06.md).

Como se modifica tanto el codigo Java (que requiere recompilar) como el web.xml (que requiere reiniciar Tomcat), hay que detener y volver a arrancar el servidor, y recargar tambien la pagina del formulario en el navegador (fuente: TD_07_06.md).

## Comprobar que la peticion llega, antes de leer los parametros

Conviene comprobar que la peticion llega correctamente al servlet antes de programar la lectura de parametros. Si se usa el metodo [[td6-metodos-get-post|GET]], esto se puede verificar observando que la URL generada al enviar el formulario incluye los parametros enviados, aunque el servlet todavia no los este leyendo (fuente: TD_07_06.md).

## El metodo getParameter

Para que el servlet recoja un parametro concreto, se utiliza el metodo getParameter del objeto request, pasandole como argumento el nombre del campo tal y como se definio en el atributo name del HTML. getParameter siempre devuelve un valor de tipo String (fuente: TD_07_06.md):

```java
String nombreStr = request.getParameter("nombre").trim();
String contrasenaStr = request.getParameter("contrasena").trim();
```

Se aplica tambien el metodo trim() para eliminar espacios en blanco sobrantes al principio o al final del valor recibido. Es habitual anadir un sufijo (como Str) al nombre de la variable, para distinguir que se trata de una variable local del servlet, sin que tenga que llamarse igual que el parametro del formulario (fuente: TD_07_06.md).

## Mostrar los valores recibidos en la respuesta

Una vez leidos los parametros, se incluyen en la respuesta HTML generada por el servlet, por ejemplo dentro de parrafos (fuente: TD_07_06.md):

```java
out.println("<p>Nombre: " + nombreStr + "</p>");
out.println("<p>Contrasena: " + contrasenaStr + "</p>");
```

Tras guardar los cambios, compilar de nuevo y reiniciar el servidor, al recargar el formulario, introducir los valores y enviarlo, la respuesta del servlet muestra correctamente los valores introducidos (fuente: TD_07_06.md).

## Paginas relacionadas

- [[td7-servlets]]
- [[td6-formularios-html]]
- [[td7-web-xml]]
- [[td7-practica-servlets]]
- [[td8-documentacion-java-y-servlets]]
- [[sesiones-y-cookies]]
