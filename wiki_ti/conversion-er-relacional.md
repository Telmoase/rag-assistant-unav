# Conversión del modelo ER al modelo relacional

**Resumen**: Reglas sistemáticas para traducir un diagrama Entidad-Relación a tablas del modelo relacional, según el tipo de cardinalidad de cada relación.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_04.md

**Última actualización**: 2026-05-19

---

## Dos enfoques de diseño

Hay dos enfoques para diseñar una base de datos relacional (fuente: TI_02_04.md):
- **Directo**: diseñar las tablas directamente en el modelo relacional.
- **ER → Relacional**: diseñar primero el [[modelo-entidad-relacion|diagrama ER]] y después convertirlo siguiendo las reglas de cardinalidad. Con esta sistemática la conversión es directa y clara.

## Reglas por tipo de cardinalidad

### Relación 1:1

Una sola tabla recoge los campos de ambas entidades. La clave puede ser la de cualquiera de las dos (fuente: TI_02_04.md).

**Ejemplo**: un chofer conduce siempre el mismo camión → tabla única con datos de ambos, usando el DNI del chofer como clave.

### Relación C:1 (cero o uno : uno)

Dos soluciones válidas (fuente: TI_02_04.md):

| Solución | Descripción | Inconveniente |
|----------|-------------|--------------|
| Una tabla | Clave de la entidad opcional como campo; registros sin relación quedan a nulo | Introduce nulos |
| Dos tablas | En la tabla del lado opcional se incluye la clave de la otra | Sin nulos; solución preferible |

**Ejemplo**: un alumno puede tener o no un ordenador, pero un ordenador siempre pertenece a un alumno → tabla ORDENADORES incluye el código del alumno.

### Relación C:C (cero o uno : cero o uno)

Tres tablas. La solución de dos tablas no vale porque deja elementos sin relacionar fuera (fuente: TI_02_04.md):
1. Tabla para la primera entidad.
2. Tabla para la segunda entidad.
3. Tabla intermedia con solo los pares que sí están relacionados.

**Ejemplo**: profesores y despachos (no todos los profesores tienen despacho ni todos los despachos están ocupados).

### Relación 1:N

Dos tablas. En la tabla del lado N se incluye como campo la clave del lado 1 (fuente: TI_02_04.md).

**Ejemplo**: trabajadores y categorías → tabla TRABAJADORES incluye el código de categoría. Varios trabajadores comparten la misma categoría; la información de cada categoría se almacena una sola vez.

### Relación C:N

Similar a 1:N, pero los elementos del lado 1 pueden no tener registros en el lado N. Puede resolverse con dos tablas (con posibles nulos) o con tres (como C:C) (fuente: TI_02_04.md).

### Relación N:N

Siempre tres tablas (fuente: TI_02_04.md):
1. Tabla para la primera entidad.
2. Tabla para la segunda entidad.
3. Tabla intermedia cuya clave es la **combinación de las claves de ambas entidades**. Puede tener campos adicionales si la relación tiene atributos propios.

**Ejemplo**: proveedores y materias primas. La tabla intermedia recoge (código_proveedor, código_materia_prima) y puede incluir el precio, que varía según la combinación.

## Tabla resumen

| Cardinalidad | Nº de tablas | Implementación |
|-------------|-------------|----------------|
| 1:1 | 1 | Campos de ambas entidades en una tabla |
| C:1 | 1 o 2 | Clave opcional como campo (nulos) o tabla separada (sin nulos) |
| C:C | 3 | Tabla intermedia solo con los pares relacionados |
| 1:N | 2 | Clave del lado 1 en la tabla del lado N |
| C:N | 2 o 3 | Como 1:N, con opción de tabla intermedia |
| N:N | 3 | Tabla intermedia con clave compuesta |

## Páginas relacionadas

- [[modelo-entidad-relacion]]
- [[modelo-relacional]]
- [[normalizacion]]
- [[ti2-relaciones]]
