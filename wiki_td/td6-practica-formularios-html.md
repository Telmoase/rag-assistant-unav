Practica 6: Formularios HTML

Resumen: ejercicios de la sexta practica dedicados a formularios HTML, con cajas de texto, casillas checkbox y radio, ventanas de seleccion y areas de texto.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 5 - Internet y lenguaje HTML/Practica 6. HTML basico.md

Ultima actualizacion: 2026-06-24

Estos dos ejercicios pertenecen al mismo fichero de practica que [[td5-practica-html-basico|Practica 6: HTML basico]] (Ejercicios 6.1 a 6.3), pero se agrupan aqui por tratar especificamente sobre formularios, el tema correspondiente a este apartado de la asignatura. La teoria correspondiente esta en [[td6-formularios-html]].

## Ejercicio 6.4: Formulario de cajas de texto

Crear una pagina Web, a partir del fichero informacion.html, con un formulario y sus cajas de texto. La pagina muestra el titulo "INFORMACION" y el subtitulo "Formulario de registro", seguidos de una serie de campos de texto etiquetados, y al final dos botones: Enviar y Borrar. El formato se realiza con una tabla de 2 columnas, con el texto de las celdas de la izquierda alineado a la derecha con el atributo `ALIGN="right"` (fuente: Practica 6. HTML basico.md).

Caracteristicas de los campos del formulario:

| Campo | Nombre de la caja de texto | Tamano |
|---|---|---|
| Nombre | nombre | 12 |
| Primer Apellido | apell1 | (por defecto) |
| Segundo Apellido | apell2 | (por defecto) |
| Domicilio | domicilio | 18 |
| Codigo Postal | CP | 5 |
| Telefono | tel | 9 |
| e-mail | mail | 25 |
| Confirmar e-mail | c_mail | 25 |

El formulario debe estar dirigido (atributo action) a `http://www1.tecnun.es/asignaturas/informat3/Material/query.asp` y utilizar el metodo GET (`method="GET"`, ver [[td6-metodos-get-post]]) (fuente: Practica 6. HTML basico.md).

## Ejercicio 6.5: Formulario con distintos controles

Completar el formulario de arte.html, titulado "CATALOGO DE ARTE", con el texto introductorio "Introduce los terminos de busqueda", organizado en cuatro columnas (Obra, Tipo, Disponibilidad, Estilo), seguido de un area de texto bajo el texto "Haganos saber sus sugerencias" con un contenido por defecto, y un boton final llamado "Buscar" (fuente: Practica 6. HTML basico.md).

Elementos del formulario:

- **Obra**: caja de texto de nombre titulo, y caja de texto de nombre autor.
- **Tipo**: casillas checkbox de nombre tipo y valores esc, arq y pint (Escultura, Arquitectura, Pintura).
- **Disponibilidad**: casillas radio de nombre disp y valores publ y priv (Museo / Acceso publico, Coleccion privada).
- **Estilo**: ventana de seleccion de nombre estilo y valores clas, abs, surr y otro (Clasico, Abstracto, Surrealista, Otros).
- **Area de texto**: 4 filas y 40 columnas, con un texto por defecto (por ejemplo, "Me gustaria indicar que...").

(fuente: Practica 6. HTML basico.md)

## Paginas relacionadas

- [[td6-formularios-html]]
- [[td6-metodos-get-post]]
- [[td5-practica-html-basico]]
- [[td5-html-basico]]
