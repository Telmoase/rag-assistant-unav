Metodos GET y POST en formularios HTML

Resumen: compara los metodos GET y POST usados para enviar los datos de un formulario al servidor, explicando donde queda colocada la informacion en cada caso y cuando conviene usar cada metodo.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 6 - Formularios en HTML/TD_06_04.md

Ultima actualizacion: 2026-06-24

## Los dos metodos mas habituales

El protocolo HTTP (ver [[td5-arquitectura-de-la-web]]) ofrece varios metodos para realizar peticiones; los dos que se usan habitualmente en [[td6-formularios-html|formularios HTML]] son GET y POST (fuente: TD_06_04.md).

## Diferencia conceptual

Segun la idea original con la que se disenaron estos metodos, GET se usa habitualmente para obtener un recurso del servidor (por ejemplo, pedir la informacion de un producto indicando su codigo), y POST se usa para enviar informacion al servidor para que la guarde (por ejemplo, dar de alta un nuevo producto o registrar un usuario). En la practica, sin embargo, esta distincion no es obligatoria a nivel tecnico: cualquiera de los dos metodos funciona para cualquiera de las dos acciones (fuente: TD_06_04.md).

## Diferencia practica: donde va la informacion

Con GET, la informacion de los campos del formulario aparece directamente en la URL, visible en la barra de direcciones del navegador. Con POST, esa informacion va dentro del cuerpo de la llamada HTTP y no es visible directamente en la barra de direcciones, aunque se puede consultar en la consola de desarrollador (fuente: TD_06_04.md).

## Por que se recomienda GET durante el desarrollo

GET tiene un limite practico en el tamano de la informacion que se puede enviar a traves de la URL, a diferencia de POST, que no tiene ese mismo limite. Aun asi, suele ser mas comodo usar GET durante el desarrollo y las pruebas de un formulario, porque permite ver directamente en la URL que datos se estan enviando. Por este motivo, se recomienda POST para informacion sensible o de tamano considerable en la version final de una aplicacion, reservando GET para las fases de desarrollo (fuente: TD_06_04.md).

## Implicaciones para la programacion del servidor

Que los datos lleguen por GET o por POST implica programar la recepcion de la peticion de la forma correspondiente. Sin embargo, una vez recibidos, los parametros (nombres y valores de los campos del formulario) son exactamente los mismos en ambos casos: cambiar el metodo de un formulario no cambia que datos se envian, solo como llegan al servidor y como hay que programar su recepcion (fuente: TD_06_04.md).

## Paginas relacionadas

- [[td6-formularios-html]]
- [[td5-arquitectura-de-la-web]]
- [[td6-practica-formularios-html]]
- [[td7-servlets]]
