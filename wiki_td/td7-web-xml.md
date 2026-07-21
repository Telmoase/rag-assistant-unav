El fichero de configuracion web.xml

Resumen: explica para que sirve el fichero web.xml de una aplicacion de servlets en Apache Tomcat, su estructura en XML, y como relaciona una URL con la clase del servlet que debe responder a ella.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_05.md

Ultima actualizacion: 2026-06-24

## Para que sirve web.xml

Al crear un [[td7-servlets|servlet]], es necesario crear tambien un fichero de configuracion llamado web.xml dentro de la carpeta WEB-INF de la aplicacion. Cada aplicacion (cada carpeta dentro de webapps) tiene su propio web.xml, y este fichero indica, cuando un cliente solicita un recurso concreto, cual es el servlet que debe responder a esa peticion (fuente: TD_07_05.md).

## El fichero completo

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<web-app>
<servlet>
  <servlet-name>primer</servlet-name>
  <servlet-class>HelloWorld</servlet-class>
</servlet>
<servlet-mapping>
  <servlet-name>primer</servlet-name>
  <url-pattern>/start</url-pattern>
</servlet-mapping>
</web-app>
```

(fuente: TD_07_05.md)

## Que es XML

El fichero esta escrito en XML (Extensible Markup Language). El nombre tiene relacion directa con [[td5-html-basico|HTML]] (HyperText Markup Language): ambos son lenguajes de marcado basados en etiquetas, pero en HTML las etiquetas estan predefinidas (h1, table, etc.), mientras que en XML se pueden definir las etiquetas propias que se necesiten para representar cualquier tipo de informacion. Apache Tomcat utiliza XML como formato para sus ficheros de configuracion, con sus propias etiquetas especificas (fuente: TD_07_05.md).

La estructura de un fichero XML sigue las mismas reglas que HTML respecto al anidamiento: cada etiqueta de apertura debe tener su correspondiente etiqueta de cierre, y todo lo que se abre dentro de una etiqueta debe cerrarse antes de cerrar la etiqueta exterior (fuente: TD_07_05.md).

## El bloque servlet: identificar la clase

Por cada servlet creado en la aplicacion, hay que incluir un bloque servlet en el web.xml con dos elementos (fuente: TD_07_05.md):

- **servlet-name**: un nombre que se usa unicamente dentro del propio web.xml, para identificar a ese servlet.
- **servlet-class**: el nombre de la clase del servlet, que corresponde al fichero .class generado al compilar el .java.

## El bloque servlet-mapping: relacionar la URL con el servlet

El bloque servlet-mapping define que parte de la URL llamada por el navegador debe responder con un servlet concreto, con dos elementos (fuente: TD_07_05.md):

- **servlet-name**: debe coincidir exactamente con el servlet-name del bloque servlet correspondiente, para vincular ambos bloques.
- **url-pattern**: la parte de la direccion, despues del nombre de la aplicacion, que activa este servlet (en el ejemplo, /start).

## El proceso completo cuando llega una peticion

Cuando Tomcat recibe una peticion, identifica primero a que aplicacion va dirigida (por el nombre de la carpeta dentro de webapps). Despues consulta el web.xml de esa aplicacion para averiguar donde esta definida la parte de la URL solicitada, encuentra la url-pattern asociada a un servlet-name dentro de un servlet-mapping, localiza el bloque servlet con ese mismo nombre, y obtiene la clase a utilizar. Finalmente, invoca el metodo doGet de esa clase para generar la respuesta (fuente: TD_07_05.md).

## Paginas relacionadas

- [[td7-servlets]]
- [[td5-html-basico]]
- [[td7-apache-tomcat]]
