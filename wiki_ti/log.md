# Log de operaciones

Registro de solo anexar de todas las operaciones sobre la wiki.

---

## 2026-05-19 — Ingestión del Tema 1 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/):
- TI_01_00a.md — Sistemas de numeración (video)
- TI_01_00b.md — ASCII (video)
- TI_01_01.md — Ficheros CSV (video)
- TI_01_02.md — Diferentes formatos de CSV (video)
- TI_01_03.md — Conceptos de base de datos (video)
- TI_01_04.md — Creación de tabla en Access (video)
- TI_01_05.md — Importación de fichero CSV en Access (video)
- TI_01_05b.md — Importación de fichero CSV en Access 2019 (video)
- Tabla ASCII.md — Tabla ASCII completa (referencia)
- Práctica 1. Datos y tablas.md — Enunciado de la práctica
- TI_01.md — Compilación de todos los vídeos del Tema 1

**Páginas creadas:**
- wiki/ti1-datos-y-tablas.md — Resumen del tema
- wiki/sistemas-de-numeracion.md — Bases numéricas y conversiones
- wiki/codigo-ascii.md — Estándar ASCII y representación de texto
- wiki/formato-csv.md — Estructura y variantes del formato CSV
- wiki/base-de-datos-tabular.md — Tabla, registro, campo, clave primaria
- wiki/microsoft-access.md — Crear e importar tablas en Access
- wiki/practica-1-datos-y-tablas.md — Ejercicios de la práctica
- wiki/index.md — Índice de la wiki (creado)
- wiki/log.md — Este fichero (creado)

## 2026-05-19 — Lint y correcciones

**Hallazgos corregidos:**
1. `codigo-ascii.md`: error de rango — los imprimibles son 32–126, no 32–127; 127 (DEL) es control.
2. `formato-csv.md`: ambigüedad en "Estructura interna" — añadida mención a `\r\n` de Windows con referencia a la sección de variaciones.
3. `sistemas-de-numeracion.md`: eliminada afirmación sin fuente ("el octal aparece en permisos Unix").
4. `sistemas-de-numeracion.md`: eliminado enlace débil a `[[base-de-datos-tabular]]` de "Páginas relacionadas".
5. `ti1-datos-y-tablas.md`: fuentes listadas explícitamente (incluido TI_01.md) en vez de "(todos los archivos)".

**Pendiente de vigilancia:**
- "Limpieza de datos" (formato-csv.md): concepto en negrita sin página propia; promover si aparece en fuentes futuras.

## 2026-05-19 — Lint post-Tema 2 y correcciones

**Hallazgos corregidos:**
1. `microsoft-access.md`: añadido TI_02_07.md al campo Fuentes (era citado en el cuerpo pero no en el encabezado).
2. `codigo-ascii.md`: corregida nota de referencia de "(32–127)" a "(32–126)" — consistente con la corrección anterior sobre qué son imprimibles.
3. `microsoft-access.md`: añadido enlace [[ti2-relaciones]] a "Páginas relacionadas" (la página cubre contenido de ambos temas).

**Pendiente de vigilancia:**
- "dominio" (modelo-relacional.md): término en negrita sin página propia; promover si aparece en fuentes futuras.

## 2026-05-19 — Ingestión del Tema 2 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 2 - Relaciones/):
- TI_02_01.md — Modelo Entidad-Relación (video)
- TI_02_02.md — Caso de laboratorio médico (video)
- TI_02_03.md — Modelo relacional (video)
- TI_02_04.md — Conversión ER a Modelo Relacional (video)
- TI_02_05.md — Normalización 1FN y 2FN (video)
- TI_02_06.md — Normalización 3FN y FNBC (video)
- TI_02_07.md — Relaciones en Access (video)
- Modelo Entidad-Relación.md — Apuntes web de referencia
- Práctica 2. Relaciones.md — Enunciado de la práctica

**Páginas creadas:**
- wiki/ti2-relaciones.md — Resumen del tema
- wiki/modelo-entidad-relacion.md — Modelo ER: entidades, relaciones, cardinalidad
- wiki/modelo-relacional.md — Modelo relacional: tablas, claves, tabla intermedia, índices
- wiki/conversion-er-relacional.md — Reglas de conversión por tipo de cardinalidad
- wiki/normalizacion.md — 1FN, 2FN, 3FN, FNBC y desnormalización
- wiki/integridad-referencial.md — Restricciones y comportamientos Restrict/Set null/Cascade
- wiki/practica-2-relaciones.md — Ejercicios de la práctica

