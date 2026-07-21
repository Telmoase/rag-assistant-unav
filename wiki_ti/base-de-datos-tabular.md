# Base de datos tabular

**Resumen**: Una base de datos tabular organiza la información en tablas formadas por registros (filas) y campos (columnas). Es el modelo fundamental de las bases de datos relacionales.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_03.md

**Última actualización**: 2026-05-19

---

## Los tres elementos principales

Una base de datos tabular se organiza en torno a tres conceptos fundamentales (fuente: TI_01_03.md):

**Tabla**: el conjunto completo de datos, formado por todos los registros y todos los campos. Equivale a un fichero [[formato-csv|CSV]] completo o a una hoja de Excel.

**Registro**: cada una de las filas de la tabla. Representa un elemento individual del conjunto de datos. Ejemplo: cada color en la base de datos LEGO es un registro (135 en total).

**Campo**: cada una de las columnas de la tabla. Define un atributo concreto almacenado para todos los registros. Ejemplo: `name`, `rgb`, `is_trans`.

## Tipos de datos de un campo

Los campos pueden almacenar distintos tipos de datos (fuente: TI_01_03.md):

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Texto** (alfanumérico) | Cadenas de caracteres | `name`: "Red", "Blue" |
| **Numérico** | Enteros o decimales | `id`: 1, 2, 3… |
| **Booleano** | Solo verdadero o falso | `is_trans`: si el color es transparente |

## La clave primaria

Un campo cuya función es **identificar de forma inequívoca** cada registro se llama **clave primaria**. Sus valores deben ser únicos para cada registro de la tabla (fuente: TI_01_03.md).

Ejemplo: el campo `id` en la tabla de colores LEGO actúa como clave primaria porque ningún color tiene el mismo identificador.

Para los criterios de elección de la clave primaria (claves significativas vs autonumérico) véase [[eleccion-claves]].

## Diseño de sistemas de información

Al diseñar un sistema de información se definen qué tablas son necesarias, qué campos tiene cada una y cómo se relacionan entre sí. Véase [[practica-1-datos-y-tablas]] para un ejemplo de diseño del sistema Codex.

## Páginas relacionadas

- [[formato-csv]]
- [[microsoft-access]]
- [[modelo-relacional]]
- [[ti1-datos-y-tablas]]
