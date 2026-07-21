Servlets en Java

Resumen: explica que es un servlet, como se despliega una aplicacion de servlets dentro de Apache Tomcat, y la estructura del codigo de un servlet (HttpServlet, doGet, throws, PrintWriter), con el ejemplo HelloWorld.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_01.md, Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_03.md, Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_04.md, Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_01.md, Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_02.md

Ultima actualizacion: 2026-06-25

## Donde se procesa la informacion de un formulario

Cuando se envia un [[td6-formularios-html|formulario]], la informacion llega al servidor, que puede guardarla y construir una pagina de respuesta para devolver al navegador. Todo este procesamiento ocurre en el servidor, mediante aplicaciones especificas que se ejecutan ahi; en este curso, esas aplicaciones se construyen con Java (fuente: TD_07_01.md).

## Que es un servlet

Java dispone de un elemento especifico para construir aplicaciones que se ejecutan en el servidor: el servlet. El nombre viene de "servlet" como contraccion de una aplicacion (applet) que se ejecuta en el servidor (server), en contraposicion a un applet tradicional, que se ejecutaba en el navegador del cliente (fuente: TD_07_01.md).

Un servlet actua como puente entre la peticion que llega del navegador y la respuesta que el servidor debe generar: recibe la peticion (por ejemplo, mediante el metodo doGet si la peticion fue [[td6-metodos-get-post|GET]]), procesa la informacion necesaria, y construye el texto HTML que se enviara de vuelta como respuesta (fuente: TD_07_01.md).

## Donde se despliega un servlet

Un servlet no se ejecuta directamente desde la consola, aunque si se compila desde ahi: se ejecuta a traves de la web, gracias a un servidor de aplicaciones capaz de servirlo, en este caso [[td7-apache-tomcat|Apache Tomcat]]. Para ello, hay que crear la aplicacion dentro de la carpeta webapps de la instalacion de Tomcat (fuente: TD_07_03.md).

Dentro de webapps, se crea una carpeta con el nombre de la aplicacion (por ejemplo, Servlet1); dentro de ella, una carpeta WEB-INF (en mayusculas, porque el sistema distingue mayusculas y minusculas), y dentro de WEB-INF, una carpeta classes (en minusculas). Este patron de carpetas se repite siempre igual para cualquier aplicacion de servlets (fuente: TD_07_03.md):

```
webapps/
  Servlet1/
    WEB-INF/
      classes/
```

El fichero del servlet se guarda dentro de classes, con un nombre que debe coincidir exactamente con el nombre de la clase. Se compila desde esa carpeta con el comando habitual `javac NombreDelServlet.java` (fuente: TD_07_03.md).

## Por que no se puede ejecutar un servlet directamente

Si se intenta ejecutar un servlet con el comando `java`, se obtiene un error porque no se encuentra el metodo main: un servlet no tiene main, sino un metodo doGet (u otros equivalentes), que solo es invocado por el servidor de aplicaciones cuando recibe una peticion correspondiente, sin ejecutarse nunca de forma independiente desde la consola. Para poder ejecutarlo a traves del navegador, es necesario crear tambien el fichero de configuracion [[td7-web-xml|web.xml]] dentro de WEB-INF (fuente: TD_07_03.md).

Si se modifica el codigo de un servlet, hay que guardarlo, compilarlo de nuevo, detener Tomcat, volver a arrancarlo y recargar la pagina en el navegador: es necesario reiniciar el servidor porque carga las clases compiladas al iniciarse y no detecta automaticamente los cambios mientras esta en ejecucion (fuente: TD_07_03.md).

## Estructura del codigo: el ejemplo HelloWorld

```java
import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class HelloWorld extends HttpServlet{
    public void doGet(HttpServletRequest request, HttpServletResponse response)
      throws ServletException, IOException {
        PrintWriter out = response.getWriter();
        out.println("Hello World");
    }
}
```

Comparado con una clase Java normal ejecutada desde consola, hay varias diferencias clave (fuente: TD_07_04.md):

