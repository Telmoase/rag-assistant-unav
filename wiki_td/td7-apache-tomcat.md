Apache Tomcat

Resumen: explica como instalar, configurar, iniciar y detener Apache Tomcat, el servidor usado para ejecutar servlets en el curso, incluyendo la creacion de una pagina web sencilla y la instalacion portable desde un pendrive.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_02.md, Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_05.md, Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_06.md

Ultima actualizacion: 2026-06-25

## Que es Apache Tomcat

Apache Tomcat es el servidor que se utiliza para ejecutar los [[td7-servlets|servlets]] del curso. Antes de crear y ejecutar servlets, es necesario instalarlo y aprender a iniciarlo y detenerlo correctamente (fuente: TD_07_02.md).

## Instalacion

1. **Crear una carpeta de trabajo** con permiso de escritura, por ejemplo dentro de la carpeta del usuario o en C:\temp (por ejemplo, C:\temp\Tomcat).
2. **Copiar cinco carpetas** desde la instalacion base de Apache Tomcat (por ejemplo, en C:\Programs\JavaStack\apache-tomcat-9.0.89) a la carpeta de trabajo: conf, logs, temp, webapps y work. Para ahorrar espacio, se pueden eliminar las carpetas docs y examples dentro de webapps, ya que no son necesarias para el funcionamiento basico.
3. **Crear y ejecutar el fichero sj.bat** dentro de la carpeta de Tomcat, desde el [[td1-command-prompt|Command Prompt]]:

```
C:\temp\Tomcat>sj
```

(fuente: TD_07_02.md)

## Variables de entorno de sj.bat

El fichero sj.bat define tres variables de entorno necesarias para que Tomcat funcione correctamente (fuente: TD_07_02.md):

- **CATALINA_BASE**: la carpeta donde estan los ficheros de Tomcat que se van a usar (la carpeta de trabajo).
- **CATALINA_HOME**: la ubicacion de la instalacion principal de Apache Tomcat.
- **JAVA_HOME**: la version de Java que se va a utilizar.

Por ejemplo:

```
set CATALINA_BASE=C:\temp\Tomcat
set CATALINA_HOME=C:\Programs\JavaStack\apache-tomcat-9.0.89
set JAVA_HOME=C:\Programs\JavaStack\jdk1.8.0_131
```

## El comando set y otras formas de definir las variables

El comando set del sistema operativo tiene dos funciones: mostrar el contenido de las variables de entorno (tecleando set solo se muestran todas; anadiendo unas letras, por ejemplo set java, se muestran solo las que empiezan por esas letras), y definir nuevas variables con la sintaxis set NOMBRE=valor. Algunas variables ya existen de forma predefinida en el sistema, como %CD%, que contiene la ruta completa en la que se encuentra la consola en ese momento; para consultar el valor de cualquier variable se escribe su nombre entre dos simbolos de tanto por ciento, por ejemplo %drive% (fuente: TD_08_05.md).

Una forma de definir las variables de Java y Tomcat es asumir que la instalacion esta en una carpeta fija (por ejemplo, en la raiz del disco) y construir las rutas necesarias uniendo esa carpeta base con los nombres concretos de las subcarpetas. A la variable PATH se le anaden los directorios necesarios para Java y para Tomcat, conservando el valor anterior que ya tuviera; a la variable CLASSPATH se le anade el valor anterior mas las carpetas necesarias para los servlets y para librerias adicionales usadas en el curso, como la libreria matematica Jama (fuente: TD_08_05.md).

La forma mas recomendable, sin embargo, sigue siendo el comando sj: a diferencia de la definicion manual, sj no asume ninguna ruta o disco especifico, sino que toma como referencia la carpeta desde la que se ejecuta. Detecta esa carpeta actual y, a partir de ella, define automaticamente CATALINA_BASE, CATALINA_HOME, PATH y CLASSPATH. Por eso basta con situarse (con cd) dentro de la carpeta donde esta instalado Java, ya sea en el disco duro o en un pendrive, y ejecutar sj desde ahi (fuente: TD_08_05.md).

## Iniciar y detener el servidor

Una vez ejecutado sj.bat, el servidor se inicia con el comando `startup`, que abre una nueva ventana de consola para el proceso de Tomcat en ejecucion. A partir de ese momento, se puede acceder desde el navegador a una direccion como `http://localhost:8082` para ver la pagina de bienvenida de Tomcat y explorar ejemplos incluidos por defecto. Para detener Tomcat, se ejecuta `shutdown`, que cierra la ventana correspondiente (fuente: TD_07_02.md).

## Crear una pagina web sencilla para comprobar la instalacion

1. Ir a la carpeta de Tomcat y ejecutar de nuevo sj.bat para definir las variables de entorno.
2. Crear una carpeta nueva (por ejemplo, firstWeb) dentro de la carpeta webapps de CATALINA_BASE.
3. Crear dentro de esa carpeta un fichero index.html, que es el nombre que Tomcat abre por defecto al acceder a la carpeta de una aplicacion; con otro nombre habria que indicarlo explicitamente en la direccion del navegador.
4. Iniciar Tomcat con startup.
5. Acceder desde el navegador a la direccion correspondiente, por ejemplo `http://localhost:8082/firstWeb`.

(fuente: TD_07_02.md)

Al guardar el fichero index.html desde algunos editores de texto, conviene revisar que el nombre final no termine como index.html.txt, ya que algunos editores anaden automaticamente la extension .txt; de lo contrario no se mostrara la pagina esperada (fuente: TD_07_02.md).

## Instalacion portable desde un pendrive

Todo el proceso se puede repetir copiando la carpeta de instalacion de JavaStack a un pendrive (por ejemplo, a E:\Programs\JavaStack) y usando esa ubicacion en lugar de la carpeta del usuario o de C:\temp, siguiendo exactamente el mismo proceso. Esto permite llevar la instalacion completa de un ordenador a otro sin necesidad de reinstalar nada (fuente: TD_07_02.md).

## Instalar una aplicacion ya creada (por ejemplo, desde GitHub)

Para instalar una [[td8-aplicaciones-de-ejemplo|aplicacion ya creada]], como las disponibles en el repositorio del curso en GitHub, se descarga el repositorio completo como fichero comprimido y se descomprime, obteniendo una carpeta con todo el material. Si solo se quiere usar una aplicacion concreta, se navega hasta su subcarpeta dentro de la carpeta de tipo webapps del repositorio descomprimido, y esa carpeta se copia directamente a la carpeta webapps de la instalacion local de Apache Tomcat (fuente: TD_08_06.md).

A continuacion, se ejecuta el comando sj desde la carpeta donde esta instalado Java para definir las variables de entorno, y se arranca Tomcat. Una vez que Tomcat termina de leer las aplicaciones instaladas, se accede desde el navegador con la direccion local, el nombre de la carpeta de la aplicacion copiada, y el fichero HTML que se quiera abrir dentro de ella; la aplicacion descargada queda funcionando exactamente igual que cualquier otra creada manualmente dentro de webapps (fuente: TD_08_06.md).

## Paginas relacionadas

- [[td7-servlets]]
- [[td7-web-xml]]
- [[td1-command-prompt]]
- [[td8-aplicaciones-de-ejemplo]]
