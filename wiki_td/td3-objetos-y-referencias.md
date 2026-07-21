Creacion de objetos y arrays de objetos en Java

Resumen: explica como se crea un objeto con la palabra reservada new, como funcionan las referencias compartidas entre variables, como se declaran y crean arrays de objetos en dos pasos diferenciados, y como se unifica la sintaxis de declaracion para tipos primitivos, referencias a objetos y arrays.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_02.md, Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_03.md, Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_06.md

Ultima actualizacion: 2026-06-24

## Por que es necesaria la palabra reservada new

Definir una clase (ver [[td3-definicion-de-clases]]) establece la estructura de sus objetos, pero no crea ningun objeto por si misma. Para crear un objeto concreto hay que llamar a un constructor de esa clase usando la palabra reservada new. Un constructor es un metodo especial con el mismo nombre que la clase, encargado de inicializar el objeto en el momento en que se crea (fuente: TD_03_02.md).

## Declaracion de una referencia a un objeto

Antes de crear el objeto se puede declarar una variable que actuara como referencia a el, indicando primero el tipo (el nombre de la clase) y despues el nombre de la variable, igual que con un tipo primitivo (fuente: TD_03_02.md):

```java
MyClass unaRef;
```

En este punto la referencia todavia no apunta a ningun objeto real: se inicializa a null (fuente: TD_03_02.md).

## Creacion del objeto con new

Para crear el objeto y que la referencia apunte a el, se usa new seguido del constructor de la clase (fuente: TD_03_02.md):

```java
unaRef = new MyClass();
```

Tambien se pueden combinar declaracion y creacion en una sola sentencia:

```java
MyClass otraRef = new MyClass();
```

Tambien es valido crear un objeto e invocar un metodo sobre el directamente, sin guardarlo antes en una variable, si no se va a volver a utilizar:

```java
System.out.println(new Circulo(0.0, 0.0, 5.0));
```

(fuente: TD_03_02.md)

## Referencias que apuntan al mismo objeto

Es posible declarar una segunda referencia y asignarle el mismo valor que otra referencia ya existente (fuente: TD_03_02.md):

```java
MyClass segundaRef = unaRef;
```

En este caso segundaRef no crea un objeto nuevo, sino que pasa a apuntar al mismo objeto que unaRef. Cualquier cambio realizado a traves de una de las dos referencias sera visible tambien a traves de la otra, porque ambas senalan al mismo objeto en memoria (fuente: TD_03_02.md).

## Arrays de objetos: declaracion y creacion en dos pasos

La sintaxis para declarar un array de objetos es igual que la de un array de un tipo primitivo, pero usando el nombre de la clase como tipo (fuente: TD_03_03.md):

```java
Circulo [] vectorCirculos;
```

Para crear el array con un tamano determinado se usa new indicando el numero de elementos entre corchetes (fuente: TD_03_03.md):

```java
vectorCirculos = new Circulo[5];
```

Esta sentencia crea el array (el espacio para 5 referencias a objetos Circulo), pero no crea ningun objeto Circulo todavia: cada posicion queda inicializada a null (fuente: TD_03_03.md).

## Inicializar cada posicion del array con su propio objeto

Para que cada posicion contenga un objeto real, hay que crear cada objeto individualmente y asignarlo a la posicion correspondiente (fuente: TD_03_03.md):

```java
vectorCirculos[0] = new Circulo(0.0, 0.0, 5.0);
```

Crear un array de objetos es por tanto un proceso en dos pasos: primero se crea el array de referencias, y despues se debe crear cada objeto individualmente y asignarlo a su posicion. Esto contrasta con los arrays de tipos primitivos, donde crear el array ya deja cada posicion con un valor por defecto utilizable, como 0 para los tipos enteros (fuente: TD_03_03.md).

## Una misma estructura para todas las declaraciones

Tanto las variables de tipos primitivos como las referencias a objetos, y tanto los arrays de tipos primitivos como los arrays de objetos, siguen exactamente la misma estructura de declaracion en Java: primero el tipo, despues el nombre de la variable (fuente: TD_03_06.md):

```java
int x;                          // variable de tipo primitivo
Circulo unCirculo;               // referencia a un objeto
int [] vector;                   // array de tipo primitivo
Circulo [] vectorCirculos;        // array de objetos
```

Los corchetes de un array se pueden colocar tanto antes como despues del nombre de la variable; ambas formas son equivalentes (fuente: TD_03_06.md).

## Dos formas de inicializar un array

Hay dos formas de dar contenido a un array de tipo primitivo una vez declarado: usar new indicando el tamano entre corchetes, o indicar directamente los valores entre llaves, lo que fija automaticamente el tamano al numero de elementos indicados (fuente: TD_03_06.md):

```java
int [] vector = new int[10];
int [] vector = {1, 2, 3, 4, 5};
```

Para un array de objetos, en cambio, declarar y crear el array con new solo crea el espacio de referencias, todas inicializadas a null; cada objeto debe crearse e inicializarse individualmente, asignandolo a su posicion correspondiente (fuente: TD_03_06.md).

## Paginas relacionadas

- [[td2-tipos-y-variables]]
- [[td3-definicion-de-clases]]
- [[td3-practica-clases-objetos]]
- [[td4-vector]]
