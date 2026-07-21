# Normalización

**Resumen**: La normalización es el proceso de aplicar reglas formales a una base de datos para eliminar redundancias y garantizar coherencia. Las formas normales principales son 1FN, 2FN, 3FN y FNBC.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_05.md, Raw/Tecnologia de la informacion/Tema 2 - Relaciones/TI_02_06.md

**Última actualización**: 2026-05-19

---

## Qué es la normalización

La normalización consiste en aplicar una serie de reglas progresivas a la estructura de una base de datos para garantizar que no generará problemas en su uso. Las ventajas principales son (fuente: TI_02_05.md):
- Facilitar el uso posterior de la base de datos.
- Eliminar redundancias, evitando que la misma información se almacene más de una vez.

Existen cinco formas normales, pero en la práctica se aplican las tres primeras más la Forma Normal de Boyce-Codd (FNBC) (fuente: TI_02_05.md).

## Primera Forma Normal (1FN)

Una tabla está en 1FN si todos los valores de cada atributo son **atómicos**, es decir, indivisibles: no se puede almacenar más de un valor en un mismo campo (fuente: TI_02_05.md).

**Ejemplo de incumplimiento**: un campo "medidas" con el valor `"M3;M4;M6"` (tres valores en un campo).

**Soluciones**:
- Si hay un paso regular, almacenar solo el valor mínimo y máximo.
- Crear una segunda tabla con una fila por cada combinación (artículo, medida).
- Crear tablas propias para tornillos y medidas (solución más completa).

## Dependencia funcional

Un atributo B depende funcionalmente de A si, dado un valor de A, queda determinado de forma única un valor de B (fuente: TI_02_05.md).

**Ejemplo**: el modelo de un camión depende funcionalmente de su matrícula.

B tiene **dependencia funcional total** de A si depende de A como conjunto y no de ningún subconjunto de A.

## Segunda Forma Normal (2FN)

Una tabla está en 2FN si está en 1FN y todos los atributos no clave dependen de forma **total** de la clave, no solo de una parte de ella (fuente: TI_02_05.md).

Solo aplica cuando la clave está compuesta por varios atributos (típico en tablas intermedias de relaciones N:N, véase [[conversion-er-relacional]]).

**Ejemplo de incumplimiento**: tabla con clave compuesta (código_artículo, código_almacén) y un campo "encargado_almacén" que depende solo del código_almacén. Viola la 2FN porque no depende de la clave completa (fuente: TI_02_06.md).

## Dependencia transitiva

Dados A, B y C: si C depende funcionalmente de B, y B depende de A, entonces C tiene una **dependencia transitiva** respecto a A (fuente: TI_02_06.md).

## Tercera Forma Normal (3FN)

Una tabla está en 3FN si cumple la 2FN y no existen atributos secundarios con dependencia transitiva respecto a la clave primaria (fuente: TI_02_06.md).

**Ejemplo de incumplimiento**: tabla de almacenes donde el número_de_busca depende del encargado, y el encargado depende del código_almacén → dependencia transitiva. Solución: separar encargado y número de busca en una tabla propia.

## Forma Normal de Boyce-Codd (FNBC)

Versión más estricta de la 3FN: una tabla está en FNBC si **todas las dependencias funcionales tienen como determinante la clave completa**. Ningún atributo secundario puede determinar a otro (fuente: TI_02_06.md).

Cuando la clave tiene un solo atributo, 3FN y FNBC son equivalentes (fuente: TI_02_06.md).

**Ejemplo de incumplimiento de FNBC (que podría cumplir 3FN)**: tabla con clave compuesta (dirección, ciudad) y campo código_postal. El código postal determina la ciudad, es decir, la ciudad depende de un atributo no clave. Viola la FNBC.

## Desnormalización

En algunos casos se decide intencionalmente **no aplicar** alguna forma normal para mejorar el rendimiento o simplificar consultas. Una tabla no normalizada no es incorrecta: es una decisión de diseño consciente (fuente: TI_02_06.md).

**Inconveniente de normalizar en exceso**: aumenta el número de tablas, haciendo más complejas las consultas (requieren uniones entre tablas) y pudiendo reducir el rendimiento (fuente: TI_02_06.md).

## Páginas relacionadas

- [[modelo-relacional]]
- [[conversion-er-relacional]]
- [[ti2-relaciones]]
