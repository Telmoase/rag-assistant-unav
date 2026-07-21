# Informes en Access

**Resumen**: Los informes son el objeto de Access para presentar e imprimir datos de forma estructurada, con soporte para agrupación de registros, cabeceras de grupo y campos calculados.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_06.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/Práctica 5. Informes.md

**Última actualización**: 2026-05-19

---

## Qué es un informe

El objeto **informe** de Access sirve para mostrar información de forma elegante y clara, casi siempre pensada para imprimir. Es el mecanismo para generar listados y reportes a partir de los datos de la base de datos (fuente: Práctica 5. Informes.md).

## Proceso de creación

El primer paso es tener preparada una **consulta** con los datos que se quieren mostrar; el informe toma esa consulta como origen de datos (fuente: TI_05_06.md).

Desde el menú **Crear** se accede a la opción de informe. En las propiedades del informe se configura el **origen de datos**, seleccionando la consulta preparada previamente.

## Añadir campos

Se insertan los campos que se quieren mostrar. Para cada campo se configura el cuadro de datos y su etiqueta. Las **etiquetas de cabecera** se colocan en la sección de cabecera del informe, no en el área de detalle, para que aparezcan una sola vez en la parte superior (fuente: TI_05_06.md).

## Agrupar registros

Para evitar que un valor se repita en cada fila se configura una **agrupación**. En el diseño del informe se define el campo de agrupación; el campo agrupador se mueve a la cabecera del grupo, de forma que aparece una vez por grupo y debajo se listan los registros correspondientes (fuente: TI_05_06.md).

Ejemplo: agrupar albaranes por gasolinera — el nombre de la gasolinera aparece solo una vez por grupo y debajo se listan sus albaranes.

## Orientación de impresión

En las propiedades de formato del informe se puede configurar la orientación: **vertical** (por defecto) u **horizontal**, útil cuando el informe tiene muchas columnas (fuente: TI_05_06.md).

## Tipos de informes

Los ejercicios de la [[practica-5-informes|práctica 5]] ilustran los principales patrones:

- **Listado simple**: tabla directa de una entidad sin agrupación (compañías, camiones).
- **Agrupado**: registros agrupados por una categoría (gasolineras por compañía).
- **Con totales**: subtotal por grupo y total general (albaranes por gasolinera con importe total).
- **Con agrupación por fecha**: albaranes por camión organizados por mes.
- **Con campo calculado**: consumo en litros calculado a partir del importe y el precio del gasoil.

## Páginas relacionadas

- [[consultas-access]]
- [[practica-5-informes]]
- [[microsoft-access]]
- [[ti5-informes]]
