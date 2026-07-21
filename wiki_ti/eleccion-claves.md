# Elección de claves primarias

**Resumen**: Criterios para elegir la clave primaria de una tabla: los problemas de las claves significativas (DNI, matrícula) y la ventaja de las claves no significativas generadas automáticamente.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_03.md

**Última actualización**: 2026-05-19

---

## Qué es la clave primaria

La clave primaria es el índice principal de una tabla. Identifica cada registro de forma única y es el campo que se usa para establecer la [[integridad-referencial]] con otras tablas (fuente: TI_05_03.md).

## Claves significativas y sus problemas

Una **clave significativa** es un campo que tiene un valor real asociado a la entidad: el DNI de una persona, la matrícula de un vehículo. Aunque parecen buenas claves porque identifican de forma natural a la entidad, presentan dos problemas (fuente: TI_05_03.md):

**No unicidad**: pueden darse situaciones en que el valor no sea único. Por ejemplo, errores en la expedición de DNIs, o personas extranjeras con un número de carnet distinto al DNI.

**Posibilidad de cambio**: el valor puede cambiar con el tiempo. Un vehículo puede cambiar de matrícula por un trámite administrativo. Si la matrícula era la clave de la tabla de vehículos, ese cambio afecta a todos los registros de otras tablas que hacían referencia a ese vehículo, lo que es una operación compleja y propensa a errores.

## Claves no significativas

La solución recomendada es una **clave no significativa**: un número correlativo o aleatorio que no representa ningún atributo real de la entidad. Al no tener valor externo asociado, no existe ningún condicionante que obligue a cambiarlo (fuente: TI_05_03.md).

| | Clave significativa | Clave no significativa |
|---|---|---|
| **Unicidad** | No garantizada (errores, excepciones) | Garantizada (generada por el sistema) |
| **Estabilidad** | Puede cambiar (trámites, correcciones) | Estable por definición |
| **Legibilidad** | Aporta información propia | Sin valor propio (opaca) |

Inconveniente de la clave no significativa: no aporta información por sí misma. Para saber a qué entidad corresponde el identificador 1042 hay que consultar la tabla (fuente: TI_05_03.md).

## Criterio de elección

Al elegir la clave primaria hay que asegurarse de que el campo sea duradero y no cambie. Si no puede garantizarse esa estabilidad, la mejor opción es una clave no significativa generada automáticamente: el campo **autonumérico** en Access (fuente: TI_05_03.md).

## Páginas relacionadas

- [[indices-access]]
- [[modelo-relacional]]
- [[integridad-referencial]]
- [[ti5-informes]]
