# Práctica 3: Consultas

**Resumen**: Enunciado y ejercicios de la Práctica 3 de Tecnología de la Información. Consultas sobre la base de datos de albaranes, sobre Northbrick y sobre el sistema de información propio.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 3 - Consultas/Práctica 3. Consultas.md

**Última actualización**: 2026-05-19

---

El objeto Consulta de Access permite mostrar la información de las tablas de formas distintas y también insertar, modificar o eliminar datos de forma automatizada (fuente: Práctica 3. Consultas.md).

## Ejercicio 1: Base de datos de albaranes

**1. Consulta de proyección**
Mostrar número de albarán, nombre del conductor y nombre de la gasolinera. Requiere combinar varias tablas (fuente: Práctica 3. Consultas.md).

**2. Consulta de selección con parámetros**
Número de albaranes e importe total por camión y gasolinera para un periodo introducido por el usuario: `BETWEEN [Fecha Inicio] AND [Fecha Final]` (fuente: Práctica 3. Consultas.md).

**3. Consulta de tabla cruzada (crosstab)**
Importe total por camión (filas) y gasolinera (columnas) (fuente: Práctica 3. Consultas.md).

**4. Totales y ordenación**
Importes totales y número de albaranes por compañía, ordenados de mayor a menor importe (fuente: Práctica 3. Consultas.md).

**5. Consulta con expresiones**
Consumo total en litros por camión, asumiendo que el precio del gasoil se ha mantenido constante (fuente: Práctica 3. Consultas.md).

**6. Creación de tabla**
Crear la tabla `Hacienda` con el total facturado por cada compañía (fuente: Práctica 3. Consultas.md).

**7. Actualización**
Incrementar un 2% el precio de las gasolineras de CAMPSA, teniendo en cuenta que cada gasolinera puede tener un precio distinto (fuente: Práctica 3. Consultas.md).

**8. Borrado**
Eliminar los albaranes del año 2020 y anteriores. **Hacer copia de la tabla antes de ejecutar** (fuente: Práctica 3. Consultas.md).

**9. Consulta anidada**
Mostrar el camión que ha repostado más veces en una misma gasolinera y el número de veces. Requiere construir más de una consulta (fuente: Práctica 3. Consultas.md).

## Ejercicio 2: Base de datos Northbrick

Base de datos: `northbrick_2019.mdb` (fuente: Práctica 3. Consultas.md).

**1. Agrupación por categoría**
Para cada categoría de producto: número de productos y precio más alto (fuente: Práctica 3. Consultas.md).

**2. Verificación de precios**
Pedidos en los que el precio del pedido es distinto del precio del producto en la tabla de productos (fuente: Práctica 3. Consultas.md).

**3. Importe mensual**
Importe vendido por mes y año. Usar `Month(campo)` y `Year(campo)`. Considerar solo `UnitPrice × Quantity` sin descuento (fuente: Práctica 3. Consultas.md).

## Ejercicio 3: Trabajo de la asignatura

Describir el enunciado del sistema de información propio y diseñar 2 consultas elaboradas por cada miembro del equipo que muestren resultados relevantes para el sistema (fuente: Práctica 3. Consultas.md).

## Páginas relacionadas

- [[consultas-access]]
- [[ti3-consultas]]
- [[algebra-relacional]]
- [[microsoft-access]]
