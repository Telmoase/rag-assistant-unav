# JOIN en SQL

**Resumen**: El JOIN en SQL combina registros de varias tablas mediante una condición de igualdad entre campos comunes. Se construye sobre el producto cartesiano filtrando solo las combinaciones con significado real.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_07.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_08.md

**Última actualización**: 2026-05-19

---

## Producto cartesiano como base

Cuando se incluyen dos tablas en el `FROM` sin ninguna condición de unión, SQL realiza el [[algebra-relacional|producto cartesiano]]: combina cada registro de la primera tabla con cada registro de la segunda (fuente: TI_06_07.md):

```sql
SELECT * FROM items, publishers;
```

Con 8.569 registros en `items` y 727 en `publishers`, el resultado tiene 8.569 × 727 = 6.229.663 registros. La mayoría de esas combinaciones no tienen ningún significado real (un libro combinado con una editorial que no lo publicó).

El producto cartesiano es la base del JOIN: añadiendo una condición `WHERE` que filtra solo los registros en los que el campo común coincide en ambas tablas se obtiene el JOIN (fuente: TI_06_07.md).

## JOIN de dos tablas

Se añade la condición de igualdad en el `WHERE`. Cuando dos tablas tienen un campo con el mismo nombre hay que usar la notación `tabla.campo` para evitar ambigüedad (fuente: TI_06_08.md):

```sql
SELECT * FROM titles, publishers
WHERE publishers.PubID = titles.PubID;
```

El resultado contiene solo los registros en los que el campo común coincide en ambas tablas. Los registros sin correspondencia se descartan (**inner join**) (fuente: TI_06_08.md).

## JOIN de más de dos tablas

Se añaden todas las tablas en el `FROM` y una condición de unión por cada par de tablas relacionadas. Con cuatro tablas se necesitan tres condiciones (fuente: TI_06_08.md):

```sql
SELECT * FROM titles, publishers, [title author], authors
WHERE titles.ISBN = [title author].ISBN
AND [title author].Au_ID = authors.Au_ID;
```

Cada condición `AND` une un par de tablas adicional.

## Proyección sobre el JOIN

Se puede limitar los campos mostrados especificándolos en el `SELECT`. Si el campo existe en varias tablas hay que indicar la tabla (fuente: TI_06_08.md):

```sql
SELECT titles.title, publishers.name
FROM titles, publishers, [title author], authors
WHERE titles.ISBN = [title author].ISBN
AND [title author].Au_ID = authors.Au_ID;
```

## Registros sin correspondencia

El JOIN solo devuelve registros que tienen correspondencia en **todas** las tablas unidas. Los registros sin correspondencia en alguna tabla relacionada se descartan del resultado (fuente: TI_06_08.md).

## Comparación con Access y el álgebra relacional

En el editor gráfico de [[consultas-access|Access]], el JOIN se realiza automáticamente al añadir tablas relacionadas a una consulta. En SQL hay que expresarlo explícitamente. La operación es la misma que el [[algebra-relacional|join del álgebra relacional]]: producto cartesiano + selección por igualdad del campo común.

## Páginas relacionadas

- [[sql-select]]
- [[sql-agrupacion]]
- [[algebra-relacional]]
- [[consultas-access]]
- [[ti6-sql]]
