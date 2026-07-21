# Funciones de agrupación y GROUP BY en SQL

**Resumen**: Las funciones de agrupación (COUNT, MIN, MAX, SUM, AVG) calculan un valor resumen sobre un conjunto de registros. GROUP BY agrupa por campo y HAVING filtra los grupos resultantes.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_05.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_06.md

**Última actualización**: 2026-05-19

---

## Funciones de agrupación

Las funciones de agrupación calculan un valor resumen a partir de un conjunto de registros. En lugar de devolver una fila por registro, devuelven un único valor calculado sobre todos los registros que cumplen la condición (fuente: TI_06_05.md):

| Función | Descripción |
|---------|-------------|
| `COUNT(*)` | Número de registros |
| `MIN(campo)` | Valor mínimo del campo |
| `MAX(campo)` | Valor máximo del campo |
| `SUM(campo)` | Suma de los valores del campo |
| `AVG(campo)` | Media de los valores del campo |

```sql
SELECT COUNT(*) FROM items WHERE [year published] = 1990;

SELECT MIN([year published]) AS minimo,
       MAX([year published]) AS maximo,
       COUNT(*) AS cantidad
FROM items
WHERE title LIKE "*SQL*";
```

## Alias con AS

`AS` asigna un nombre al campo resultado. Permite referenciarlo en consultas anidadas y hace el resultado más legible (fuente: TI_06_05.md):

```sql
SELECT COUNT(*) AS [Total libros] FROM items WHERE [year published] = 1990;
```

## Funciones en subconsultas

Los resultados de las funciones de agrupación son útiles como argumentos de [[sql-subconsultas|subconsultas]]. Por ejemplo, contar libros publicados en el año más reciente que apareció un libro de SQL (fuente: TI_06_05.md):

```sql
SELECT COUNT(*) AS cantidad FROM items
WHERE [year published] = (
    SELECT MAX([year published]) FROM items
    WHERE title LIKE "*SQL*"
);
```

## GROUP BY

`GROUP BY` agrupa los registros por el valor de un campo. Solo se puede mostrar en el `SELECT` el campo por el que se agrupa y funciones de agrupación; mostrar cualquier otro campo produce un error (fuente: TI_06_06.md):

```sql
SELECT [year published], COUNT(*) AS cantidad
FROM items
WHERE title LIKE "*SQL*"
GROUP BY [year published];
```

Devuelve una fila por cada año distinto, con el número de libros de ese año.

```sql
SELECT Au_ID, COUNT(*) AS [Cantidad libros]
FROM [Title Author]
GROUP BY Au_ID
ORDER BY COUNT(*) DESC;
```

Devuelve una fila por autor con su número de libros, ordenada de mayor a menor.

## HAVING

`HAVING` filtra los grupos resultantes, igual que `WHERE` filtra registros antes de agrupar. Se usa cuando la condición depende del resultado de una función de agrupación (fuente: TI_06_06.md):

```sql
SELECT Au_ID, COUNT(*) AS [Cantidad libros]
FROM [Title Author]
GROUP BY Au_ID
HAVING COUNT(*) > 1
ORDER BY COUNT(*) DESC;
```

Devuelve solo los autores con más de un libro.

## Orden de ejecución de SQL

El orden en que SQL evalúa las cláusulas es diferente del orden en que se escriben (fuente: TI_06_06.md):

| Paso | Cláusula | Qué hace |
|------|----------|----------|
| 1 | `FROM` | Obtiene los registros de la tabla |
| 2 | `WHERE` | Filtra los registros que cumplen la condición |
| 3 | `GROUP BY` | Agrupa los registros filtrados |
| 4 | `HAVING` | Filtra los grupos que cumplen la condición |
| 5 | `SELECT` | Calcula los campos y funciones a mostrar |
| 6 | `ORDER BY` | Ordena los resultados finales |

Por esto `HAVING` puede usar funciones de agrupación (ya calculadas en el paso 3) y `WHERE` no puede (aún no se han calculado).

## Páginas relacionadas

- [[sql-select]]
- [[sql-operadores]]
- [[sql-subconsultas]]
- [[sql-join]]
- [[ti6-sql]]
