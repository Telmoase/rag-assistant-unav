# Modelo Entidad-Relación

**Resumen**: El modelo Entidad-Relación (ER) es el principal modelo de diseño conceptual de bases de datos. Define entidades, relaciones entre ellas y la cardinalidad de esas relaciones.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_01.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_02.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Modelo Entidad-Relación.md

**Última actualización**: 2026-05-19

---

## Qué es el modelo ER

El modelo Entidad-Relación es el modelo de diseño de bases de datos más utilizado. Permite describir la realidad a modelizar usando dos elementos principales: **entidades** y **relaciones** (fuente: TI_02_01.md).

## Entidades

Una entidad es cualquier clase de objeto de la realidad que se quiere modelizar: puede ser concreta o abstracta, natural o artificial, física o virtual. En la práctica, las entidades suelen ser **sustantivos**: persona, departamento, estudiante, grado (fuente: TI_02_01.md).

Se representan con un **rectángulo** con el nombre de la entidad escrito dentro.

## Relaciones

Una relación es la asociación entre dos entidades. Suelen ser **verbos**: "pertenece", "matricula", "tiene". Se representan con un **rombo** con el tipo de relación escrito dentro (fuente: TI_02_01.md).

Las relaciones pueden transformarse en entidades cuando es necesario añadirles atributos propios o cuando agrupan varias cosas (fuente: TI_02_01.md).

## Cardinalidad

La cardinalidad indica cuántas instancias de una entidad se asocian con cuántas instancias de otra (fuente: TI_02_01.md):

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **1:1** | Cada instancia de A con exactamente una de B, y viceversa | Grado ↔ Plan de estudios |
| **1:N** | Una instancia de A con múltiples de B | Departamento → Asignaturas |
| **N:N** | Múltiples de A con múltiples de B | Estudiante ↔ Asignatura |
| **C** (opcional) | Cero o uno: la relación puede no existir | Estudiante → Asesor (puede no tenerlo) |

Ejemplos del dominio de matrícula (fuente: TI_02_01.md):
- Estudiante - Grado: **1:N** (un estudiante pertenece a un grado; un grado tiene N estudiantes)
- Estudiante - Asignatura: **N:N** (un estudiante en varias asignaturas; una asignatura con varios estudiantes)
- Estudiante - Asesor: **C:N** (un estudiante tiene cero o un asesor; un asesor tiene N estudiantes)

## Caso práctico: laboratorio médico

El modelo se construye leyendo el enunciado frase a frase e identificando entidades y relaciones (fuente: TI_02_02.md):

| Frase | Entidad identificada |
|-------|---------------------|
| "Un laboratorio realiza pruebas médicas" | **Prueba** |
| "Los médicos solicitan pruebas para sus pacientes" | **Médico**, **Paciente** |
| "Los médicos realizan peticiones de pruebas" | **Petición** (la relación se convierte en entidad porque agrupa varias pruebas) |
| "La petición la envía la enfermera al laboratorio" | **Enfermera** |
| "La prueba la realiza siempre el mismo autoanalizador" | **Autoanalizador** |
| "Una prueba puede prepararla cualquier técnico" | **Técnico** |

**Entidades finales**: Prueba, Médico, Petición, Paciente, Enfermera, Autoanalizador, Técnico.

**Lección clave**: cuando una relación agrupa varias cosas o tiene atributos propios, debe convertirse en entidad. En el ejemplo, la "solicitud" inicial entre Médico y Prueba pasó a ser la entidad Petición (fuente: TI_02_02.md).

## Del ER al modelo relacional

Una vez definido el diagrama ER, se convierte al [[modelo-relacional]] siguiendo las reglas de [[conversion-er-relacional]].

## Páginas relacionadas

- [[modelo-relacional]]
- [[conversion-er-relacional]]
- [[ti2-relaciones]]
