# Tema 5: Informes

**Resumen**: Resumen del Tema 5 de Tecnología de la Información: índices de base de datos, criterios para elegir claves primarias e informes en Access.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_01.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_02.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_03.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_04.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_06.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/Práctica 5. Informes.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 5 abarca tres áreas complementarias: la estructura interna de los índices, los criterios para elegir claves primarias y la creación de informes en Access para presentar datos de forma estructurada.

## Índices

Un [[indices-access|índice]] es una estructura adicional que permite acceder rápidamente a registros sin recorrer toda la tabla. La clave primaria es siempre un índice; se pueden crear índices adicionales sobre cualquier campo. Los índices pueden ser simples (un campo) o compuestos (varios campos) (fuente: TI_05_01.md).

## Elección de claves

La [[eleccion-claves|elección de la clave primaria]] es una decisión crítica de diseño. Las claves significativas (DNI, matrícula) presentan problemas de unicidad y posibilidad de cambio; la solución recomendada es una clave no significativa generada automáticamente: el campo autonumérico de Access (fuente: TI_05_03.md).

## Integridad referencial

La [[integridad-referencial]] garantiza que los datos entre tablas sean coherentes. El Tema 5 detalla los mecanismos de integridad (tipo de dato, nulos, unicidad, reglas, triggers) y advierte que el comportamiento en cascada es el más peligroso, mientras que Restrict es el más seguro (fuente: TI_05_04.md).

## Informes en Access

Los [[informes-access|informes]] son el mecanismo de Access para presentar e imprimir datos de forma estructurada. Se crean a partir de una consulta, permiten agrupar registros por campos y configurar la orientación de impresión (fuente: TI_05_06.md).

## Práctica 5

Ver [[practica-5-informes]] para los ejercicios de listados simples, agrupación, totales y campos calculados sobre consumo.

## Páginas relacionadas

- [[indices-access]]
- [[eleccion-claves]]
- [[integridad-referencial]]
- [[informes-access]]
- [[practica-5-informes]]
- [[microsoft-access]]
