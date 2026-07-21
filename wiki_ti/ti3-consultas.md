# Tema 3: Consultas

**Resumen**: Resumen del Tema 3 de Tecnología de la Información. Cubre el álgebra relacional como fundamento teórico y las consultas en Microsoft Access como implementación práctica.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_01.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_02.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_03.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_04.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_05.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/Práctica 3. Consultas.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 3 enseña a recuperar y transformar datos almacenados en una base de datos. El bloque teórico (álgebra relacional) formaliza qué operaciones son posibles sobre tablas; el bloque práctico (consultas en Access) muestra cómo ejecutarlas con una interfaz gráfica.

## Bloque 1: Álgebra relacional

El [[algebra-relacional]] define ocho operaciones formales sobre tablas, clasificadas en tres grupos:

- **Unarias**: selección (filtra filas: `σ`) y proyección (filtra columnas: `π`).
- **Binarias básicas**: unión, diferencia y producto cartesiano. La unión y la diferencia exigen dominios compatibles entre las tablas.
- **Derivadas**: intersección, cociente y **join**. El join es la operación más importante del tema: combina dos tablas por su campo común descartando los registros sin coincidencia, y es la base de casi todas las consultas reales.

## Bloque 2: Consultas en Access

Las [[consultas-access|consultas en Access]] implementan el álgebra relacional de forma visual:

- **Consultas básicas**: criterios en la misma fila se combinan con AND; en filas distintas, con OR. Los campos pueden mostrarse u ocultarse.
- **Totales y agrupaciones**: `Group By` con funciones de agregación (Suma, Media, Mínimo, Máximo, Contar, Desviación).
- **Tabla cruzada (crosstab)**: formato matricial filas × columnas con un valor en cada cruce.
- **Varias tablas**: Access realiza el join automáticamente a partir de las relaciones definidas.
- **Filtros por fecha**: delimitador `#fecha#`; rangos con `BETWEEN`.
- **Parámetros**: valores entre corchetes que el usuario introduce en cada ejecución.
- **Consultas de acción**: creación de tabla, actualización y borrado. Modifican datos reales y piden confirmación. Importante: hacer siempre copia de seguridad antes de ejecutar borrados o actualizaciones masivas.

## Práctica

Los ejercicios de [[practica-3-consultas|Práctica 3]] aplican todos estos conceptos sobre la base de datos de albaranes (9 ejercicios), sobre la base de datos Northbrick (3 ejercicios) y sobre el sistema de información propio del trabajo de la asignatura.

## Páginas relacionadas

- [[algebra-relacional]]
- [[consultas-access]]
- [[modelo-relacional]]
- [[microsoft-access]]
- [[practica-3-consultas]]
