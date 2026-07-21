# Práctica 1: Datos y tablas

**Resumen**: Ejercicios prácticos del Tema 1 de Tecnología de la Información: lectura de CSV, visualización con distintas herramientas, importación en Access y diseño de un sistema de información.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/Práctica 1. Datos y tablas.md

**Última actualización**: 2026-05-19

---

## Ejercicio 1: Contar registros en parts.csv

Leer el fichero `parts.csv` (base de datos LEGO, disponible en Kaggle) y determinar cuántos registros contiene. Indicar el código del producto en la posición 1000, contando desde 1 (fuente: Práctica 1. Datos y tablas.md).

Herramientas sugeridas: Excel, Notepad++, o cualquier aplicación considerada adecuada.

## Ejercicio 2: Visualización de CSV

Realizar ejercicios de visualización de CSV en línea y comprobar la representación de los registros de `parts.csv`. Analizar las demás tablas de la base de datos LEGO en Kaggle para entender la razón de su diseño en función de sus campos y contenido (fuente: Práctica 1. Datos y tablas.md).

Herramientas: Excel, Notepad++, hexed.it (editor hexadecimal online).

## Ejercicio 3: Base de datos Access con albaranes

Crear una base de datos en Access con una tabla que contenga los datos de `AlbaranesDatos.csv`. Se recomienda abrir el fichero con Notepad++ antes de importarlo para inspeccionar su contenido (fuente: Práctica 1. Datos y tablas.md).

Véase [[microsoft-access]] para el proceso de importación.

## Ejercicio 4: Diseño del sistema de información Codex

Definir las tablas necesarias en papel y luego en Access para implementar el sistema Codex (fuente: Práctica 1. Datos y tablas.md).

**Requisitos del sistema:**
- El profesor define preguntas para una asignatura y puede activar algunas de ellas.
- El profesor puede indicar qué respuestas anteriores son visibles con su calificación.
- El alumno accede con usuario y contraseña, responde las preguntas activas y obtiene su calificación.
- Las respuestas y calificaciones persisten entre sesiones.

**Posibles tablas** (fuente: Práctica 1. Datos y tablas.md):
- `Asignaturas` — lista de asignaturas
- `Preguntas` — preguntas por asignatura (con estado activa/inactiva y flag de visible)
- `Alumnos` — usuario y contraseña
- `Respuestas` — respuesta de cada alumno a cada pregunta, con su calificación

Cada tabla debe tener entre 2 y 5 registros de ejemplo.

Véase [[base-de-datos-tabular]] para los conceptos de tabla, registro, campo y clave primaria.

## Páginas relacionadas

- [[formato-csv]]
- [[base-de-datos-tabular]]
- [[microsoft-access]]
- [[ti1-datos-y-tablas]]
