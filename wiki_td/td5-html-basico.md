HTML basico: etiquetas y estructura de una pagina web

Resumen: introduce las etiquetas HTML basicas a partir de la primera pagina web del CERN, muestra como el navegador construye la estructura minima de una pagina aunque el fichero no tenga etiquetas explicitas, y recopila las etiquetas principales de formato de texto, listas, tablas, anclas, links e imagenes.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/TD_05_04.md, Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/TD_05_05.md, Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/TD_05_06.md, Tecnologia Digital/Tema 6 - Formularios en HTML/TD_06_03.md

Ultima actualizacion: 2026-06-24

## Que es HTML

HTML (HyperText Markup Language) es el lenguaje utilizado en Internet para definir las paginas de la World Wide Web (ver [[td5-arquitectura-de-la-web]]). Los ficheros HTML son ficheros puramente de texto (ASCII), que se pueden escribir con cualquier editor basico, como Notepad; tambien se pueden usar procesadores de texto mas avanzados, como Microsoft Word, pero hay que asegurarse de guardar el fichero como texto sin formato. En el fichero se introducen unas marcas llamadas TAGs (etiquetas), que el navegador interpreta para dar formato al texto (fuente: TD_05_06.md).

## Estructura comun de las etiquetas

Las etiquetas HTML siguen una estructura comun: un nombre encerrado entre los simbolos menor que y mayor que, y se cierran repitiendo el mismo nombre, esta vez precedido de una barra, dentro de los mismos simbolos (fuente: TD_05_04.md):

```
<nombre>contenido afectado</nombre>
```

## Una pagina web es, en su forma mas simple, un fichero de texto

Para crear una pagina web no hace falta ningun software especial: basta con un fichero de texto plano guardado con extension .html. Aunque el fichero no contenga ninguna etiqueta HTML explicita, el navegador sigue siendo capaz de mostrarlo, presentando el texto sin ningun formato especial (fuente: TD_05_05.md).

Si se inspecciona la estructura de esa pagina desde el propio navegador, se observa algo importante: aunque el fichero fuente no incluyera ninguna etiqueta, el navegador construye automaticamente la estructura completa que toda pagina web necesita: una etiqueta html de apertura y cierre, dentro de ella una cabecera (head) y un cuerpo (body). El navegador anade esta estructura minima incluso cuando el autor no la ha escrito explicitamente (fuente: TD_05_05.md).

La estructura general de un fichero HTML, escrita explicitamente, es (fuente: TD_05_06.md):

```html
<!DOCTYPE HTML>
<HTML>
    <HEAD>
        <TITLE>Titulo de la pagina</TITLE>
    </HEAD>
    <BODY>
    </BODY>
</HTML>
```

## El ciclo de edicion y comprobacion

Para dar formato al contenido se anaden etiquetas directamente en el fichero de texto. Por ejemplo, para que un texto se muestre como un titulo de cabecera de nivel uno, se envuelve entre las etiquetas h1 (fuente: TD_05_05.md):

```html
<h1>Este es un mensaje de cabecera nivel uno</h1>
```

Al guardar el fichero con este cambio y recargar la pagina en el navegador, se puede ver inmediatamente el resultado. Este ciclo (modificar el fichero, guardarlo, comprobar el resultado en el navegador) es el flujo de trabajo basico para desarrollar paginas web sencillas (fuente: TD_05_05.md).

## El titulo de la pagina frente al titulo visible

La etiqueta title define el texto que aparece en la cabecera de la pestana del navegador, no el titulo visible dentro del cuerpo de la pagina. El titulo que aparece dentro del propio contenido de la pagina esta delimitado por la etiqueta h1: la h es la inicial de header (cabecera), y el numero 1 indica que es una cabecera de nivel uno, el mas destacado. Para titulos de distinto nivel existen seis etiquetas de cabecera, de H1 (la mas destacada) a H6 (la menos destacada) (fuente: TD_05_04.md, TD_05_06.md).

## Formato de parrafos

El texto se agrupa en parrafos con la etiqueta P. Los parrafos se separan entre si con un espaciado mayor al de una simple nueva linea; para un espaciado mas compacto dentro de un mismo parrafo se usa BR (line break). Para lineas horizontales separadoras se usa HR, que admite atributos como WIDTH (ancho), SIZE (grosor) o NOSHADE (sin sombreado). Los parrafos se pueden indentar con BLOCKQUOTE, que aplica una sangria al texto hasta que se cierra la etiqueta. La etiqueta PRE (preformatted) respeta exactamente la forma original en que se ha escrito el texto, incluyendo espacios y saltos de linea; aunque puede parecer util, es preferible evitarla en general, porque impide que la pagina se adapte a distintos formatos de pantalla (fuente: TD_05_06.md).

## Formato de texto: funcion frente a apariencia

Una idea importante de HTML es definir la funcion que se desea dar al texto (resaltar una palabra, mantener un espaciado constante) sin decir exactamente como debe representarse visualmente, dejando esa decision al navegador. Por ejemplo, STRONG y EM indican enfasis fuerte y enfasis, que la mayoria de navegadores representan como negrita y cursiva respectivamente, pero el navegador podria elegir otra forma de representarlo si no soporta esos estilos. Tambien existen etiquetas que fijan directamente el formato visual, sin dejar margen al navegador: B (bold), I (italic), TT (teletype, letra de paso constante) (fuente: TD_05_06.md).

