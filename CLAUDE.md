# Wiki del Asistente IA — Tecnología de la información

Una base de conocimientos académica mantenida por Claude Code.
Basada en el patrón de LLM Wiki de Andrej Karpathy.

## Propósito

Esta wiki es una base de conocimientos estructurada e interconectada
sobre los contenidos de la asignatura Tecnología
de la Información (Universidad de Navarra).
Claude mantiene la wiki. El humano aporta las fuentes, hace preguntas
y guía el análisis.

## Estructura de carpetas
raw/          -- documentos fuente (inmutables -- nunca modificar estos)
wiki/         -- páginas markdown mantenidas por Claude
wiki/index.md -- tabla de contenidos de toda la wiki
wiki/log.md   -- registro de solo anexar de todas las operaciones

## Flujo de trabajo de ingestión

Cuando el usuario agrega una nueva fuente a `raw/` y pide ingerirla:

1. Lee el documento fuente completo
2. Discute los puntos clave con el usuario antes de escribir nada
3. Crea una página de resumen en `wiki/` con el nombre de la fuente
4. Crea o actualiza páginas de conceptos para cada idea o entidad principal
5. Añade enlaces wiki ([[nombre-pagina]]) para conectar páginas relacionadas
6. Actualiza `wiki/index.md` con las nuevas páginas y una descripción breve
7. Añade una entrada a `wiki/log.md` con la fecha, la fuente y qué cambió

Una sola fuente puede tocar 10-15 páginas wiki. Eso es normal.

## Formato de página

Cada página wiki debe seguir esta estructura:

```markdown
# Título de la página

**Resumen**: Una o dos oraciones describiendo esta página.

**Asignatura**: Tecnología de la Información

**Fuentes**: Lista de archivos fuente en raw/ en los que se basa.

**Última actualización**: Fecha de la actualización más reciente.

---

El contenido principal va aquí. Usa encabezados claros y párrafos cortos.

Enlaza conceptos relacionados usando [[wiki-links]] a lo largo del texto.

## Páginas relacionadas

- [[concepto-relacionado-1]]
- [[concepto-relacionado-2]]
```

## Reglas de citación

- Cada afirmación factual debe referenciar su archivo fuente
- Usa el formato (fuente: nombre-fichero.pdf) tras la afirmación
- Si dos fuentes del profesor discrepan, nota la contradicción explícitamente
- Si una afirmación no tiene fuente, márcala como pendiente de verificación

## Lint

Cuando el usuario pida auditar la wiki:

- Verifica contradicciones entre páginas
- Encuentra páginas huérfanas (sin enlaces entrantes desde otras páginas)
- Identifica conceptos mencionados que no tienen página propia
- Marca afirmaciones que pueden estar desactualizadas con fuentes nuevas
- Verifica que todas las páginas sigan el formato definido arriba
- Reporta los hallazgos como lista numerada con correcciones sugeridas

## Reglas

- Nunca modifiques nada en la carpeta `raw/`
- Siempre actualiza `wiki/index.md` y `wiki/log.md` tras cualquier cambio
- Nombres de página en minúsculas con guiones (ej. `prepared-statement.md`)
- Escribe en lenguaje claro y directo, pensado para estudiantes universitarios
- Cuando no estés seguro de cómo categorizar algo, pregunta al usuario

## Comandos rápidos

- `ingiere` — ejecuta el flujo de trabajo de ingestión completo sobre los archivos nuevos que encuentres en `raw/`. Equivale a decir: "I just added a new source to the raw folder. Please read it and update the wiki."