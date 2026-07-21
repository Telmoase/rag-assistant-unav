# Consultas en Access

**Resumen**: Guía de uso de consultas en Microsoft Access: desde las consultas básicas de selección hasta las consultas de acción (creación de tabla, actualización, borrado).

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_04.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_05.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/Práctica 3. Consultas.md

**Última actualización**: 2026-05-19

---

## Qué es una consulta

Una consulta en Access permite recuperar datos de una o varias tablas aplicando filtros, seleccionando campos y realizando operaciones sobre los datos. Equivale a las operaciones del [[algebra-relacional]]: la selección filtra filas y la proyección elige columnas (fuente: TI_03_04.md). Cada consulta del diseñador gráfico tiene un equivalente en SQL visible desde la vista SQL; véase [[sql-select]].

## Crear una consulta básica

En el diseño de consulta la **parte superior** muestra las tablas que participan y la **parte inferior** contiene los campos a mostrar. Añadir el asterisco (`*`) equivale a incluir todos los campos de la tabla, como ver la tabla directamente (fuente: TI_03_04.md).

## Criterios de filtro

Para filtrar filas se añade un criterio en el campo correspondiente (fuente: TI_03_04.md):

- **Valor exacto**: `gasolinera = 3`
- **Expresión**: `gasolinera < 3`

| Posición del criterio | Operador lógico |
|-----------------------|----------------|
| Misma fila | AND — deben cumplirse todos |
| Filas distintas | OR — basta con cumplir uno |

Cada campo tiene una casilla para mostrarlo u ocultarlo: permite usar un campo como filtro sin que aparezca en el resultado (fuente: TI_03_04.md).

## Ordenar resultados

Se puede ordenar por cualquier campo (ascendente o descendente) desde la fila **Orden** del diseño (fuente: TI_03_04.md).

## Totales y agrupaciones

Activando la fila **Total** se pueden aplicar operaciones de agregación (fuente: TI_03_04.md):

| Opción | Efecto |
|--------|--------|
| Agrupar por | Agrupa registros por el valor del campo |
| Suma | Suma los valores del campo en cada grupo |
| Media | Calcula la media del grupo |
| Mínimo / Máximo | Valor mínimo o máximo del grupo |
| Contar | Número de registros del grupo |
| Desviación | Desviación estándar del grupo |

Ejemplo: agrupar por gasolinera y sumar el importe → total gastado en cada gasolinera. Añadir también el campo camión con Group By → total por combinación de gasolinera y camión (fuente: TI_03_04.md).

## Consulta de tabla cruzada (crosstab)

Presenta los datos en formato matricial. El asistente de Access pide tres elementos (fuente: TI_03_04.md):

1. El campo que forma las **filas** (ej.: camión).
2. El campo que forma las **columnas** (ej.: gasolinera).
3. El **valor** en el cruce y la operación a aplicar (ej.: suma del importe).

## Consultas con varias tablas

Al añadir varias tablas al diseño, Access muestra automáticamente las relaciones definidas y realiza el **join** de forma implícita (véase [[algebra-relacional]]). Si se añaden los asteriscos de varias tablas, los campos pueden duplicarse; la solución es eliminar los asteriscos y seleccionar solo los campos necesarios (fuente: TI_03_05.md).

## Filtros por fecha

Access usa el símbolo `#` como delimitador de fechas (fuente: TI_03_05.md):

| Criterio | Sintaxis |
|----------|----------|
| Fecha exacta | `#20/09/2019#` |
| Posterior a | `> #20/09/2019#` |
| Igual o posterior | `>= #20/09/2019#` |
| Rango con parámetros | `BETWEEN [Fecha Inicio] AND [Fecha Final]` |

## Consultas con parámetros

En lugar de un valor fijo en el criterio, se escribe un nombre entre corchetes: `[Fecha de filtro]`. Access solicita el valor al usuario cada vez que ejecuta la consulta, permitiendo reutilizarla con distintos valores sin modificar su diseño (fuente: TI_03_05.md).

## Consultas de acción

A diferencia de las consultas de selección, estas modifican los datos reales. Access pide confirmación antes de ejecutarlas.

### Creación de tabla

Genera una nueva tabla a partir del resultado de una consulta. Se configura indicando el nombre de la nueva tabla. Al ejecutarla (no al previsualizarla), Access inserta los registros e informa del número de filas creadas. Es útil para crear tablas de trabajo sin alterar las originales (fuente: TI_03_05.md).

### Actualización

Modifica los valores de un campo en los registros que cumplan un criterio. Se configura indicando (fuente: TI_03_05.md):

- El campo que se va a actualizar.
- El nuevo valor (puede ser una expresión, ej.: `[importe] / 2`).
- El criterio que limita los registros afectados (ej.: `importe >= 300`).

Access avisa del número de registros que se van a modificar y pide confirmación antes de aplicar los cambios.

### Borrado

Elimina los registros que cumplan un criterio. **Hacer siempre una copia de la tabla antes de ejecutarla** (fuente: Práctica 3. Consultas.md).

## Páginas relacionadas

- [[algebra-relacional]]
- [[sql-select]]
- [[sql-agrupacion]]
- [[sql-join]]
- [[microsoft-access]]
- [[integridad-referencial]]
- [[practica-3-consultas]]
- [[ti3-consultas]]
- [[ti6-sql]]