- **La clase debe extender HttpServlet**, de la libreria de servlets (de ahi los `import` de `javax.servlet.*` y `javax.servlet.http.*`). Al extenderla, la clase aprovecha la funcionalidad ya implementada en HttpServlet.
- **No hay metodo main.** En su lugar se usa doGet (o doPost, segun el metodo HTTP de la peticion); por sencillez de desarrollo se suele usar doGet.
- **doGet tiene dos argumentos**, porque responde al esquema de peticion y respuesta de HTTP: `HttpServletRequest request` (la peticion recibida) y `HttpServletResponse response` (el objeto usado para construir y enviar la respuesta).
- **La clausula `throws ServletException, IOException`** es necesaria porque doGet puede lanzar excepciones que no se gestionan dentro de el; al relanzarlas con throws, es quien invoca al metodo (Apache Tomcat) quien se encarga de gestionarlas.

Dentro del cuerpo de doGet, se obtiene primero el objeto sobre el que escribir la respuesta con `PrintWriter out = response.getWriter();`. Este objeto se comporta como la salida estandar usada en programas de consola, pero en vez de escribir en la consola escribe en el contenido de la respuesta enviada al navegador. Sobre el se usa `println`, igual que para escribir en consola, una llamada por cada linea de HTML que se quiera generar (fuente: TD_07_04.md).

## Ciclo de vida de un servlet: init y destroy

Un servlet puede incluir el metodo init, que se ejecuta para realizar operaciones que solo deben ocurrir una vez durante toda la vida del servlet, no en cada peticion individual: se ejecuta la primera vez que se accede al servlet despues de arrancar [[td7-apache-tomcat|Tomcat]], y no se vuelve a ejecutar en las peticiones siguientes mientras el servidor siga en marcha. De forma simetrica, existe el metodo destroy, pensado para realizar alguna operacion en el momento en que Tomcat se va a cerrar y el servlet deja de estar disponible (fuente: TD_08_02.md).

## Manejo de excepciones con try-catch

Como alternativa a relanzar una excepcion con throws, se puede capturar directamente dentro del propio metodo con la estructura try-catch:

```java
try {
    PrintWriter out = response.getWriter();
    ...
} catch (IOException e) {
    System.out.println("Error: " + e);
}
```

El bloque try contiene la operacion que puede dar lugar a un error (en este caso, obtener el escritor de la respuesta). El bloque catch, inmediatamente despues del try, especifica el tipo de excepcion que se va a capturar (en este caso, IOException) y que hacer si se produce ese error. Dejar el bloque catch vacio silenciaria cualquier error sin dejar rastro de lo sucedido, lo que hace mucho mas dificil localizar despues que ha fallado y por que; por eso es preferible, como minimo, mostrar un mensaje que indique que se ha producido un error (fuente: TD_08_02.md).

## Los metodos flush y close

Al final de la generacion de la respuesta, se utilizan los metodos flush() y close() sobre el objeto PrintWriter, para forzar que los datos pendientes se envien efectivamente al cliente y cerrar el escritor. Aunque en la practica suele funcionar de forma similar sin llamarlos explicitamente, es mas correcto incluirlos al final de cada pagina, para asegurar que los datos llegan correctamente al navegador (fuente: TD_08_02.md).

## Pagina de inicio: index.html

Cuando una aplicacion tiene varios recursos (por ejemplo, un servlet y un [[td6-formularios-html|formulario]]), conviene crear un fichero index.html en la carpeta raiz de la aplicacion. Tomcat muestra automaticamente ese fichero cuando se accede a la aplicacion sin especificar ningun fichero concreto, por lo que sirve como punto de entrada centralizado a todos los recursos de la aplicacion (fuente: TD_08_01.md).

Dentro de index.html conviene usar enlaces relativos (por ejemplo, simplemente start o formulario.html) en lugar de la ruta completa con el nombre del servidor y el puerto: si estos cambiaran mas adelante, un enlace relativo sigue funcionando sin tener que modificarlo, porque el navegador completa automaticamente la parte que falta usando como referencia la aplicacion en la que se encuentra (fuente: TD_08_01.md).

Si solo se modifica o crea el fichero index.html (un fichero HTML, no un .java), no es necesario volver a compilar nada ni reiniciar Tomcat: basta con guardar el cambio y recargar la pagina en el navegador (fuente: TD_08_01.md).

## Paginas relacionadas

- [[td7-apache-tomcat]]
- [[td7-web-xml]]
- [[td7-parametros-en-servlets]]
- [[td7-practica-servlets]]
- [[td6-formularios-html]]
- [[td6-metodos-get-post]]
- [[generar-html-desde-java]]
- [[td8-aplicaciones-de-ejemplo]]
- [[td8-documentacion-java-y-servlets]]
