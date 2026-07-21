# Subformularios en Access

**Resumen**: Un subformulario es un formulario incrustado dentro de otro. Se usa para mostrar simultáneamente el registro principal (lado 1 de una relación) y todos sus registros relacionados (lado N).

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_04.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_05.md

**Última actualización**: 2026-05-19

---

## Qué es un subformulario

Un subformulario es un formulario incluido dentro de otro formulario. Se usa cuando existe una [[conversion-er-relacional|relación 1:N]] entre dos tablas y se quiere mostrar simultáneamente los datos del registro principal (lado 1) y todos sus registros relacionados (lado N) (fuente: TI_04_04.md).

Ejemplo: datos de un camión en la zona principal + lista de sus albaranes en el subformulario.

## Estructura del formulario con subformulario

| Zona | Muestra | Tabla |
|------|---------|-------|
| **Cabecera / zona principal** | Datos del registro del lado 1 | Ej.: tabla camiones |
| **Subformulario** | Lista de registros del lado N | Ej.: tabla albaranes |

## Crear un formulario con subformulario automáticamente

Desde la pestaña **Crear**, seleccionando la tabla del lado 1 y pulsando **Formulario**, Access detecta automáticamente la relación 1:N y genera el formulario con el subformulario incluido (fuente: TI_04_04.md).

## Navegación

El formulario con subformulario tiene **dos barras de navegación independientes** (fuente: TI_04_04.md):

- La barra del **subformulario** navega entre los registros del lado N del registro actual.
- La barra del **formulario principal** navega entre los registros del lado 1.

Al cambiar de registro en el formulario principal, el subformulario se actualiza automáticamente mostrando solo los registros relacionados.

## Propiedades de vinculación

En modo diseño, las propiedades de datos del subformulario muestran (fuente: TI_04_04.md):

| Propiedad | Descripción |
|-----------|-------------|
| **Origen de datos** | Tabla o consulta que alimenta el subformulario |
| **Campo de unión maestro** | Campo de la tabla principal que establece el vínculo (lado 1) |
| **Campo de unión secundario** | Campo de la tabla del subformulario que corresponde al anterior (lado N) |

Esta vinculación garantiza que el subformulario muestre solo los registros relacionados con el registro actual del formulario principal.

## Modos de presentación del subformulario

### Hoja de datos (datasheet)

Modo por defecto cuando Access genera el subformulario automáticamente. Muestra los registros como una tabla simple (fuente: TI_04_05.md).

### Modo tabular

Formulario creado manualmente con el asistente. Muestra cada registro en una fila con las cabeceras de columna en la parte superior. Permite mayor personalización visual (fuente: TI_04_05.md).

## Crear y usar un subformulario tabular

**Paso 1 — Crear el formulario tabular** con el asistente (fuente: TI_04_05.md):

1. Seleccionar la tabla del lado N como origen de datos.
2. Añadir los campos deseados (normalmente todos excepto la [[modelo-relacional|clave foránea]] del lado 1, que ya aparece en el formulario principal).
3. Elegir la distribución **tabular**.
4. Finalizar. Se puede ajustar el alto de las filas para mayor compacidad.

**Paso 2 — Sustituir el subformulario automático** en el formulario principal (fuente: TI_04_05.md):

1. Abrir el formulario principal en modo diseño.
2. Seleccionar el subformulario existente.
3. En sus propiedades de datos, cambiar el **Origen** para que apunte al formulario tabular recién creado en lugar de a la tabla directa.
4. Guardar.

**Paso 3 — Ajustar el tamaño** (fuente: TI_04_05.md):

1. Quitar el layout automático del control para poder redimensionarlo libremente.
2. Ampliar el área del subformulario arrastrando sus bordes.
3. En modo layout, ajustar el ancho de cada columna.

## Páginas relacionadas

- [[formularios-access]]
- [[conversion-er-relacional]]
- [[modelo-relacional]]
- [[microsoft-access]]
- [[ti4-formularios]]