**Páginas actualizadas:**
- wiki/microsoft-access.md — Añadida sección "Relaciones en Access" (TI_02_07)
- wiki/base-de-datos-tabular.md — Añadido enlace a [[modelo-relacional]]
- wiki/index.md — Añadida sección Tema 2

## 2026-05-19 — Actualización de rutas de fuentes tras reorganización de Raw/

El usuario reorganizó manualmente la carpeta `Raw/` añadiendo el subdirectorio `Tecnologia de la informacion/`.

**Cambio aplicado en todas las páginas wiki:**
- `Raw/Tema 1 - Datos y tablas/` → `Raw/Tecnologia de la informacion/Tema 1 - Datos y tablas/`
- `Raw/Tema 2 - Relaciones/` → `Raw/Tecnologia de la informacion/Tema 2 - Relaciones/`

**Páginas actualizadas** (15 en total):
base-de-datos-tabular.md, codigo-ascii.md, conversion-er-relacional.md, formato-csv.md,
integridad-referencial.md, log.md, microsoft-access.md, modelo-entidad-relacion.md,
modelo-relacional.md, normalizacion.md, practica-1-datos-y-tablas.md, practica-2-relaciones.md,
sistemas-de-numeracion.md, ti1-datos-y-tablas.md, ti2-relaciones.md

## 2026-05-19 — Ingestión del Tema 3 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 3 - Consultas/):
- TI_03_01.md — Operaciones unarias: selección y proyección (video)
- TI_03_02.md — Operaciones binarias: unión, diferencia, producto cartesiano (video)
- TI_03_03.md — Operaciones derivadas: intersección, cociente, join (video)
- TI_03_04.md — Consultas en Access: básicas, totales, tabla cruzada (video)
- TI_03_05.md — Tipos de consultas: varias tablas, fechas, parámetros, acción (video)
- Práctica 3. Consultas.md — Enunciado de la práctica

**Páginas creadas:**
- wiki/ti3-consultas.md — Resumen del tema
- wiki/algebra-relacional.md — Las 8 operaciones del álgebra relacional
- wiki/consultas-access.md — Consultas de selección, acción y tabla cruzada en Access
- wiki/practica-3-consultas.md — Ejercicios de la práctica

**Páginas actualizadas:**
- wiki/microsoft-access.md — Añadida sección "Consultas" con enlace a consultas-access.md; nuevas fuentes TI_03_04 y TI_03_05
- wiki/index.md — Añadida sección Tema 3

## 2026-05-19 — Lint post-Tema 3

**Sin hallazgos de:** contradicciones, páginas huérfanas, violaciones de formato.

**Hallazgos corregidos:**
1. `microsoft-access.md`: Resumen desactualizado — no mencionaba consultas. Actualizado.
2. `algebra-relacional.md`: conexión selección → SQL (`WHERE`) estaba en TI_03_01.md pero omitida en la wiki. Añadida.
3. `normalizacion.md`: dos afirmaciones sin fuente ("cinco formas normales" y "normalizar en exceso") — añadidas citas TI_02_05.md y TI_02_06.md.
4. `modelo-relacional.md`: tabla de terminología (Columna/Fila y sinónimos) sin fuente — añadida cita TI_02_03.md.
5. `practica-1-datos-y-tablas.md`: sección "Posibles tablas" sin fuente — añadida cita.
6. `practica-2-relaciones.md`: descripción del problema y paso 1 sin fuentes — añadidas citas.
7. `practica-3-consultas.md`: ejercicios Northbrick 2.1, 2.2 y 2.3 sin fuente — añadidas citas.

**Pendiente de vigilancia:**
- "dominio" (modelo-relacional.md): término en negrita sin página propia; promover si aparece en fuentes futuras.
- "limpieza de datos" (formato-csv.md): concepto en negrita sin página propia; promover si aparece en fuentes futuras.

