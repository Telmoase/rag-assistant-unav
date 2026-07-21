Estilo de codigo en Java

Resumen: principales convenciones de estilo para escribir codigo Java legible y mantenible, basadas en el documento Java Code Conventions de Sun Microsystems, con especial enfasis en indentacion, comentarios, declaraciones y sentencias de control.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 2 - Variables y sentencias de control/TD_02_03.md

Ultima actualizacion: 2026-06-24

## Por que seguir una guia de estilo

Un programa puede ser sintacticamente correcto de muchas formas distintas. Para que el codigo sea legible y mantenible se sigue una guia de estilo. La referencia utilizada es el documento Java Code Conventions, publicado por Sun Microsystems en 1997, que sigue siendo el estandar de referencia para Java (fuente: TD_02_03.md).

## Indentacion

La unidad de indentacion recomendada es de cuatro espacios. Si se usan tabuladores, deben fijarse exactamente cada 8 espacios, no cada 4 (fuente: TD_02_03.md).

## Tipos de comentarios

Java distingue tres tipos de comentarios (fuente: TD_02_03.md):

| Tipo | Delimitadores | Uso |
|---|---|---|
| Comentario de bloque | `/* ... */` | Describir ficheros, metodos, estructuras de datos o algoritmos; puede ocupar varias lineas |
| Comentario de linea | `// ...` | Explicaciones breves que caben en una sola linea |
| Comentario de documentacion | `/** ... */` | Describir clases, interfaces, constructores, metodos y campos; se extrae a HTML con `javadoc` |

Los comentarios deben aportar informacion que no sea evidente leyendo el codigo directamente, y deben evitarse los que se vuelvan obsoletos facilmente a medida que el codigo cambia (fuente: TD_02_03.md).

## Declaraciones

Se recomienda una [[td2-tipos-y-variables|declaracion de variable]] por linea, en lugar de declarar varias variables en la misma sentencia. Esto facilita anadir un comentario explicativo junto a cada declaracion (fuente: TD_02_03.md):

```java
int level;   // recomendado: una por linea
int size;
```

## Sentencias de control: el caso de if

Las llaves se usan siempre alrededor de los bloques de una sentencia de control, incluso cuando el bloque contiene una sola instruccion. Esto evita errores al anadir nuevas lineas de codigo mas adelante (fuente: TD_02_03.md):

```java
if (condicion) {
    sentencias;
} else {
    sentencias;
}
```

## Paginas relacionadas

- [[td2-tipos-y-variables]]
- [[td2-desarrollo-incremental]]
- [[td2-practica-lenguaje-java]]
