# Práctica 2: Relaciones

**Resumen**: Ejercicios prácticos del Tema 2 sobre diseño de bases de datos relacionales: modelo ER, conversión al modelo relacional, implementación en Access con relaciones e integridad referencial.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/Práctica 2. Relaciones.md

**Última actualización**: 2026-05-19

---

## Ejercicio 1: Sistema de información de consumo de gasoil

Diseñar e implementar una base de datos para controlar el consumo de gasoil de los camiones de una empresa de transporte (fuente: Práctica 2. Relaciones.md).

### Descripción del problema

Cuando un transportista reposta en una gasolinera, rellena un albarán con: nombre de gasolinera, matrícula del camión, fecha, importe del consumo y número del cheque de pago. El departamento de contabilidad introduce estos albaranes en la base de datos (fuente: Práctica 2. Relaciones.md).

Los datos de prueba son los de `AlbaranesDatos.csv` (utilizado también en [[practica-1-datos-y-tablas|Práctica 1]]).

### Pasos

1. Diseñar el [[modelo-entidad-relacion|modelo ER]] y la [[conversion-er-relacional|conversión al modelo relacional]] (fuente: Práctica 2. Relaciones.md).
2. Crear una base de datos Access en blanco.
3. Crear las tablas con sus campos y claves principales.
4. Crear las relaciones con [[integridad-referencial]]: no debe permitirse un código de camión que no esté en CAMIONES ni un código de gasolinera que no esté en GASOLINERAS.
5. Introducir datos de prueba manualmente.
6. Borrarlos e importar los del fichero CSV.
7. Añadir una tabla COMPANIA (nombre, precio actual del gasoil, dirección de sede) con sus relaciones. Registros de ejemplo: Petronor, Campsa, Cepsa, Repsol, Avanti.

## Ejercicio 2: Inicio del trabajo de la asignatura

1. Describir en texto un problema a solucionar con un sistema de información, similar al Ejercicio 1 o al caso del laboratorio médico.
2. Crear las tablas, relaciones e insertar algunos datos (fuente: Práctica 2. Relaciones.md).

## Páginas relacionadas

- [[modelo-entidad-relacion]]
- [[modelo-relacional]]
- [[conversion-er-relacional]]
- [[integridad-referencial]]
- [[microsoft-access]]
- [[practica-1-datos-y-tablas]]
- [[ti2-relaciones]]
