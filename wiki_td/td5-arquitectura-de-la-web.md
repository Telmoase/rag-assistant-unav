Arquitectura de la Web y estructura de un navegador

Resumen: explica el ciclo de peticion y respuesta entre navegador y servidor, los cuatro elementos que forman la Web, y la estructura interna de un navegador (interfaz de usuario, DOM, parsers, interprete de JavaScript y capa de comunicacion).

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/TD_05_02.md, Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/TD_05_03.md

Ultima actualizacion: 2026-06-24

## Como se accede a un servidor a traves de Internet

Internet conecta multitud de ordenadores, algunos de los cuales actuan como servidores: ordenadores dedicados a almacenar y entregar datos cuando se les solicita. Desde el ordenador propio, conectado a Internet siguiendo sus protocolos, se puede acceder a estos servidores (fuente: TD_05_02.md).

## El ciclo de peticion y respuesta

El acceso se realiza habitualmente mediante un navegador. Al escribir una URL en la barra de direcciones, se genera una peticion que llega al servidor correspondiente. El servidor recibe la peticion, identifica que contenido se esta solicitando, y devuelve una respuesta al ordenador que hizo la peticion. Esa respuesta puede contener texto, imagenes, audio, o cualquier otro tipo de contenido, y se muestra en la pantalla del navegador. Si dentro de esa pagina se hace clic en un enlace, se genera una nueva peticion, posiblemente a otro servidor distinto, que produce una nueva respuesta y muestra la siguiente pagina (fuente: TD_05_02.md).

## Los cuatro elementos que forman la Web

De este proceso se identifican los cuatro elementos que intervienen, coincidiendo con los cuatro componentes inventados por Tim Berners-Lee (ver [[td5-historia-de-la-computacion]]) (fuente: TD_05_02.md):

- Un **navegador** (cliente), que realiza las peticiones y muestra el resultado.
- Un **servidor**, que recibe las peticiones y devuelve las respuestas correspondientes.
- Un **protocolo de comunicaciones**, HTTP, que define como se estructuran las peticiones y las respuestas (ver [[td6-metodos-get-post|metodos GET y POST]]).
- Un **lenguaje** en el que va escrito el contenido del mensaje que produce el servidor: habitualmente [[td5-html-basico|HTML]].

Estos cuatro componentes fueron disenados por Berners-Lee mientras trabajaba en el CERN, donde una de sus tareas era ayudar a conectar e intercambiar informacion entre ordenadores de cientos de cientificos e ingenieros, repartidos por distintas partes del mundo y cada uno con fabricante y sistema operativo distintos. La Web resolvio ese problema de interoperabilidad proporcionando un conjunto de estandares comunes, independientes del fabricante o sistema operativo de cada ordenador concreto (fuente: TD_05_02.md).

## El navegador como elemento de la Web

El navegador es el elemento desde el cual el usuario realiza peticiones al servidor y desde el cual se interpreta la respuesta que el servidor envia, continuando habitualmente la navegacion hacia otras paginas dentro del propio navegador (fuente: TD_05_03.md).

## La interfaz de usuario

La capa mas visible del navegador es la interfaz de usuario, compuesta por los elementos con los que el usuario interactua directamente: el teclado, el raton, y la pantalla donde se muestra la pagina web recibida (fuente: TD_05_03.md).

## El modelo del objeto del documento (DOM)

La interfaz de usuario se relaciona con la instancia principal del navegador: el modelo del objeto del documento, conocido como DOM (Document Object Model). El DOM es la representacion interna del documento que se esta mostrando, con una estructura jerarquica, y es el resultado de procesar la respuesta recibida del servidor. A traves del DOM se puede acceder a cualquiera de los elementos de la pagina, o a las modificaciones que se vayan a realizar sobre ella (fuente: TD_05_03.md).

## Los parsers

Para construir el DOM a partir de la respuesta recibida, el navegador realiza peticiones internas a distintos parsers, cada uno especializado en interpretar un tipo concreto de contenido: por ejemplo, hay un parser para el HTML y otro distinto para el CSS (la pagina de estilo que define el aspecto visual). Los parsers transforman los documentos recibidos en los elementos del DOM que el usuario puede ver finalmente en pantalla (fuente: TD_05_03.md).

## El interprete de JavaScript

Se puede considerar como otro elemento separado el interprete de JavaScript, capaz de ejecutar los programas escritos en ese lenguaje que llegan desde el servidor junto con la pagina. Tanto los parsers como el interprete de JavaScript se comunican con la capa de comunicacion (fuente: TD_05_03.md).

## La capa de comunicacion y el flujo completo

La capa de comunicacion permite que el navegador, a traves de la conexion a Internet del ordenador, se comunique con otros ordenadores: realiza la peticion HTTP correspondiente a la accion del usuario, y recibe la respuesta del servidor. Resumiendo el flujo completo: la capa de comunicacion envia la peticion HTTP y recibe la respuesta; esa respuesta es interpretada por los parsers, que construyen el DOM; y ese modelo se representa finalmente en pantalla a traves de la interfaz de usuario (fuente: TD_05_03.md).

El propio navegador ofrece herramientas para observar este proceso en detalle: ver como una pagina HTML es procesada por los parsers, visualizar el modelo resultante, inspeccionar la estructura de una llamada HTTP, o depurar el codigo JavaScript en ejecucion (fuente: TD_05_03.md).

## Paginas relacionadas

- [[td5-historia-de-la-computacion]]
- [[td5-html-basico]]
- [[td5-practica-html-basico]]
- [[td6-metodos-get-post]]