Los parrafos se pueden alinear con el atributo ALIGN, con los valores LEFT, RIGHT o CENTER. Otros efectos de texto disponibles son U (subrayado), STRIKE (tachado), BIG (letra mas grande), SMALL (letra mas pequena), SUB (subindice) y SUP (superindice) (fuente: TD_05_06.md).

## Listas

Una lista no ordenada se define con UL (unordered list); cada elemento se marca con LI (list item) y van precedidos por marcadores (bullets), usandose cuando no importa el orden de los elementos. En la primera pagina web del CERN, por ejemplo, cada elemento de una lista UL contenia a su vez un texto con un hipervinculo (fuente: TD_05_04.md, TD_05_06.md).

Una lista ordenada se define con OL (ordered list), tambien con elementos LI; la diferencia es que los elementos van precedidos por numeros, asignados automaticamente segun su posicion en la lista (fuente: TD_05_06.md).

## Tablas

Las tablas permiten organizar contenido en filas y columnas, y se construyen con tres niveles de etiquetas anidadas: TABLE (la tabla completa), TR (table row, una fila), y dentro de cada fila, TD (table data, una celda). Una tabla puede llevar el atributo BORDER para mostrar bordes visibles, y se puede centrar en la pagina envolviendola con la etiqueta CENTER. Las tablas pueden anidarse: una tabla puede contener dentro de una de sus celdas otra tabla completa, o cualquier otro elemento HTML (fuente: TD_05_06.md).

## Hipervinculos: la etiqueta a

Cada palabra o frase que aparece como un enlace esta delimitada por la etiqueta a (de anchor). Dentro de esa etiqueta hay un atributo que indica la direccion a la que se va al hacer clic (fuente: TD_05_04.md).

Las anclas son referencias invisibles dentro del documento que sirven como punto de destino para un enlace, definidas con la etiqueta A y el atributo NAME, por ejemplo `<A NAME="ancla">`; el ancla en si no se muestra como contenido visible, su unica funcion es marcar una posicion concreta del documento (fuente: TD_05_06.md).

Los links son palabras o elementos diferenciados que envian al usuario a otro ordenador remoto, o a otra zona de la misma pagina marcada con un ancla; el conjunto de links es lo que constituye el hipertexto. Se definen con la etiqueta A y el atributo HREF, que indica la direccion de destino (fuente: TD_05_06.md):

```html
<A HREF="http://www.tecnun.es/">Al Web</A>
<A HREF="#ancla">Al ancla</A>
```

## Insercion de imagenes e imagenes clicables

Para insertar una imagen se utiliza la etiqueta IMG, con el atributo SRC indicando el fichero donde se encuentra la imagen (fuente: TD_05_06.md):

```html
<img src="logo.png">
```

Se pueden combinar links e imagenes para crear una imagen que funcione tambien como enlace, envolviendo la etiqueta IMG dentro de una etiqueta A con su atributo HREF (fuente: TD_05_06.md):

```html
<A HREF="#ancla">
<img src="logo.png">
</A>
```

## Caracteres especiales: entidades HTML

Es habitual que los caracteres acentuados aparezcan en el navegador de forma incorrecta, mostrando simbolos extranos en lugar de la letra esperada, cuando la codificacion en la que esta guardado el fichero no coincide con la que el navegador espera al interpretarlo. Para evitar este problema, HTML permite escribir un caracter especial mediante una entidad: una secuencia que empieza con el simbolo `&` y termina con punto y coma, que se muestra siempre correctamente sin depender de la codificacion real del fichero (fuente: TD_06_03.md).

Las entidades tambien son necesarias para mostrar literalmente los simbolos `<` y `>`, los mismos que delimitan las etiquetas HTML: si se escriben directamente, el navegador los interpreta como el inicio o el final de una etiqueta en lugar de mostrarlos como texto. Usando la entidad correspondiente para cada simbolo se pueden incluir ejemplos de codigo HTML dentro de una pagina sin que el navegador los interprete como etiquetas reales (fuente: TD_06_03.md).

## Ejemplo real: la primera pagina web del CERN

Comparando el codigo fuente de una de las primeras paginas web publicadas por Tim Berners-Lee desde el CERN (todavia accesible hoy) con su visualizacion actual, se pueden identificar estas etiquetas basicas en un contexto real: title para el texto de la pestana, h1 para el titulo visible, a para los hipervinculos, y ul/li para las listas. El navegador permite inspeccionar la estructura interna de la pagina, mostrando las etiquetas de apertura y cierre incluso si el autor original no las escribio explicitamente de forma completa, y visualizando la estructura jerarquica completa en forma de arbol de elementos anidados (fuente: TD_05_04.md).

## Paginas relacionadas

- [[td5-arquitectura-de-la-web]]
- [[td5-historia-de-la-computacion]]
- [[td5-practica-html-basico]]
- [[td6-formularios-html]]
- [[td6-practica-formularios-html]]
- [[td7-web-xml]]
