# Tema 4: Formularios

**Resumen**: Resumen del Tema 4 de Tecnología de la Información. Cubre la creación y configuración de formularios en Access, el control combo para claves foráneas y los subformularios para relaciones 1:N.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_01.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_02.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_03.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_04.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_05.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/Práctica 4. Formularios.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 4 enseña a construir interfaces de usuario sobre una base de datos Access. Los formularios reemplazan la vista de datos directa por pantallas más cómodas e intuitivas, y permiten controlar exactamente qué puede ver y modificar el usuario.

## Bloque 1: Formularios

Un [[formularios-access|formulario]] muestra un registro por pantalla y permite navegar, añadir y editar datos. Los tres modos de trabajo son **diseño** (modificar estructura), **layout** (ajustar viendo datos reales) y **vista** (uso final).

Los controles fundamentales son:

- **Etiqueta**: texto estático.
- **Cuadro de texto**: vinculado a un campo de la tabla mediante el *Origen del control*.
- **Combo** (menú desplegable): el control más importante del tema. Sustituye la escritura de un código numérico por una selección de una lista legible. Se usa para campos que son [[modelo-relacional|claves foráneas]] hacia otra tabla. Se configura con el asistente indicando tabla de origen, campos visibles y campo donde se almacena el valor.

Se puede designar un formulario de inicio que se abra automáticamente al arrancar la base de datos desde **Opciones → Base de datos actual**.

## Bloque 2: Subformularios

Un [[subformularios-access|subformulario]] es un formulario incrustado en otro. Se usa cuando hay una relación 1:N: el formulario principal muestra los datos del lado 1 y el subformulario lista todos los registros del lado N. Cada nivel tiene su propia barra de navegación.

La vinculación se establece mediante el **campo de unión maestro** (lado 1) y el **campo de unión secundario** (lado N). Access puede generarlo automáticamente al crear un formulario sobre la tabla del lado 1.

El subformulario puede presentarse como **hoja de datos** (generado automáticamente, visual de tabla) o como **formulario tabular** (creado con el asistente, distribución en filas con cabeceras de columna, más personalizable).

## Práctica

Los ejercicios de [[practica-4-formularios|Práctica 4]] construyen formularios para todas las tablas de la base de datos de albaranes (Compañías, Camiones, Gasolineras, Albaranes) y un formulario con subformulario tabular mejorado que muestra el nombre de la gasolinera en lugar del código y permite seleccionarla con un combo.

## Páginas relacionadas

- [[formularios-access]]
- [[subformularios-access]]
- [[consultas-access]]
- [[microsoft-access]]
- [[conversion-er-relacional]]
- [[practica-4-formularios]]
