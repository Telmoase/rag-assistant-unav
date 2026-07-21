# Tema 1: Datos y tablas

**Resumen**: Resumen del Tema 1 de Tecnología de la Información. Cubre la representación de datos en binario, el estándar ASCII, el formato CSV y los fundamentos de bases de datos tabulares con Microsoft Access.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_00a.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_00b.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_01.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_02.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_03.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_04.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_05.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_05b.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/Tabla ASCII.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/Práctica 1. Datos y tablas.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 1 sienta las bases sobre cómo se almacenan y organizan los datos en un ordenador. Se parte del nivel más bajo (bits y bytes) y se asciende hasta las bases de datos tabulares y su gestión con herramientas de escritorio.

## Bloque 1: Representación de datos en binario

Los ordenadores almacenan todo en binario (0s y 1s). Para trabajar con esos datos de forma humana se usan sistemas de numeración alternativos:

- **[[sistemas-de-numeracion]]**: decimal, binario, octal y hexadecimal. Conversión por divisiones sucesivas; conversión rápida agrupando bits (1 dígito hex = 4 bits, 1 dígito octal = 3 bits).
- **[[codigo-ascii]]**: estándar que asigna un número a cada carácter de texto. Cada carácter ocupa un byte; la tabla ASCII cubre 0–127 (7 bits), con extensión 128–255 para caracteres de otros idiomas. Diferencia mayúscula/minúscula = 32 decimal.

## Bloque 2: Ficheros CSV

El [[formato-csv|formato CSV]] es la forma más simple de almacenar datos tabulares en texto plano:
- Primera línea = cabecera; resto = registros.
- El separador puede ser coma (`,`) o punto y coma (`;`) según la configuración regional.
- El fin de línea varía: `\n` en Unix/Mac, `\r\n` en Windows.
- Siempre inspeccionar el fichero antes de procesarlo con código.

## Bloque 3: Bases de datos tabulares

Una [[base-de-datos-tabular]] organiza la información en **tablas** (registros × campos). Los campos tienen tipos de dato (texto, numérico, booleano) y uno de ellos actúa como **clave primaria** para identificar cada registro de forma inequívoca.

## Bloque 4: Microsoft Access

[[microsoft-access|Microsoft Access]] es la herramienta de escritorio usada en la práctica. Permite:
- Definir la estructura de una tabla manualmente en **vista de diseño**.
- Importar datos directamente desde CSV mediante el **asistente de importación**.
- Pegar datos desde Excel, previa limpieza de incompatibilidades (especialmente en campos booleanos).

## Práctica

Los conceptos del tema se aplican en [[practica-1-datos-y-tablas|Práctica 1]]: contar registros en un CSV de LEGO, visualizar datos en distintas herramientas, importar un CSV de albaranes en Access y diseñar las tablas del sistema de información Codex.

## Páginas relacionadas

- [[sistemas-de-numeracion]]
- [[codigo-ascii]]
- [[formato-csv]]
- [[base-de-datos-tabular]]
- [[microsoft-access]]
- [[practica-1-datos-y-tablas]]
