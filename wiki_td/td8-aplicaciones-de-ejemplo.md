Aplicaciones de ejemplo con servlets

Resumen: describe tres aplicaciones completas de ejemplo (gestion de matrices, reserva de libros y panel de temperaturas) que recogen los ejercicios del curso, y explica como descargar e instalar cualquier aplicacion del repositorio del curso en GitHub.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_03.md, Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_06.md

Ultima actualizacion: 2026-06-25

## Tres aplicaciones de ejemplo

Existen tres aplicaciones de ejemplo que recogen los ejercicios realizados en las practicas del curso: una aplicacion de gestion de matrices, una aplicacion de reserva de libros, y una aplicacion de simulacion de un panel de temperaturas. Tras descargarlas e instalarlas (ver [[td7-apache-tomcat|instalar una aplicacion ya creada]]), se recomienda arrancar Tomcat desde el directorio donde se encuentra la aplicacion de reserva de libros, ya que esta utiliza un fichero local con la lista de libros y necesita ejecutarse desde esa ubicacion para poder leerlo correctamente (fuente: TD_08_03.md).

## Aplicacion de matrices

Muestra un menu desde el que se pueden introducir distintas matrices y realizar operaciones con ellas (fuente: TD_08_03.md):

- **Introducir matriz**: pide las dimensiones (por ejemplo, 2 por 2) y rellenar sus valores. Una vez creada, se muestra en una tabla y se numera (la primera matriz creada recibe el valor 0).
- **Mostrar matrices**: permite ver las matrices ya creadas.
- **Calcular inversa**: se selecciona una matriz y se calcula su inversa.
- **Multiplicar**: se seleccionan dos matrices y se calcula el producto. Si se multiplica una matriz por su inversa, el resultado deberia ser la matriz identidad (con valores muy cercanos a cero fuera de la diagonal, debido a la precision limitada de los calculos en coma flotante).
- **Calcular determinante**: se selecciona una matriz y se calcula su determinante.

## Aplicacion de reserva de libros

Los libros se leen desde un fichero de texto (.txt) local. La aplicacion permite mostrar el listado completo de libros en una tabla, introducir un nuevo libro, o realizar una reserva seleccionando varios libros de la lista. Esta aplicacion es la que introduce el uso de [[sesiones-y-cookies|sesiones y cookies]] para acumular reservas e identificar al usuario entre visitas (fuente: TD_08_03.md).

## Aplicacion de panel de temperaturas

Simula un panel dividido en celdas (por ejemplo, de 30 por 30, o el numero que se indique), en el que se pueden fijar valores de temperatura (entre 0 y 255) en algunas celdas concretas, por ejemplo en las esquinas o en puntos especificos del panel. Al pulsar calcular, la aplicacion determina la temperatura del resto de las celdas aplicando las reglas de calculo del ejercicio correspondiente, y muestra el resultado completo en una tabla o cuadricula (fuente: TD_08_03.md).

## Descargar e instalar una aplicacion desde GitHub

El repositorio del curso (por ejemplo, el repositorio CS en GitHub) se descarga completo como un fichero comprimido de pocos megas; tras descomprimirlo se obtiene una carpeta con todo el material, que puede ser interesante conservar para no depender de Internet cada vez que se necesite consultar algo (fuente: TD_08_06.md).

Si solo se quiere usar una aplicacion concreta, se navega dentro de la carpeta descomprimida hasta la subcarpeta de tipo webapps, se localiza la carpeta de esa aplicacion, y se copia directamente a la carpeta webapps de la instalacion local de [[td7-apache-tomcat|Apache Tomcat]]. Con ese simple paso, la aplicacion ya queda preparada para ejecutarse: basta con ejecutar sj para definir las variables de entorno, arrancar Tomcat, y acceder desde el navegador a la direccion local correspondiente a la carpeta copiada (fuente: TD_08_06.md).

## Paginas relacionadas

- [[td7-apache-tomcat]]
- [[td7-servlets]]
- [[sesiones-y-cookies]]
