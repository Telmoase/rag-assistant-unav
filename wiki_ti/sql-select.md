# SQL: consulta básica (SELECT)

**Resumen**: Estructura fundamental de una consulta SQL — SELECT, FROM, WHERE, ORDER BY — y cómo acceder a la vista SQL en Microsoft Access.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_02.md, Raw/Tecnologia de la informacion/Tema 6 - SQL/TI_06_03.md

**Última actualización**: 2026-05-19

---

## Estructura básica

La consulta SQL más básica tiene la forma (fuente: TI_06_02.md):

```sql
SELECT campos FROM tabla WHERE condición ORDER BY campo;
```

| Cláusula | Función | Equivalente en álgebra relacional |
|----------|---------|----------------------------------|
| `SELECT` | Campos que se quieren mostrar | Proyección (π) |
| `FROM` | Tabla sobre la que se consulta | — |
| `WHERE` | Condición para filtrar filas | Selección (σ) |
| `ORDER BY` | Campo por el que se ordenan los resultados | — |

Las cláusulas `WHERE` y `ORDER BY` son opcionales (fuente: TI_06_02.md).

## Proyección: SELECT

La proyección elige qué columnas mostrar. El asterisco (`*`) selecciona todas; con nombres concretos se elige un subconjunto. Los nombres de campo con espacios van entre corchetes (fuente: TI_06_02.md):

```sql
SELECT title, [year published], ISBN FROM items;
```

## Selección: WHERE

La selección filtra qué filas se incluyen en el resultado (fuente: TI_06_02.md):

```sql
SELECT * FROM items WHERE [year published] = 1990;
```

## Ordenación: ORDER BY

Ordena los resultados por el campo indicado, ascendente por defecto. Para orden descendente se añade `DESC` (fuente: TI_06_03.md):

```sql
SELECT * FROM items WHERE [year published] = 1990 ORDER BY title;
SELECT * FROM items ORDER BY [year published] DESC;
```

## Vista SQL en Access

Para escribir SQL en Access (fuente: TI_06_02.md):

1. Crear una consulta en modo diseño (Crear → Diseño de consulta).
2. Cerrar el selector de tablas sin elegir ninguna.
3. Cambiar a la **vista SQL** desde el menú de vistas.

Atajos para alternar entre vista SQL y vista de resultados (fuente: TI_06_02.md):
- `Ctrl + .` → vista SQL
- `Ctrl + ,` → vista de datos (resultados)

El tamaño de fuente del editor SQL se configura en Archivo → Opciones → Diseñador de objetos (fuente: TI_06_02.md).

Cualquier consulta creada con el editor gráfico de Access tiene su equivalente SQL visible en la vista SQL. Las consultas SQL más complejas van más allá de lo que permite construir el editor gráfico (fuente: TI_06_02.md).

## Páginas relacionadas

- [[sql-operadores]]
- [[sql-subconsultas]]
- [[sql-agrupacion]]
- [[sql-join]]
- [[algebra-relacional]]
- [[consultas-access]]
- [[microsoft-access]]
- [[ti6-sql]]
