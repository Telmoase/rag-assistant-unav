# Modelo relacional

**Resumen**: El modelo relacional (Codd, 1970) implementa una base de datos como un conjunto de tablas con propiedades formales. Es el modelo en el que se basan los gestores de bases de datos actuales.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_03.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Modelo Entidad-Relación.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_03.md

**Última actualización**: 2026-05-19

---

## Qué es el modelo relacional

El modelo relacional fue creado por Codd en 1970. Mientras el [[modelo-entidad-relacion|modelo ER]] sirve para el diseño conceptual, el modelo relacional permite implementar una base de datos real: los datos se almacenan en tablas y las relaciones entre entidades se representan como referencias entre tablas (fuente: TI_02_03.md).

## Propiedades de una tabla

Una tabla bien formada en el modelo relacional cumple estas propiedades (fuente: TI_02_03.md, Modelo Entidad-Relación.md):

- El tipo de fila es único: la estructura de la tabla define qué datos puede contener.
- **No hay filas duplicadas**: cada fila se identifica de forma única.
- Cada columna tiene un nombre propio.
- Cada celda contiene un único valor (esto es la **Primera Forma Normal**).
- Los valores de una columna pertenecen al **dominio** definido para ella: un tipo de dato o un conjunto restringido de valores.

## Terminología

Los elementos de una tabla tienen nombres equivalentes según el contexto (fuente: TI_02_03.md):

| Concepto | Sinónimos |
|----------|-----------|
| Columna | Campo, atributo |
| Fila | Tupla, registro |

## La clave

La **clave** es el campo (o conjunto de campos) que identifica de forma única cada registro. No puede haber dos registros con la misma clave (fuente: TI_02_03.md). Para los criterios de elección de la clave primaria (claves significativas vs no significativas) véase [[eleccion-claves]].

## Relaciones entre tablas

Las relaciones entre entidades del modelo ER se implementan como referencias entre tablas (fuente: TI_02_03.md):

- En la mayoría de casos basta con incluir en una tabla la **clave de la tabla relacionada**. Este campo se denomina **clave foránea** (*foreign key*): apunta a la clave primaria de la tabla relacionada (fuente: TI_04_03.md).
- Cuando existe una relación **N:N** es necesario crear una **tabla intermedia** cuya clave es la combinación de las claves de las dos tablas que relaciona.

Ejemplo del laboratorio médico: la relación N:N entre Petición y Prueba genera la tabla **Detalle Petición**, con clave compuesta por (id_petición, id_prueba).

Para las reglas detalladas véase [[conversion-er-relacional]].

## Índices

Los índices permiten acceder a los registros de forma rápida sin recorrer la tabla entera, de forma similar al índice de una guía telefónica (fuente: Modelo Entidad-Relación.md). En Access se crean desde el botón **Índices** en la vista de diseño de la tabla; pueden ser simples (un campo) o compuestos (varios campos). Véase [[indices-access]] para una guía completa.

## Páginas relacionadas

- [[modelo-entidad-relacion]]
- [[conversion-er-relacional]]
- [[normalizacion]]
- [[integridad-referencial]]
- [[base-de-datos-tabular]]
- [[indices-access]]
- [[eleccion-claves]]
- [[ti2-relaciones]]
