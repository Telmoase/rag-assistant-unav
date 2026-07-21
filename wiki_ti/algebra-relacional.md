# Álgebra relacional

**Resumen**: Conjunto de operaciones formales sobre tablas de una base de datos relacional. Define el fundamento teórico de las consultas SQL y de Access.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_01.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_02.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_03.md

**Última actualización**: 2026-05-19

---

## Concepto

El álgebra relacional es el conjunto de operaciones que se pueden realizar sobre tablas de una base de datos. Los operandos son tablas y el resultado de cada operación es también una tabla. Las operaciones son análogas a las matemáticas: suma, resta, multiplicación, división y algunas específicas de tablas (fuente: TI_03_01.md).

## Clasificación

| Tipo | Operaciones |
|------|-------------|
| **Básicas unarias** | Selección, proyección |
| **Básicas binarias** | Unión, diferencia, producto cartesiano |
| **Derivadas** | Intersección, cociente, join |

Las operaciones derivadas se obtienen combinando las básicas (fuente: TI_03_01.md).

## Operaciones unarias

### Selección

Devuelve un subconjunto de las **filas** de una tabla: las que cumplen una condición (fuente: TI_03_01.md).

**Notación**: σ(tabla, condición)

Ejemplo: σ(R, C < 2) → solo las filas de R donde C es menor que 2.

### Proyección

Devuelve un subconjunto de las **columnas** de una tabla (fuente: TI_03_01.md).

**Notación**: π(tabla, columnas)

Ejemplo: π(R, A, C) → solo las columnas A y C de R.

Selección y proyección pueden combinarse para obtener a la vez las filas y las columnas deseadas. Son la base de las [[consultas-access|consultas en Access]]: la selección corresponde al filtro por criterio y la proyección a la elección de campos visibles. En SQL la selección se convierte en la cláusula `WHERE` y la proyección en la lista de campos del `SELECT` (fuente: TI_03_01.md). Véase [[sql-select]] para la sintaxis SQL completa.

## Operaciones binarias básicas

La unión y la diferencia requieren que ambas tablas tengan el mismo número de columnas y **dominios compatibles** (números con números, texto con texto, etc.) (fuente: TI_03_02.md).

### Unión

Combina los registros de dos tablas en una sola. Si un registro aparece en ambas, se incluye **una sola vez** (fuente: TI_03_02.md).

R ∪ S → todos los registros de R más los de S que no estaban ya en R.

### Diferencia

Devuelve los registros que están en la primera tabla pero **no** en la segunda (fuente: TI_03_02.md).

R − S → filas de R que no aparecen en S.

### Producto cartesiano

Combina **cada fila** de la primera tabla con **cada fila** de la segunda. El resultado tiene tantas columnas como la suma de columnas de ambas tablas y tantas filas como el producto del número de filas de cada una (fuente: TI_03_02.md).

Ejemplo: si R tiene 5 filas y S tiene 10, R × S tiene 50 filas.

Cuando ambas tablas comparten un nombre de campo, se antepone el nombre de la tabla como prefijo (R.C y S.C) para evitar ambigüedad (fuente: TI_03_02.md).

El producto cartesiano es la base del **join**.

## Operaciones derivadas

### Intersección

Devuelve los registros que están **a la vez** en las dos tablas (fuente: TI_03_03.md):

**R ∩ S = R − (R − S)**

### Cociente

El cociente de T entre S es la tabla que, al hacer el producto cartesiano por S, reproduce T. Tiene uso restringido y no se aplica en la parte práctica del curso (fuente: TI_03_03.md).

### Join (combinación)

La operación derivada **más importante**. Combina dos tablas por un campo común y devuelve solo los registros que tienen coincidencia en ese campo. El campo común aparece una sola vez en el resultado (fuente: TI_03_03.md).

**Proceso**:
1. Producto cartesiano de las dos tablas.
2. Selección de las filas donde el campo común coincide en ambas.
3. Se descartan los registros sin coincidencia.

Ejemplo: dadas R(A, C) y S(C, D), el join produce una tabla con columnas A, C, D, donde cada fila combina un registro de R con el de S que tiene el mismo valor en C.

En Access el join se realiza automáticamente al añadir tablas relacionadas a una consulta. Véase [[consultas-access]]. En SQL se implementa explícitamente con varias tablas en el `FROM` y condiciones de igualdad en el `WHERE`; véase [[sql-join]].

## Páginas relacionadas

- [[consultas-access]]
- [[sql-select]]
- [[sql-join]]
- [[modelo-relacional]]
- [[ti3-consultas]]
- [[ti6-sql]]
