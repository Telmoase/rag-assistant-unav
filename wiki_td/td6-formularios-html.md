Formularios HTML

Resumen: explica la etiqueta form y los atributos action y method para enviar informacion al servidor, y describe los distintos tipos de campo disponibles dentro de un formulario: cajas de texto, contrasena, botones, areas de texto, radio, checkbox, listas de seleccion y otros tipos especiales de input.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 6 - Formularios en HTML/TD_06_01.md, Tecnologia Digital/Tema 6 - Formularios en HTML/TD_06_02.md

Ultima actualizacion: 2026-06-24

## De pedir recursos a enviar informacion

Hasta ahora las peticiones de un navegador a un servidor buscaban obtener un recurso ya almacenado en el servidor (ver [[td5-arquitectura-de-la-web]]). Existe otro tipo de peticion en la que el objetivo es el contrario: enviar informacion al servidor para que la guarde, como ocurre al rellenar un formulario con datos personales y pulsar el boton de enviar (fuente: TD_06_01.md).

## La etiqueta form

Para presentar los campos de un formulario en una pagina web se usa la etiqueta `form`, con dos atributos principales: `action`, que indica la URL a la que se envian los datos, y `method`, que indica el metodo HTTP utilizado para enviarlos (ver [[td6-metodos-get-post]]). Tambien se le puede asignar un atributo `name` para identificar el formulario. Todo lo que se coloque dentro de la apertura y cierre de `form` se muestra en el navegador como parte del formulario (fuente: TD_06_01.md, TD_06_02.md).

## Tipos de campo dentro de un formulario

Dentro del formulario, cada campo se define con la etiqueta `input` y un atributo `type` que determina su comportamiento. Si no se especifica `type`, el valor por defecto es `text` (fuente: TD_06_02.md):

- **Caja de texto** (`type="text"` o sin atributo type): campo simple identificado con un atributo `name`.
- **Contrasena** (`type="password"`): se comporta igual que una caja de texto, pero los caracteres escritos se muestran ocultos en pantalla.
- **Boton de envio** (`type="submit"`): al pulsarlo, recoge toda la informacion de los campos del formulario y la envia segun el `method` y `action` indicados.
- **Boton de borrado** (`type="reset"`): borra el contenido del formulario sin enviarlo.
- **Area de texto multilinea** (etiqueta `textarea`, no `input`): permite texto en varias lineas, indicando filas (`rows`) y columnas (`cols`), con un texto inicial opcional entre su apertura y cierre.
- **Botones de opcion** (`type="radio"`): varios campos con el mismo atributo `name` pero distinto `value`, de forma que solo se puede activar una opcion del grupo a la vez.
- **Casillas de verificacion** (`type="checkbox"`): a diferencia de los radio, se pueden activar varias casillas del grupo a la vez, porque no son excluyentes entre si.
- **Ventana de seleccion** (etiqueta `select` con varias `option` dentro): lista desplegable; con `size="1"` se muestra solo la opcion seleccionada. Cada `option` lleva un `value` (lo que se envia) y un texto visible.
- **Listas**: misma estructura que la ventana de seleccion, pero con un `size` mayor que 1 para mostrar varias opciones a la vez sin desplegar; con el atributo `MULTIPLE` se pueden seleccionar varias opciones a la vez.

Ademas de estos, el atributo `type` de `input` admite otros valores para tipos de dato mas especificos: `button` (boton generico que no envia el formulario), `color` (selector de color), `date` y `datetime-local` (fecha y fecha con hora), `email` (con cierta validacion de formato), `file` (seleccion de un fichero del ordenador), `hidden` (campo oculto que se envia igualmente) y `range` (control deslizante entre los valores `min` y `max`) (fuente: TD_06_02.md).

## Ejemplo de uso

Por ejemplo, al enviar un formulario con un campo `nombre` con valor "Peter" y un campo `contrasena` con valor "123" usando el metodo GET, la URL resultante incluye esos valores como parametros tras un signo de interrogacion; la interpretacion de esos parametros depende de la programacion del servidor (fuente: TD_06_02.md).

Para probar cualquiera de estos ejemplos basta con copiar el codigo del formulario dentro del `body` de una pagina HTML (ver [[td5-html-basico]]) y abrirlo en el navegador. Si aparecen caracteres incorrectos en lugar de tildes o simbolos especiales, suele deberse a que la codificacion del fichero no coincide con la esperada por el navegador (fuente: TD_06_02.md).

## Paginas relacionadas

- [[td6-practica-formularios-html]]
- [[td6-metodos-get-post]]
- [[td5-html-basico]]
- [[td5-arquitectura-de-la-web]]
- [[td7-servlets]]
- [[td7-parametros-en-servlets]]
