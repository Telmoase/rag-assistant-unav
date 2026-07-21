Sesiones y cookies

Resumen: explica como un servidor identifica a un mismo usuario a lo largo de varias visitas guardando informacion en su sesion y usando una cookie en el navegador, con el ejemplo de una aplicacion de reserva de libros.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_03.md

Ultima actualizacion: 2026-06-25

## El problema: recordar al usuario entre peticiones

Cada peticion HTTP que llega a un [[td7-servlets|servlet]] es, en principio, independiente de las anteriores. Sin embargo, hay situaciones en las que conviene que el servidor recuerde informacion de un mismo usuario a lo largo de varias peticiones, por ejemplo para acumular las reservas que va haciendo dentro de una misma visita (fuente: TD_08_03.md).

## La sesion: guardar informacion mientras dura la visita

En una aplicacion de reserva de libros, al hacer una reserva, los codigos de los libros seleccionados se guardan en la sesion del usuario. Si se hace una reserva varias veces sin reiniciar la sesion, los codigos se acumulan, apareciendo codigos de reservas anteriores junto con los nuevos, porque todo se guarda en la misma sesion (fuente: TD_08_03.md).

## La cookie: identificar al usuario en visitas posteriores

Si el usuario se registra (introduciendo un nombre asociado a la sesion), el servidor crea una cookie que permite mantener esa sesion identificada en las siguientes visitas desde el mismo navegador. A partir de ese momento, las reservas mostradas corresponden especificamente a ese usuario, localizado mediante la cookie guardada en el ordenador (fuente: TD_08_03.md).

## Paginas relacionadas

- [[td8-aplicaciones-de-ejemplo]]
- [[td7-servlets]]
- [[td7-parametros-en-servlets]]
