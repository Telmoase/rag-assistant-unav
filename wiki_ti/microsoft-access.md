# Microsoft Access

**Resumen**: Microsoft Access es un gestor de bases de datos de escritorio que permite crear tablas, definir relaciones e índices, realizar consultas, construir formularios e interfaces de usuario, y generar informes para presentar e imprimir datos.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_04.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_05.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_05b.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_07.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_04.md, Raw/Tecnologia de la informacion/Tema 3 - Consultas/TI_03_05.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_01.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_02.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_03.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_04.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_05.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_01.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_02.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_06.md

**Última actualización**: 2026-05-19

---

## Crear una tabla en vista de diseño

La **vista de diseño** permite definir la estructura de una tabla campo a campo. Cada fila de la vista representa un campo (columna) de la tabla (fuente: TI_01_04.md).

Para cada campo se especifica su nombre y su tipo de dato. Importante: evitar palabras reservadas de Access como nombre de campo (p. ej., `name` puede causar errores; usar `nombre_color` en su lugar).

Ejemplo de tabla `colores` con los campos de la base de datos LEGO:

| Campo | Tipo en Access | Notas |
|-------|---------------|-------|
| `id` | Numérico | Cambiar de autonumérico si se importan los valores propios del CSV |
| `nombre_color` | Texto corto | Hasta 255 caracteres |
| `rgb` | Texto corto | Código alfanumérico |
| `es_transparente` | Sí/No (booleano) | Se muestra como casilla de verificación |

## Vista de datos

La **vista de datos** es donde se introducen y consultan los registros. Los cambios se guardan automáticamente al pasar al siguiente registro, sin necesidad de guardar explícito (fuente: TI_01_04.md).

## Importar datos desde Excel (copiar y pegar)

Para cargar muchos registros sin introducirlos manualmente (fuente: TI_01_04.md):

1. Abrir el CSV en Excel y preparar los datos.
2. Resolver incompatibilidades antes de pegar. Problema frecuente con campos booleanos: Access espera `verdadero`/`falso`, pero el CSV puede usar `T`/`F`. Solución: **buscar y reemplazar** en Excel (`F` → `falso`, `T` → `verdadero`) antes de pegar.
3. Seleccionar toda la tabla en Excel y pegarla en Access.

## Importar un CSV con el asistente de importación

Access incluye un asistente de importación de ficheros de texto (fuente: TI_01_05.md):

1. Indicar que se importa en una nueva tabla de la base de datos actual.
2. El asistente detecta automáticamente el separador del fichero.
3. Revisar y ajustar los tipos de dato propuestos para cada campo.
4. Designar uno de los campos como clave primaria.
5. Asignar nombre a la tabla y finalizar.

Si el fichero CSV está abierto en otra aplicación, Access no puede leerlo y muestra un error: hay que cerrarlo primero.

**Limitaciones del asistente:**
- Los nombres de campo se toman tal cual de la cabecera del CSV; puede ser necesario renombrarlos después.
- Los tipos inferidos pueden no ser correctos: el campo booleano suele quedar como texto y hay que corregirlo manualmente en vista de diseño.

## Diferencias entre versiones de Access

| Versión | Ruta para importar fichero de texto |
|---------|--------------------------------------|
| Access 2016 | Datos externos → Fichero de texto |
| Access 2019 | Datos externos → Nuevo origen de datos → Desde un fichero → Texto |

(fuente: TI_01_05b.md). Una vez seleccionado el fichero, el proceso del asistente es idéntico en ambas versiones.

## Relaciones en Access

Las relaciones del [[modelo-relacional]] se implementan visualmente desde **Herramientas de base de datos → Relaciones** (fuente: TI_02_07.md):

1. Si no aparece ninguna tabla, usar el botón **Mostrar tablas** para seleccionarlas.
2. Distribuir las tablas en el espacio visual siguiendo la estructura del modelo.
3. Para crear una relación, arrastrar el campo clave de la tabla del lado 1 al campo equivalente de la tabla del lado N.
4. Marcar la opción **Integridad referencial** (véase [[integridad-referencial]]).
5. Hacer clic en **Crear**. Access muestra la cardinalidad con el símbolo **1** en el lado de la clave primaria y **∞** en el lado N.

Cuando la clave de una tabla es compuesta (p. ej., una tabla intermedia de una relación N:N), hay que indicar explícitamente el sentido de la relación al crearla.

## Consultas

Access ofrece un diseñador visual de consultas que implementa las operaciones del [[algebra-relacional]]: filtra filas (selección), elige columnas (proyección) y combina tablas (join automático por las relaciones definidas). Para una guía completa véase [[consultas-access]]. Cada consulta gráfica tiene un equivalente SQL accesible desde la **vista SQL** (Ctrl+punto); véase [[sql-select]] para la sintaxis completa.

## Formularios

Los formularios son interfaces visuales que muestran un registro por pantalla y permiten navegar, añadir y editar datos de forma más cómoda que la vista de datos directa. Los controles principales son etiquetas, cuadros de texto y **combos** (menús desplegables útiles para [[modelo-relacional|claves foráneas]]). Para relaciones 1:N se usa el **subformulario**, que incrusta un formulario dentro de otro. Para una guía completa véase [[formularios-access]] y [[subformularios-access]].

## Índices

Access permite definir índices sobre los campos de una tabla desde el botón **Índices** en la vista de diseño. Siempre existe el índice de la clave primaria; se pueden añadir índices adicionales para acelerar búsquedas por otros campos. Para una guía completa véase [[indices-access]].

## Informes

Los informes son el objeto de Access para presentar e imprimir datos de forma estructurada. Se crean desde el menú **Crear**, se basan en una consulta como origen de datos y permiten agrupar registros por campos y calcular totales por grupo. Para una guía completa véase [[informes-access]].

## Cuándo usar cada enfoque

| Enfoque | Cuándo usarlo |
|---------|--------------|
| Definición manual (vista de diseño) | Control preciso sobre tipos, nombres de campo y restricciones |
| Importación automática (asistente) | Carga rápida cuando la estructura del CSV es limpia |

## Páginas relacionadas

- [[base-de-datos-tabular]]
- [[formato-csv]]
- [[consultas-access]]
- [[formularios-access]]
- [[subformularios-access]]
- [[ti1-datos-y-tablas]]
- [[ti2-relaciones]]
- [[ti3-consultas]]
- [[ti4-formularios]]
- [[ti5-informes]]
- [[ti6-sql]]