## 2026-05-19 — Ingestión del Tema 4 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 4 - Formularios/):
- TI_04_01.md — Formularios para sistemas de información (video)
- TI_04_02.md — Crear formulario desde cero (video)
- TI_04_03.md — Menú desplegable / combo (video)
- TI_04_04.md — Subformulario (video)
- TI_04_05.md — Subformulario en modo tabular (video)
- Práctica 4. Formularios.md — Enunciado de la práctica

**Páginas creadas:**
- wiki/ti4-formularios.md — Resumen del tema
- wiki/formularios-access.md — Modos, controles, combo y formulario de inicio
- wiki/subformularios-access.md — Subformulario 1:N, vinculación y modo tabular
- wiki/practica-4-formularios.md — Ejercicios de la práctica

**Páginas actualizadas:**
- wiki/microsoft-access.md — Añadida sección "Formularios"; nuevas fuentes TI_04_01–05; resumen ampliado
- wiki/index.md — Añadida sección Tema 4; descripción de microsoft-access actualizada

## 2026-05-19 — Ingestión del Tema 6 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 6 - SQL/):
- TI_06_02.md — Configuración SQL en Access: vista SQL, SELECT/FROM/WHERE/ORDER BY (video)
- TI_06_03.md — Operadores SQL: comparación, BETWEEN, IN, LIKE, AND/OR/NOT, aritmética (video)
- TI_06_04.md — Subconsultas: = y IN con SELECT anidado (video)
- TI_06_04b.md — DISTINCT: eliminar duplicados y mejorar rendimiento (video)
- TI_06_05.md — Funciones de agrupación: COUNT, MIN, MAX, SUM, AVG, AS (video)
- TI_06_06.md — GROUP BY, HAVING y orden de ejecución SQL (video)
- TI_06_07.md — Producto cartesiano en SQL (video)
- TI_06_08.md — JOIN de varias tablas en SQL (video)
- Step 2_ ij Basics.md — Tutorial herramienta ij de Apache Derby (referencia externa)

**Páginas creadas:**
- wiki/ti6-sql.md — Resumen del tema
- wiki/sql-select.md — SELECT/FROM/WHERE/ORDER BY y vista SQL en Access
- wiki/sql-operadores.md — Operadores SQL: comparación, BETWEEN, IN, LIKE, lógicos, aritmética
- wiki/sql-subconsultas.md — Subconsultas (= e IN) y DISTINCT
- wiki/sql-agrupacion.md — COUNT/MIN/MAX/SUM/AVG, AS, GROUP BY, HAVING, orden de ejecución
- wiki/sql-join.md — Producto cartesiano y JOIN de varias tablas en SQL
- wiki/apache-derby.md — Herramienta ij de Apache Derby

**Páginas actualizadas:**
- wiki/algebra-relacional.md — Añadidos enlaces [[sql-select]] y [[sql-join]] en el texto y en Páginas relacionadas; [[ti6-sql]] añadido
- wiki/consultas-access.md — Añadida referencia a [[sql-select]] en la introducción; [[sql-select]], [[sql-agrupacion]], [[sql-join]], [[ti6-sql]] en Páginas relacionadas
- wiki/microsoft-access.md — Sección "Consultas" ampliada con referencia a la vista SQL y [[sql-select]]; [[ti6-sql]] en Páginas relacionadas
- wiki/index.md — Añadida sección Tema 6

## 2026-05-19 — Ingestión del Tema 5 de Tecnología de la Información

**Fuentes ingeridas** (Raw/Tecnologia de la informacion/Tema 5 - Informes/):
- TI_05_01.md — Índices: qué son y tipos (video)
- TI_05_02.md — Creación de índice: qué ocurre al definirlo (video)
- TI_05_03.md — Elección de claves: significativas vs no significativas (video)
- TI_05_04.md — Integridad referencial: mecanismos y comportamientos (video)
- TI_05_06.md — Creación de informe en Access: consulta, agrupación, orientación (video)
- Práctica 5. Informes.md — Enunciado de la práctica

**Páginas creadas:**
- wiki/ti5-informes.md — Resumen del tema
- wiki/indices-access.md — Índices: estructura, tipos, compuestos y creación en Access
- wiki/eleccion-claves.md — Claves significativas vs no significativas; autonumérico
- wiki/informes-access.md — Informes en Access: proceso, agrupación, orientación y tipos
- wiki/practica-5-informes.md — Ejercicios de la práctica

