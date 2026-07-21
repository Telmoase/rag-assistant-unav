# Wiki - Tecnologia Digital

Indice de todas las paginas de la wiki, agrupadas por tema.

---

## Tema 1: Java y Command Prompt

- [Compilacion y ejecucion de programas Java](td1-compilacion-java.md) - proceso de compilacion, bytecode, JVM y construccion incremental del primer programa.
- [Command Prompt en Windows](td1-command-prompt.md) - comandos de navegacion, variables de entorno y utilidades de la consola.
- [Programas basicos en Java](td1-programas-basicos-java.md) - nueve programas de ejemplo que cubren argumentos, tipos, condicionales, bucles y funciones.
- [Practica 1: Compilar y ejecutar en Java](td1-practica-compilar-java.md) - ejercicios oficiales de la primera practica: Hello World, argumentos, Scanner, menu con switch, ficheros.

## Tema 2: Variables y sentencias de control

- [Tipos de variables y declaraciones en Java](td2-tipos-y-variables.md) - los ocho tipos primitivos de Java, sus rangos y tamanos, y la sintaxis de declaracion de variables y arrays.
- [Estilo de codigo en Java](td2-estilo-de-codigo-java.md) - Java Code Conventions: indentacion, tipos de comentarios, declaraciones y formateo de sentencias de control.
- [Desarrollo incremental en Java](td2-desarrollo-incremental.md) - tecnica de construccion paso a paso con variables intermedias y scaffolding, ilustrada con el calculo de distancia euclidea.
- [Practica 2: Lenguaje Java](td2-practica-lenguaje-java.md) - ejercicios de la segunda practica: escape de caracteres, sentencias de control, factorial, bucle while con aleatorios y matrices.

## Tema 3: Clases y objetos

- [Creacion de objetos y arrays de objetos en Java](td3-objetos-y-referencias.md) - la palabra reservada new, referencias compartidas, arrays de objetos en dos pasos y la sintaxis unificada de declaracion.
- [Definicion de clases en Java](td3-definicion-de-clases.md) - estructura de una clase, constructor, la palabra this, y los ejemplos completos de las clases Circulo y Complex.
- [Depuracion de programas en Java](td3-depuracion-de-programas.md) - la depuracion como ciencia experimental, lista de verificacion practica, busqueda binaria del error.
- [Practica 3: Clases y objetos](td3-practica-clases-objetos.md) - ejercicios de la tercera practica: uso de la clase Circulo y creacion de la clase Matrix.

## Tema 4: Librerias, herencia y API de Java

- [Variables y metodos static en Java](td4-static.md) - significado de static en variables y metodos, reglas de acceso entre miembros static y de instancia, convencion de nombres para constantes.
- [Herencia en Java](td4-herencia.md) - extends, herencia de variables y metodos, y el ejemplo completo de la clase Esfera que extiende Circulo usando super.
- [Packages en Java](td4-packages.md) - para que sirven los packages, declaracion con package, import de clases externas, y la organizacion de la API de Java en packages.
- [La clase Vector en Java](td4-vector.md) - la limitacion de tamano fijo de los arrays, y como Vector crece automaticamente con addElement, size y elementAt.
- [Modificadores de acceso en Java](td4-modificadores-de-acceso.md) - los cuatro niveles de acceso (public, protected, sin modificador, private) y cuando usar cada uno.
- [Practica 4: Clases y algoritmos](td4-practica-clases-algoritmos.md) - ejercicios de la cuarta practica: variables de clase, algoritmo de ordenacion, y uso de la clase Complex.
- [Practica 5: Packages y herencia](td4-practica-packages-herencia.md) - ejercicios de la quinta practica: matrices con el package Jama y Vector, y la clase NMatrix que extiende Matrix.

## Tema 5: Internet y lenguaje HTML

- [Historia de la computacion y el camino a la era digital](td5-historia-de-la-computacion.md) - hitos historicos desde la maquina de Babbage hasta la creacion de la World Wide Web.
- [Arquitectura de la Web y estructura de un navegador](td5-arquitectura-de-la-web.md) - el ciclo de peticion y respuesta, los cuatro elementos de la Web, y la estructura interna del navegador (DOM, parsers, interprete de JavaScript).
- [HTML basico: etiquetas y estructura de una pagina web](td5-html-basico.md) - etiquetas de texto, listas, tablas, anclas, links e imagenes, con el ejemplo de la primera pagina web del CERN.
- [Practica 6: HTML basico](td5-practica-html-basico.md) - ejercicios de formateo de texto, listas, imagenes, tablas, y generacion de una pagina HTML desde Java.

## Tema 6: Formularios en HTML

- [Formularios HTML](td6-formularios-html.md) - la etiqueta form, sus atributos action y method, y los distintos tipos de campo (texto, contrasena, radio, checkbox, listas de seleccion y otros tipos especiales de input).
- [Metodos GET y POST en formularios HTML](td6-metodos-get-post.md) - diferencia conceptual y practica entre ambos metodos, y cuando conviene usar cada uno.
- [Generar HTML desde Java](generar-html-desde-java.md) - como imprimir etiquetas HTML con println y redirigir la salida a un fichero .html, con el ejemplo HelloWorld.java.
- [Practica 6: Formularios HTML](td6-practica-formularios-html.md) - ejercicios de formularios con cajas de texto, checkboxes, radio buttons, ventana de seleccion y area de texto.

## Tema 7: Introduccion a los servlets

- [Servlets en Java](td7-servlets.md) - que es un servlet, como se despliega en Apache Tomcat, y la estructura del codigo (HttpServlet, doGet, throws, PrintWriter).
- [Apache Tomcat](td7-apache-tomcat.md) - instalacion, configuracion, arranque y parada del servidor usado para ejecutar servlets.
- [El fichero de configuracion web.xml](td7-web-xml.md) - estructura en XML del fichero que relaciona una URL con la clase del servlet que debe responder.
- [Lectura de parametros en un servlet](td7-parametros-en-servlets.md) - como recoger los parametros enviados desde un formulario con getParameter.
- [Practica: ejercicios 5, 6 y 7 sobre servlets](td7-practica-servlets.md) - formulario con campo de texto, servlet con funcion auxiliar salidaHTML, y generalizacion con campos generados dinamicamente.

## Tema 8: Servlets y clases

- [Aplicaciones de ejemplo con servlets](td8-aplicaciones-de-ejemplo.md) - matrices, reserva de libros y panel de temperaturas, y como descargar e instalar una aplicacion desde GitHub.
- [Sesiones y cookies](sesiones-y-cookies.md) - como el servidor identifica a un usuario entre varias visitas guardando informacion en la sesion y una cookie en el navegador.
- [Documentacion de Java y de Servlets](td8-documentacion-java-y-servlets.md) - como navegar la documentacion oficial de Java SE y de los servlets (Java EE), e interfaces frente a clases.
