# Índices en bases de datos

**Resumen**: Un índice es una estructura que permite acceder rápidamente a registros de una tabla sin recorrerla entera, almacenando solo el campo de ordenación y referencias a los registros, sin duplicar datos.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_01.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_02.md

**Última actualización**: 2026-05-19

---

## Qué es un índice

Un índice es una estructura adicional que permite acceder rápidamente a los registros de una tabla sin recorrerla entera. Equivale a tener los registros ordenados por un campo concreto, pero sin reordenar físicamente la tabla (fuente: TI_05_01.md).

## Por qué son necesarios

Sin índices, buscar un registro requiere recorrer la tabla desde el principio hasta encontrarlo. Con millones de registros esto es inviable. La analogía clásica: buscar un nombre en una guía telefónica ordenada por número de teléfono es posible, pero muy lento (fuente: TI_05_01.md).

La solución naive —almacenar la tabla varias veces ordenada por distintos campos— supone duplicar toda la información. Los índices resuelven esto almacenando solo el campo de ordenación y la referencia al registro correspondiente, sin duplicar el resto de la información. Una biblioteca tradicional tenía fichas ordenadas por autor y otras por título: cada conjunto era un índice (fuente: TI_05_01.md).

## Tipos de índices

- **Clave primaria**: índice principal de la tabla, marcado con el símbolo de llave en Access. Exige que los valores sean únicos y no nulos. Solo puede haber uno por tabla (fuente: TI_05_01.md).
- **Índices adicionales**: se pueden definir sobre cualquier campo o combinación de campos. Propiedades configurables:
  - **Único**: impide que haya valores duplicados en ese campo.
  - **Permite nulos**: indica si el campo puede quedar sin valor.

## Índices compuestos

Un índice puede estar formado por varios campos. En Access se crea asignando el mismo nombre a varias filas en el panel de índices, indicando en cada fila un campo distinto que forma parte del mismo índice (fuente: TI_05_01.md).

## Cómo funciona la creación

Cuando se define un nuevo índice, la base de datos realiza dos operaciones (fuente: TI_05_02.md):

1. Ordena todos los registros existentes por el campo indicado.
2. Crea la estructura de índice que almacena esa ordenación junto con las referencias a cada registro.

A partir de ese momento, las búsquedas por ese campo consultan primero el índice para localizar el registro y acceden directamente a él, sin recorrer la tabla entera.

## Creación en Access

En el diseño de una tabla, el botón **Índices** muestra los índices definidos y permite crear nuevos. Siempre aparece el índice de la clave primaria; se pueden añadir índices adicionales indicando el nombre del índice, el campo y sus propiedades (fuente: TI_05_01.md).

## Páginas relacionadas

- [[eleccion-claves]]
- [[modelo-relacional]]
- [[microsoft-access]]
- [[ti5-informes]]
