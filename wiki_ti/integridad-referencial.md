# Integridad referencial

**Resumen**: La integridad referencial garantiza la coherencia de los datos entre tablas relacionadas. Define restricciones sobre los valores permitidos y el comportamiento al borrar o modificar registros con dependencias.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_07.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Modelo Entidad-Relación.md, Raw/Tecnologia de la informacion/Tema 5 - Informes/TI_05_04.md

**Última actualización**: 2026-05-19

---

## Qué es la integridad referencial

La integridad referencial es el mecanismo que garantiza la coherencia de los datos entre tablas relacionadas. Asegura que no puedan existir registros que violen una relación: por ejemplo, no puede haber una prueba asignada a un técnico que no exista en la tabla de técnicos (fuente: TI_02_07.md).

## Tipos de restricciones

Las restricciones de integridad pueden actuar sobre (fuente: Modelo Entidad-Relación.md):

- **Tipo de dato**: el valor debe pertenecer al dominio definido para el campo.
- **Aceptación de nulos**: si el campo puede quedar vacío o no.
- **Valores únicos**: si no pueden repetirse valores en ese campo.
- **Integridad referencial entre tablas**: que el valor exista en la tabla referenciada.
- **Reglas y expresiones**: permiten validar que el valor cumple una condición compleja, como verificar el dígito de control de un pasaporte o comprobar que un número de tarjeta de crédito es válido (fuente: TI_05_04.md).
- **Disparadores** (*triggers*): funciones que se ejecutan automáticamente al introducir, modificar o borrar un valor, y que pueden realizar comprobaciones o acciones adicionales (fuente: TI_05_04.md).

## Comportamiento al borrar o modificar

Cuando se borra o modifica un registro que tiene registros relacionados en otra tabla, hay tres comportamientos posibles (fuente: Modelo Entidad-Relación.md):

| Comportamiento | Descripción |
|---------------|-------------|
| **Restringir** (*Restrict*) | Impide el borrado o modificación si existen registros relacionados. Es la opción más segura (fuente: TI_05_04.md) |
| **Poner nulo** (*Set null*) | Establece a nulo el campo relacionado en los registros dependientes. Solo es posible si esos campos permiten nulos (fuente: TI_05_04.md) |
| **En cascada** (*Cascade*) | Aplica automáticamente el mismo cambio a todos los registros relacionados. Es la opción más peligrosa; debe usarse solo cuando se está completamente seguro de que es el comportamiento deseado (fuente: TI_05_04.md) |

## Activar la integridad referencial en Access

Al crear una relación en el panel de relaciones de [[microsoft-access|Access]], se marca la opción **Integridad referencial** antes de hacer clic en Crear. Access muestra entonces la cardinalidad con el símbolo **1** en el lado de la clave primaria y el símbolo **∞** en el lado N (fuente: TI_02_07.md).

Si la clave de una tabla es compuesta (como en Detalle Petición), hay que indicar explícitamente el sentido de la relación al crearla (fuente: TI_02_07.md).

## Páginas relacionadas

- [[modelo-relacional]]
- [[microsoft-access]]
- [[ti2-relaciones]]
