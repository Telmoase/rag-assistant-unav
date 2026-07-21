# Tema 6: SQL

**Resumen**: Resumen del Tema 6 de Tecnología de la Información: SQL como lenguaje estándar para consultar bases de datos relacionales, desde la consulta básica hasta JOIN de múltiples tablas.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_02.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_03.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_04.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_04b.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_05.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_06.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_07.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_08.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/Step 2_ ij Basics.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 6 introduce SQL (*Structured Query Language*), el lenguaje estándar para consultar y manipular bases de datos relacionales. Las consultas del [[algebra-relacional]] que el Tema 3 construía con el editor gráfico de Access se expresan ahora directamente en SQL. El tema usa Access como entorno principal y [[apache-derby|Apache Derby]] como entorno secundario de práctica.

## Consulta básica

La estructura fundamental de una consulta SQL es [[sql-select|SELECT...FROM...WHERE...ORDER BY]]. La proyección (qué campos mostrar) va en `SELECT`; la selección (qué filas incluir), en `WHERE`; la ordenación, en `ORDER BY`. En Access se accede a la vista SQL desde el diseñador de consultas con Ctrl+punto (fuente: TI_06_02.md).

## Operadores

Los [[sql-operadores|operadores SQL]] permiten construir condiciones en `WHERE`: comparación (`=`, `<>`, `<`, `>=`), rangos (`BETWEEN`), listas (`IN`), patrones de texto (`LIKE`) y combinaciones lógicas (`AND`, `OR`, `NOT`). También se pueden incluir expresiones aritméticas en el `SELECT` (fuente: TI_06_03.md).

## Subconsultas y DISTINCT

Una [[sql-subconsultas|subconsulta]] es un `SELECT` dentro de otro `SELECT`. Se usa en el `WHERE` cuando el valor de filtro no es fijo sino el resultado de otra consulta. Si la subconsulta devuelve un solo valor se usa `=`; si puede devolver varios, `IN`. `DISTINCT` elimina duplicados del resultado y mejora el rendimiento de subconsultas (fuente: TI_06_04.md, TI_06_04b.md).

## Funciones de agrupación

Las [[sql-agrupacion|funciones de agrupación]] (`COUNT`, `MIN`, `MAX`, `SUM`, `AVG`) calculan un valor resumen sobre un conjunto de registros. `GROUP BY` agrupa los registros por un campo y `HAVING` filtra los grupos resultantes. El alias `AS` da nombre a los campos calculados. El orden de ejecución de SQL es: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY (fuente: TI_06_05.md, TI_06_06.md).

## JOIN de varias tablas

El [[sql-join|JOIN]] en SQL se implementa poniendo varias tablas en el `FROM` y añadiendo en el `WHERE` la condición de igualdad entre los campos comunes. Cada par de tablas adicional requiere una condición AND más. Cuando dos tablas tienen un campo con el mismo nombre se usa la notación `tabla.campo` para evitar ambigüedades (fuente: TI_06_07.md, TI_06_08.md).

## Páginas relacionadas

- [[sql-select]]
- [[sql-operadores]]
- [[sql-subconsultas]]
- [[sql-agrupacion]]
- [[sql-join]]
- [[apache-derby]]
- [[algebra-relacional]]
- [[consultas-access]]
- [[microsoft-access]]
