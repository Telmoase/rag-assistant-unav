Packages en Java

Resumen: explica para que sirven los packages, como declarar que una clase pertenece a uno, como importar clases de packages externos, y las reglas principales sobre packages segun la documentacion de Oracle.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_04.md

Ultima actualizacion: 2026-06-24

## Por que existen los packages

Java tiene miles de clases disponibles. Para organizarlas se utiliza el concepto de package (paquete): una forma de agrupar clases que tienen cierta relacion o similitud entre si (fuente: TD_04_04.md).

## Declarar que una clase pertenece a un package

Para indicar que una clase pertenece a un package concreto, se anade una sentencia al principio del fichero, antes incluso de la definicion de la clase. Por ejemplo, para que una clase pertenezca al package figuras (fuente: TD_04_04.md):

```java
package figuras;
```

Esta sentencia inicial establece que todas las clases definidas en ese fichero pertenecen al package indicado.

## Utilizar una clase de un package

Si la clase pertenece al mismo package, se puede utilizar directamente, sin ninguna referencia adicional. Si pertenece a un package distinto (externo), hay que importarla antes de poder usarla, con la sentencia import indicando el package y la clase (fuente: TD_04_04.md):

```java
import figuras.A;
```

Si se quieren importar varias clases del mismo package, se puede sustituir el nombre de la clase concreta por un asterisco, lo que importa todas las clases publicas de ese package de una sola vez (fuente: TD_04_04.md):

```java
import figuras.*;
```

## Que hace realmente la sentencia import

La sentencia import no incorpora codigo nuevo al fichero. Su unica funcion es indicarle al compilador a que clase exactamente se esta haciendo referencia cuando, mas adelante en el programa, se utilice un nombre de clase que podria existir en mas de un package. Es una forma de resolver la ambiguedad, no de copiar codigo (fuente: TD_04_04.md).

## La API de Java como ejemplo de organizacion en packages

La documentacion oficial de la API de Java (version 8) organiza sus clases en alrededor de 200 packages distintos. Cada package agrupa un conjunto de clases relacionadas, y al consultar la documentacion de una clase concreta se puede ver el listado completo de sus metodos y propiedades, ademas de informacion detallada de cada metodo individual (fuente: TD_04_04.md).

## Reglas principales sobre packages, segun la documentacion de Oracle

- Para crear un package para un tipo (clase, interfaz, enumeracion o tipo de anotacion), se coloca una sentencia package como la primera sentencia del fichero fuente que contiene ese tipo.
- Para usar un tipo publico que esta en un package distinto, hay tres opciones: usar el nombre completamente cualificado del tipo, importar el tipo concreto, o importar el package completo del que forma parte ese tipo.
- Las rutas de los ficheros fuente y de los ficheros compilados de un package reflejan el nombre del package.
- Puede ser necesario configurar la variable CLASSPATH para que el compilador y la JVM encuentren los ficheros .class correspondientes a los tipos utilizados.

(fuente: TD_04_04.md)

## Paginas relacionadas

- [[td4-vector]]
- [[td4-practica-packages-herencia]]
- [[td1-compilacion-java]]
