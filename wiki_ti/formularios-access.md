# Formularios en Access

**Resumen**: Los formularios son interfaces visuales de Access para introducir y visualizar datos registro a registro. Permiten trabajar con tablas de forma más cómoda que en la vista de datos directa.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_01.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_02.md, Raw/Tecnologia de la informacion/Tema 4 - Formularios/TI_04_03.md

**Última actualización**: 2026-05-19

---

## Qué es un formulario

Los formularios son interfaces visuales para introducir y visualizar datos, similares a los que se ven en páginas web o aplicaciones Windows. En Access se presentan como ventanas y permiten interactuar con los datos de las tablas de forma más cómoda que trabajando directamente con ellas (fuente: TI_04_01.md).

## Crear un formulario

Desde la pestaña **Crear** hay dos opciones principales (fuente: TI_04_01.md):

| Opción | Descripción |
|--------|-------------|
| **Formulario automático** | Genera un formulario basado en la tabla seleccionada en ese momento |
| **Formulario en blanco** | Crea un formulario vacío; disponible en modo diseño o en modo layout |

El formulario automático es la forma más rápida, aunque puede requerir ajustes posteriores (fuente: TI_04_03.md).

## Modos de trabajo

Un formulario tiene tres modos (fuente: TI_04_01.md):

| Modo | Uso |
|------|-----|
| **Diseño** | Modificar la estructura y los controles del formulario |
| **Layout** | Ajustar el diseño viendo los datos reales simultáneamente |
| **Vista** | Resultado final que verá el usuario |

## Vincular un formulario a una tabla

En las propiedades del formulario, el campo **Origen de datos** indica qué tabla o consulta alimenta el formulario. Al vincular una tabla, el formulario muestra un registro por pantalla y permite navegar entre registros con la barra de navegación inferior (fuente: TI_04_01.md).

Si se quiere eliminar la barra de navegación, se desactiva la opción **Botones de navegación** en las propiedades de formato (fuente: TI_04_01.md).

## Controles disponibles

Los tipos de controles accesibles desde el menú de diseño son (fuente: TI_04_03.md):

- **Etiqueta**: texto estático descriptivo.
- **Cuadro de texto**: muestra y edita el valor de un campo. Cada cuadro de texto tiene dos elementos: la caja de datos y su etiqueta asociada. En las propiedades se configura el **Origen del control** (el campo de la tabla que mostrará) (fuente: TI_04_02.md).
- **Botón**: ejecuta una acción.
- **Pestaña**: organiza controles en secciones.
- **Combo** (menú desplegable): véase sección dedicada a continuación.
- **Lista**: muestra todos los valores posibles de una lista.

## Combo (menú desplegable)

El combo permite seleccionar un valor de una lista en lugar de escribirlo manualmente. Es especialmente útil para campos que hacen referencia a otra tabla ([[modelo-relacional|claves foráneas]]), ya que muestra valores legibles en lugar de códigos numéricos (fuente: TI_04_03.md).

### Proceso de creación con el asistente

1. Seleccionar el control combo y dibujarlo en el formulario (fuente: TI_04_03.md).
2. Indicar de dónde vienen los valores: otra tabla, lista fija o consulta.
3. Elegir la tabla de origen y los campos a mostrar en el desplegable.
4. Opcionalmente, ordenar la lista por alguno de los campos.
5. Ajustar la anchura de cada columna. La columna de clave primaria suele ocultarse (anchura = 0) para mostrar solo el nombre legible.
6. Indicar en qué campo del formulario se guardará el valor seleccionado.
7. Asignar un título a la etiqueta del combo.

### Propiedades del combo

| Propiedad | Descripción |
|-----------|-------------|
| **Origen del control** | Campo de la tabla donde se guarda el valor seleccionado |
| **Origen de la fila** | Consulta SQL que recupera los valores del desplegable |
| **Anchura de columnas** | Controla qué columnas son visibles; anchura 0 = columna oculta |

Para mostrar el nombre en lugar del código, la columna del nombre debe tener anchura > 0 y la del código anchura 0 (fuente: TI_04_03.md).

## Formulario de presentación (pantalla de inicio)

Un formulario sin tabla vinculada puede usarse como pantalla de inicio de la aplicación, con etiquetas estáticas como el título. Para que se abra automáticamente al iniciar la base de datos se configura en **Archivo → Opciones → Base de datos actual**, indicando cuál es el formulario de inicio (fuente: TI_04_01.md).

## Visualización de ventanas

Por defecto Access muestra objetos en pestañas. Se puede cambiar a ventanas solapadas (visibles simultáneamente) en **Archivo → Opciones → Base de datos actual**. El cambio requiere cerrar y volver a abrir la base de datos (fuente: TI_04_03.md).

## Páginas relacionadas

- [[subformularios-access]]
- [[consultas-access]]
- [[microsoft-access]]
- [[integridad-referencial]]
- [[ti4-formularios]]
