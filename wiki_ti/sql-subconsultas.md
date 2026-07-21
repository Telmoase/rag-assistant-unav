# Subconsultas y DISTINCT en SQL

**Resumen**: Una subconsulta es un SELECT anidado dentro de otro. Se usa cuando el valor de filtro es el resultado de otra consulta. DISTINCT elimina duplicados del resultado.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_04.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_04b.md

**Última actualización**: 2026-05-19

---

## Qué es una subconsulta

Una subconsulta es una sentencia `SELECT` incluida dentro de otra sentencia SQL. El resultado de la subconsulta se usa como argumento de la consulta principal, normalmente en la cláusula `WHERE` (fuente: TI_06_04.md).

**Cuándo usarlas**: cuando el valor con el que se quiere filtrar no es un dato fijo sino el resultado de otra consulta. Por ejemplo: mostrar todos los libros publicados en el mismo año que un libro concreto.

## Subconsulta con un solo resultado: `=`

Si la subconsulta devuelve un único valor se puede usar con el operador igual. La subconsulta debe devolver un único campo y un único registro; si devuelve varios campos, da error (fuente: TI_06_04.md):

```sql
SELECT * FROM items
WHERE [year published] = (
    SELECT [year published] FROM items
    WHERE title LIKE "SQL*end"
);
```

## Subconsulta con varios resultados: `IN`

Si la subconsulta puede devolver varios registros no se puede usar `=`. Se usa `IN`, que comprueba si el valor está en la lista de resultados (fuente: TI_06_04.md):

```sql
SELECT * FROM items
WHERE [year published] IN (
    SELECT [year published] FROM items
    WHERE title LIKE "SQL*"
);
```

Devuelve todos los libros publicados en cualquiera de los años en que se publicó algún libro con SQL en el título.

## Subconsultas con varias tablas

Las subconsultas permiten encadenar consultas sobre tablas distintas. Por ejemplo, para obtener todos los libros escritos por los autores de un libro concreto (fuente: TI_06_04.md):

1. Identificar el libro por su ISBN.
2. Consultar la tabla de autores para obtener los autores de ese libro.
3. Usar esos autores como filtro para obtener todos los libros que han escrito.

Cada paso se implementa como una subconsulta anidada dentro de la siguiente.

## DISTINCT

`DISTINCT` elimina los duplicados del resultado, devolviendo cada valor solo una vez (fuente: TI_06_04b.md):

```sql
SELECT DISTINCT [year published] FROM items
WHERE title LIKE "SQL*";
```

**Por qué mejora el rendimiento**: cuando una subconsulta devuelve valores repetidos, la consulta principal realiza comparaciones innecesarias con cada duplicado. Usando `DISTINCT` en la subconsulta se reduce el número de comparaciones sin cambiar el resultado final.

`DISTINCT` se puede aplicar a cualquier `SELECT`, no solo a subconsultas (fuente: TI_06_04b.md).

## Páginas relacionadas

- [[sql-select]]
- [[sql-operadores]]
- [[sql-agrupacion]]
- [[ti6-sql]]
