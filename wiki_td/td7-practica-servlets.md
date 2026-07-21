Practica: ejercicios 5, 6 y 7 sobre servlets

Resumen: resuelve de forma encadenada tres ejercicios sobre servlets: un formulario con un campo de texto, un servlet que construye una respuesta con una funcion auxiliar, y la generalizacion del formulario con campos generados dinamicamente.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 7 - Introduccion a los servlets/TD_07_07.md

Ultima actualizacion: 2026-06-24

Esta pagina recoge la resolucion en video de los Ejercicios 5, 6 y 7 sobre [[td7-servlets|servlets]], ya que todavia no se ha incorporado el clipping oficial del enunciado de esta practica a Raw/; si se anade mas adelante, se actualizara esta pagina citandolo tambien (fuente: TD_07_07.md).

## Planteamiento general

Los tres ejercicios se resuelven de forma encadenada: el ejercicio 5 pide crear un formulario HTML con un campo de texto; el ejercicio 6 pide crear el servlet que reciba ese formulario y construya una respuesta usando una funcion auxiliar; y el ejercicio 7 completa el formulario con varios campos generados dinamicamente, en funcion de un parametro de entrada, y con un campo adicional para el nombre del usuario (fuente: TD_07_07.md).

## Ejercicio 5: formulario con un campo de texto

Se crea un fichero formulario.html dentro de la carpeta de la aplicacion, partiendo de la estructura basica de una pagina [[td5-html-basico|HTML]]. Dentro de ella, un [[td6-formularios-html|formulario]] cuya accion apunta al servlet del ejercicio 6, usando el metodo [[td6-metodos-get-post|GET]]. El formulario incluye un campo de texto con nombre opciones y un valor inicial por defecto (por ejemplo, value="3"), y un boton de tipo submit. Antes de tener el servlet construido, se puede comprobar que el formulario funciona inspeccionando que la URL generada al enviarlo incluye el parametro opciones con el valor introducido (fuente: TD_07_07.md).

## Ejercicio 6: el servlet y la funcion salidaHTML

El [[td7-servlets|servlet]] se construye copiando uno anterior, cambiando el nombre del fichero y de la clase. El enunciado pide implementar una funcion salidaHTML, que recibe un argumento entero opciones y devuelve un String con el codigo HTML a mostrar:

```java
String salidaHTML(int opciones) {
    String resultado = "";
    ...
    return resultado;
}
```

Dentro de doGet se recoge el [[td7-parametros-en-servlets|parametro]] opciones enviado por el formulario (convirtiendolo a entero), se llama a salidaHTML pasandole ese valor, y el resultado se imprime con out.println. Es necesario anadir tambien el nuevo servlet al fichero [[td7-web-xml|web.xml]], repitiendo el bloque servlet y servlet-mapping con el nombre correspondiente; si alguna etiqueta queda mal cerrada o mal anidada, el propio servidor senala al arrancar en que linea y columna del web.xml esta el error (fuente: TD_07_07.md).

## Construir el contenido de salidaHTML paso a paso

El enunciado pide primero resolver un caso particular: un formulario con un campo de texto oculto con nombre "Jose" que, al enviarse, llame a un servlet llamado mostrarDatos (usando GET). Al combinar HTML con comillas dobles propias de los atributos (por ejemplo, action="..."), conviene usar comillas simples dentro del texto HTML donde no sea estrictamente necesario usar comillas dobles, para no cerrar accidentalmente la cadena de texto Java antes de tiempo. Tambien conviene generar siempre la estructura completa de una pagina HTML (con html y body) en el resultado de salidaHTML, ya que si el navegador no la reconoce como una pagina HTML valida, puede mostrar el codigo fuente en lugar de interpretarlo (fuente: TD_07_07.md).

## Anadir los botones de opcion y generalizar con un bucle

Se incluyen tres botones de opcion (radio), todos con el nombre calif, y valores 1, 2 y 3, mas el boton de envio correspondiente. La parte final del ejercicio generaliza la generacion de botones: en lugar de tres botones fijos, se genera tantos como indique el parametro opciones, con un bucle for desde 1 hasta ese valor, concatenando en cada iteracion el HTML de un boton de opcion. El campo de texto oculto con el nombre de usuario se incluye una sola vez, fuera del bucle, ya que no debe repetirse en cada iteracion (fuente: TD_07_07.md).

## Verificacion del resultado final

El resultado probado de extremo a extremo: un primer formulario (ejercicio 5) que permite indicar cuantas opciones se quieren mostrar; un servlet (ejercicio 6) que recoge ese numero y construye dinamicamente, mediante salidaHTML, un segundo formulario con esa cantidad de botones de opcion y un campo oculto con el nombre de usuario; y al enviar ese segundo formulario, un tercer servlet (mostrarDatos) que recibe tanto la calificacion elegida como el nombre de usuario (fuente: TD_07_07.md).

## Leccion practica sobre depuracion

A lo largo de este ejercicio aparecen errores tipicos al trabajar con servlets y web.xml: etiquetas mal cerradas o mal anidadas en el web.xml (que el servidor senala con su linea y columna exactas al arrancar), comillas mal cerradas dentro de cadenas de texto Java que generan HTML, y llaves de apertura o cierre de bloques de codigo puestas al reves o en el orden incorrecto. La recomendacion es avanzar paso a paso, probando cada cambio antes de seguir con el siguiente (fuente: TD_07_07.md).

## Paginas relacionadas

- [[td7-servlets]]
- [[td7-parametros-en-servlets]]
- [[td6-formularios-html]]
- [[td7-web-xml]]