**Páginas actualizadas:**
- wiki/integridad-referencial.md — Añadido TI_05_04.md como fuente; notas de seguridad en Restrict y Cascade; triggers detallados por separado de reglas
- wiki/microsoft-access.md — Añadidas secciones "Índices" e "Informes"; nuevas fuentes TI_05_01, TI_05_02, TI_05_06; resumen ampliado; enlace [[ti5-informes]]
- wiki/index.md — Añadida sección Tema 5; descripción de microsoft-access actualizada

## 2026-05-19 — Lint post-Tema 5

**Sin hallazgos de:** contradicciones entre páginas, páginas huérfanas, violaciones de formato graves.

**Hallazgos corregidos:**
1. `integridad-referencial.md`: última frase de "Activar la integridad referencial en Access" sin fuente — añadida cita TI_02_07.md.
2. `modelo-relacional.md`: sección Índices desactualizada — descripción "propiedades de cada campo" reemplazada por referencia al botón **Índices** y enlace a [[indices-access]].
3. `modelo-relacional.md`: sección "La clave" no enlazaba a [[eleccion-claves]] — añadido enlace al nuevo concepto; [[indices-access]] y [[eleccion-claves]] añadidos a Páginas relacionadas.
4. `ti5-informes.md`: párrafo introductorio sin encabezado `## Introducción`, a diferencia de los temas 1-4 — encabezado añadido.
5. `base-de-datos-tabular.md`: sección "La clave primaria" no enlazaba a [[eleccion-claves]] — añadido enlace al nuevo concepto.

**Pendiente de vigilancia:**
- "dominio" (modelo-relacional.md): término en negrita sin página propia; promover si aparece en fuentes futuras.
- "limpieza de datos" (formato-csv.md): concepto en negrita sin página propia; promover si aparece en fuentes futuras.
- "campo calculado" (informes-access.md, practica-5-informes.md): mencionado pero sin página propia; promover si aparece en fuentes futuras.
- "disparador/trigger" (integridad-referencial.md): mencionado sin página propia; promover si aparece en fuentes futuras.

## 2026-05-20 — Lint general (post-Tema 6)

**Sin hallazgos de:** páginas huérfanas, contradicciones graves, violaciones de formato.

**Hallazgos corregidos:**
1. `sql-join.md`: error de tabla en el primer ejemplo de JOIN — `FROM items, publishers` con `WHERE titles.PubID` es SQL inválido porque `titles` no está en el FROM. Corregido a `FROM titles, publishers`, coherente con el resto de ejemplos de la misma página.
2. `sql-join.md`: afirmación "Los registros sin correspondencia se descartan (inner join)" sin fuente — añadida cita TI_06_08.md.
3. `normalizacion.md`: afirmación "Cuando la clave tiene un solo atributo, 3FN y FNBC son equivalentes" sin fuente — añadida cita TI_02_06.md.
4. `sql-select.md`: atajos de teclado (Ctrl+. / Ctrl+,) y opción de tamaño de fuente del editor SQL sin fuente — añadidas citas TI_06_02.md.

**Pendiente de vigilancia (continúa):**
- "dominio" (modelo-relacional.md): término en negrita sin página propia.
- "limpieza de datos" (formato-csv.md): en negrita sin página propia.
- "campo calculado" (informes-access.md, practica-5-informes.md): sin página propia.
- "disparador/trigger" (integridad-referencial.md): sin página propia.

## 2026-05-19 — Lint post-Tema 4

**Sin hallazgos de:** contradicciones, páginas huérfanas, violaciones de formato.

**Hallazgos corregidos:**
1. `formularios-access.md`, `ti4-formularios.md`, `subformularios-access.md`, `microsoft-access.md`: término "claves foráneas" sin enlace a [[modelo-relacional]] — añadidos 4 enlaces.
2. `modelo-relacional.md`: el término "clave foránea" estaba en las fuentes del Tema 4 (TI_04_03.md) pero ausente en la página del concepto — añadido el término con su fuente; TI_04_03.md incorporado al campo Fuentes de la página.

**Pendiente de vigilancia:**
- "dominio" (modelo-relacional.md): término en negrita sin página propia; promover si aparece en fuentes futuras.
- "limpieza de datos" (formato-csv.md): concepto en negrita sin página propia; promover si aparece en fuentes futuras.
