# Tema 2: Relaciones

**Resumen**: Resumen del Tema 2 de Tecnología de la Información. Cubre el diseño de bases de datos mediante el modelo Entidad-Relación, su conversión al modelo relacional, la normalización y la integridad referencial.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_01.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_02.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_03.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_04.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_05.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_06.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_07.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Modelo Entidad-Relación.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Práctica 2. Relaciones.md

**Última actualización**: 2026-05-19

---

## Introducción

El Tema 2 enseña a diseñar la estructura de una base de datos desde cero. El proceso tiene tres etapas: modelado conceptual (ER), traducción al modelo relacional e implementación en Access con relaciones e integridad referencial.

## Bloque 1: Modelo Entidad-Relación

El [[modelo-entidad-relacion|modelo ER]] es el punto de partida del diseño. Se identifican las **entidades** (sustantivos de la realidad, representadas por rectángulos) y las **relaciones** entre ellas (verbos, representadas por rombos). La **cardinalidad** (1:1, 1:N, N:N, C) determina cuántas instancias de cada entidad participan en cada relación.

El proceso se practica con el caso del laboratorio médico: 7 entidades (Prueba, Médico, Petición, Paciente, Enfermera, Autoanalizador, Técnico) construidas leyendo el enunciado frase a frase.

## Bloque 2: Modelo relacional e implementación

El [[modelo-relacional]] formaliza la estructura como tablas. Las reglas de [[conversion-er-relacional|conversión ER → Relacional]] varían según la cardinalidad:

- 1:1 → 1 tabla
- 1:N → 2 tablas (clave del lado 1 en el lado N)
- C:C y N:N → siempre 3 tablas (tabla intermedia)

En [[microsoft-access|Access]] las relaciones se crean en el panel **Herramientas de base de datos → Relaciones**, arrastrando campos y activando la [[integridad-referencial]].

## Bloque 3: Normalización

La [[normalizacion|normalización]] verifica que la estructura no genera redundancias ni anomalías:

- **1FN**: valores atómicos (un solo valor por campo)
- **2FN**: dependencia funcional total de la clave (solo aplica a claves compuestas)
- **3FN**: sin dependencias transitivas
- **FNBC**: ningún atributo secundario puede determinar a otro

## Práctica

Los conceptos se aplican en [[practica-2-relaciones|Práctica 2]]: diseño completo de un sistema de información para control de consumo de gasoil (camiones, gasolineras, compañías) e inicio del trabajo de la asignatura.

## Páginas relacionadas

- [[modelo-entidad-relacion]]
- [[modelo-relacional]]
- [[conversion-er-relacional]]
- [[normalizacion]]
- [[integridad-referencial]]
- [[microsoft-access]]
- [[practica-2-relaciones]]
