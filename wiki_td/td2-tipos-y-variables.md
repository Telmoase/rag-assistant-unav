Tipos de variables y declaraciones en Java

Resumen: descripcion de los ocho tipos primitivos de Java, sus rangos y tamanos en memoria, junto con la sintaxis de declaracion de variables simples y arrays.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 2 - Variables y sentencias de control/TD_02_01.md, Tecnologia Digital/Tema 2 - Variables y sentencias de control/TD_02_02.md

Ultima actualizacion: 2026-06-24

## Los ocho tipos primitivos de Java

Java tiene ocho tipos de variables basicos, agrupados en cuatro categorias (fuente: TD_02_01.md):

| Categoria | Tipo | Tamano | Rango / Descripcion |
|---|---|---|---|
| Booleano | `boolean` | 1 byte | Solo `true` o `false` |
| Caracter | `char` | 2 bytes | Un simbolo Unicode (incluye ASCII) |
| Entero | `byte` | 1 byte | -128 a 127 |
| Entero | `short` | 2 bytes | -32.768 a 32.767 |
| Entero | `int` | 4 bytes | -2.147.483.648 a 2.147.483.647 |
| Entero | `long` | 8 bytes | -9,22 * 10^18 a 9,22 * 10^18 |
| Real | `float` | 4 bytes | ~6-7 cifras decimales, rango aprox. +-3,4 * 10^38 |
| Real | `double` | 8 bytes | ~15 cifras decimales, rango aprox. +-1,8 * 10^308 |

La existencia de varios tipos enteros y varios tipos reales responde a un compromiso entre el espacio en memoria y el rango de valores necesario. Elegir el tipo mas pequeno que cubra el rango requerido permite un uso mas eficiente de la memoria (fuente: TD_02_01.md).

Ademas de estos ocho tipos primitivos, en Java se pueden crear tipos propios mediante clases y usar tipos definidos en las librerias del lenguaje (fuente: TD_02_01.md).

## Declaracion de una variable simple

Para definir una variable se indica primero el tipo y despues el nombre, terminando con punto y coma. Si no se le asigna un valor explicitamente, queda inicializada a 0 (fuente: TD_02_02.md):

```java
int x;
```

Se puede asignar un valor en la misma sentencia de declaracion:

```java
int y = 5;
```

## Declaracion de un array

Para declarar un array se anaden corchetes despues del tipo. Sin inicializacion, el array queda a `null` (fuente: TD_02_02.md):

```java
int [] vector;
```

Para crear el array con un tamano concreto se usa `new`. Los elementos quedan inicializados a 0:

```java
vector = new int[10];
```

Para acceder a un elemento se usa su indice entre corchetes, empezando desde 0. Por ejemplo, `vector[0]` accede al primer elemento (fuente: TD_02_02.md).

Tambien se puede declarar e inicializar un array con valores concretos directamente:

```java
double [] v = {1.0, 2.65, 3.1};
```

## Sintaxis alternativa para declarar arrays

Los corchetes pueden colocarse despues del tipo o despues del nombre de la variable. Ambas formas son equivalentes, pero la primera es la recomendada por claridad (fuente: TD_02_02.md):

```java
int [] vector;   // forma recomendada
int vector [];   // equivalente, menos habitual
```

## Paginas relacionadas

- [[td1-compilacion-java]]
- [[td2-estilo-de-codigo-java]]
- [[td1-programas-basicos-java]]
- [[td3-objetos-y-referencias]]
