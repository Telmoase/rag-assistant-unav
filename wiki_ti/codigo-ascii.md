# Código ASCII

**Resumen**: El estándar ASCII asigna un número entero a cada carácter de texto, permitiendo almacenarlo en ficheros binarios. Es la base de la representación de texto en informática.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/TI_01_00b.md, Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/Tabla ASCII.md

**Última actualización**: 2026-05-19

---

## Texto en binario

Los ficheros almacenan información como secuencias de 0s y 1s. Para guardar texto, cada carácter se mapea a un número entero. La unidad básica es el **byte**: 8 bits agrupados, que representa 256 valores distintos (0–255) (fuente: TI_01_00b.md).

## El estándar ASCII

**ASCII** (*American Standard Code for Information Interchange*) define la correspondencia entre números enteros y caracteres (fuente: TI_01_00b.md):

- Ocupa **7 bits**: cubre los valores 0–127 (128 caracteres en total).
- Los valores 0–31 y 127 son **caracteres de control** no imprimibles (salto de línea, tabulador, DEL, etc.) (fuente: Tabla ASCII.md).
- Los valores 32–126 son **caracteres imprimibles** (letras, dígitos, signos de puntuación).
- Los valores 128–255 se reservan para **caracteres extendidos** (ñ, á, ü, etc.) (fuente: TI_01_00b.md).

## Rangos clave de la tabla ASCII

| Rango decimal | Contenido |
|---------------|-----------|
| 0–31 | Caracteres de control (no imprimibles) |
| 32 | Espacio |
| 48–57 | Dígitos 0–9 |
| 65–90 | Letras mayúsculas A–Z |
| 97–122 | Letras minúsculas a–z |
| 127 | DEL (control) |

Ejemplo: la letra `D` = decimal 68 = hexadecimal 44 = binario 01000100 (fuente: TI_01_00b.md).

Para la tabla completa de caracteres imprimibles (32–126) véase Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/Tabla ASCII.md.

## Relación entre mayúsculas y minúsculas

Las letras mayúsculas y sus minúsculas correspondientes difieren en exactamente **32 unidades decimales** (20 en hexadecimal). Esto permite convertir entre ellas con una simple suma o resta sobre el código del carácter (fuente: TI_01_00b.md).

## Representación hexadecimal del texto

En la práctica, el contenido de un fichero de texto se visualiza en **hexadecimal** en lugar de binario: resulta más compacto y cada byte ocupa siempre **dos dígitos hex** (16×16 = 256 combinaciones) (fuente: TI_01_00b.md). Los editores hexadecimales muestran esta correspondencia directamente.

## Páginas relacionadas

- [[sistemas-de-numeracion]]
- [[formato-csv]]
- [[ti1-datos-y-tablas]]
