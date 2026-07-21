Practica 6: HTML basico

Resumen: ejercicios de la sexta practica centrados en HTML puro: formatear texto y listas, anadir imagenes y tablas, y generar una pagina HTML desde Java a partir de la clase NMatrix.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/Practica 6. HTML basico.md

Ultima actualizacion: 2026-06-24

El objetivo de esta practica es familiarizarse con el lenguaje HTML (ver [[td5-html-basico]]), trabajando con un editor de ficheros ASCII como Notepad, EditPlus o Notepad++. Consiste en editar paginas Web y ver su contenido en un navegador (fuente: Practica 6. HTML basico.md).

## Ejercicio 6.1: Etiquetas para estructurar y formatear texto; listas

Formatear el texto de instituciones.html: un titulo "INSTITUCIONES VASCAS", seguido de una lista no numerada con instituciones vascas (algunas de ellas subrayadas porque actuan como enlaces), y debajo dos bloques de texto explicativo con palabras en negrita y cursiva, uno de los cuales incluye una lista numerada con dos elementos (fuente: Practica 6. HTML basico.md).

Formatos a aplicar:

- Color de fondo `#8CACD4` (atributo bgcolor del elemento BODY).
- Texto de titulo en fuente arial, color blanco, tamano 2 puntos mayor que el estandar (atributos `face="arial" color="white" size="+2"` del elemento FONT).
- Resto del documento: listas numeradas y no numeradas, negrita, subrayado, italica, fuente arial o por defecto.

(fuente: Practica 6. HTML basico.md)

## Ejercicio 6.2: Imagenes y tablas

Anadir la ultima columna de la tabla de turismo.html: una tabla con tres categorias en la primera columna (Gastronomia, Cultura, Ocio, cada una como enlace subrayado), una segunda columna con varias filas de texto por categoria, y una tercera columna con una imagen relacionada con cada categoria, ocupando varias filas mediante combinacion de celdas. Imagenes a utilizar: receta1.jpg, receta2.jpg, cultura.jpg, playa.jpg (fuente: Practica 6. HTML basico.md).

## Ejercicio 6.3: Generar una pagina Web desde Java

Esta practica aplica la tecnica general de [[generar-html-desde-java|generar HTML desde Java]]: imprimir etiquetas HTML con println y redirigir la salida a un fichero.

Modificar la clase [[td4-practica-packages-herencia|NMatrix]] (del Ejercicio 5.2) para crear una nueva funcion createFile() que genere un fichero cuyo nombre sea el nombre de la matriz terminado en ".html", con una tabla HTML con los elementos de la matriz. La generacion del fichero se puede repasar en el [[td1-practica-compilar-java|Ejercicio 1.4]] (fuente: Practica 6. HTML basico.md).

La impresion de la cabecera y el comienzo de la tabla se obtiene con:

```java
toFile.println("<HTML>\n<HEAD>\n<TITLE> Practica 6 </TITLE>\n");
toFile.println("</HEAD>");
toFile.println("<BODY><TABLE border=1>");
```

Las funciones para leer los elementos de un objeto Jama.Matrix son (fuente: Practica 6. HTML basico.md):

```java
int getRowDimension(); // obtiene el numero de filas
int getColumnDimension(); // obtiene el numero de columnas
double get(int i, int j); // obtiene el elemento i, j
```

Es necesario incluir `throws IOException` en las funciones que intervienen en la llamada (main(), Opcion1(), LeerMatriz() y createFile()), e importar `java.io.*`. La funcion se define como `public void createFile() throws IOException`. Se llama despues de crear un objeto NMatrix, por ejemplo desdoblando la ultima linea de LeerMatriz() en `NMatrix m = new NMatrix(nombre, val, filas, columnas);` seguido de `return m;`, para poder introducir en medio la llamada `m.createFile()` (fuente: Practica 6. HTML basico.md).

## Paginas relacionadas

- [[td5-html-basico]]
- [[td4-practica-packages-herencia]]
- [[td1-practica-compilar-java]]
- [[generar-html-desde-java]]
- [[td6-practica-formularios-html]]
