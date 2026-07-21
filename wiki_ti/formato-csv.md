# Formato CSV

**Resumen**: CSV (Comma-Separated Values) es un formato de fichero de texto plano para almacenar datos tabulares. No existe un estándar único: los separadores y los fines de línea varían según la aplicación.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_01.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_02.md

**Última actualización**: 2026-05-19

---

## Qué es un fichero CSV

CSV (*Comma-Separated Values*) es un fichero de texto plano donde cada línea representa un **registro** y los campos de cada registro se separan por un delimitador (habitualmente la coma). La primera línea suele ser la **cabecera** con los nombres de los campos (fuente: TI_01_01.md).

Ejemplo (base de datos LEGO, fichero de colores):
```
id, name, rgb, is_trans
0, Black, 05131D, f
1, Blue, 0055BF, f
```
- Línea 1: cabecera (4 campos)
- Líneas 2–136: 135 registros de colores

## Abrir un CSV con Excel

Excel puede abrir ficheros CSV, pero a veces los muestra como texto sin separar en columnas. Para dividirlos correctamente se usa **Texto a columnas** (menú Datos) (fuente: TI_01_01.md):

1. Seleccionar formato **delimitado** (no anchura fija)
2. Indicar el delimitador (coma u otro)
3. Opcionalmente asignar un tipo de dato a cada columna

## Estructura interna del fichero

Cada registro termina con un **carácter de salto de línea** (`\n`, o `\r\n` en ficheros generados en Windows — véase sección Variaciones del formato). Es habitual que el fichero tenga una línea vacía al final — resultado de un salto de línea tras el último registro — lo que puede hacer que algunos programas cuenten un registro más de los esperados (fuente: TI_01_01.md).

Los editores de texto avanzados (como Notepad++) permiten mostrar caracteres no imprimibles (saltos de línea, tabuladores, retornos de carro), lo que es útil para **limpieza de datos** previa al procesamiento.

## Variaciones del formato

El CSV no tiene un estándar único ni obligatorio (fuente: TI_01_02.md):

**Separador de campos:**
| Separador | Cuándo se usa |
|-----------|--------------|
| Coma (`,`) | El más habitual en general |
| Punto y coma (`;`) | Excel en configuraciones regionales donde la coma es separador decimal |

**Fin de línea:**
| Secuencia | Sistema |
|-----------|---------|
| `\n` (*line feed*) | Unix / Linux / Mac |
| `\r\n` (*carriage return + line feed*) | Windows |

## Implicación práctica

Antes de procesar un CSV con código, conviene inspeccionarlo con un editor de texto para identificar (fuente: TI_01_02.md):
- Qué carácter se usa como separador
- Qué secuencia marca el fin de cada registro
- Si hay caracteres inesperados que requieran limpieza

No asumir que el separador siempre es coma ni que el fin de línea es siempre el mismo.

## Páginas relacionadas

- [[base-de-datos-tabular]]
- [[microsoft-access]]
- [[codigo-ascii]]
- [[ti1-datos-y-tablas]]
