# Operadores SQL

**Resumen**: Operadores disponibles en la cláusula WHERE de SQL: comparación, BETWEEN, IN, LIKE, operadores lógicos y expresiones aritméticas en SELECT.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_03.md

**Última actualización**: 2026-05-19

---

## Operadores de comparación

Se usan en la cláusula `WHERE` para filtrar registros (fuente: TI_06_03.md):

| Operador | Significado |
|----------|-------------|
| `=` | Igual |
| `<>` | Distinto |
| `<` | Menor que |
| `>=` | Mayor o igual que |

## BETWEEN

Selecciona registros cuyo valor está entre dos límites, **ambos inclusive** (fuente: TI_06_03.md):

```sql
SELECT * FROM items WHERE [year published] BETWEEN 1990 AND 1992;
```

Equivale a `>= 1990 AND <= 1992` pero resulta más legible.

## IN

Selecciona registros cuyo valor coincide con alguno de los valores de una lista. A diferencia de `BETWEEN`, no incluye los valores intermedios, solo los especificados (fuente: TI_06_03.md):

```sql
SELECT * FROM items WHERE [year published] IN (1990, 1992);
```

`IN` también se usa con [[sql-subconsultas|subconsultas]] que devuelven varios registros.

## LIKE

Busca registros cuyo campo de texto sigue un patrón. En Access el asterisco (`*`) representa cualquier conjunto de caracteres (fuente: TI_06_03.md):

```sql
SELECT * FROM items WHERE title LIKE "*SQL*";   -- contiene SQL en cualquier posición
SELECT * FROM items WHERE title LIKE "SQL*";    -- empieza por SQL
```

## Operadores lógicos: AND, OR, NOT

Permiten combinar varias condiciones (fuente: TI_06_03.md):

| Operador | Comportamiento |
|----------|---------------|
| `AND` | Deben cumplirse todas las condiciones |
| `OR` | Basta con cumplir una |
| `NOT` | Niega la condición |

```sql
SELECT * FROM items WHERE title LIKE "SQL*" AND [year published] = 1990;
SELECT * FROM items WHERE title LIKE "SQL*" OR  [year published] = 1990;
SELECT * FROM items WHERE title LIKE "SQL*" AND NOT [year published] = 1990;
```

## Expresiones aritméticas en SELECT

Se pueden incluir expresiones aritméticas en el `SELECT` para calcular valores derivados. Access admite suma, resta, multiplicación, división y funciones propias (fuente: TI_06_03.md):

```sql
SELECT title, [year published] + 100 FROM items;
```

## Páginas relacionadas

- [[sql-select]]
- [[sql-subconsultas]]
- [[sql-agrupacion]]
- [[ti6-sql]]
