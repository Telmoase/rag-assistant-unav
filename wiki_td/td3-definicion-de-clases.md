Definicion de clases en Java

Resumen: explica como se define una clase en Java (variables miembro, constructor, la palabra reservada this), y desarrolla dos ejemplos completos, Circulo y Complex, que ilustran la sobrecarga de constructores, los miembros estaticos, la sobrecarga de metodos y la inmutabilidad de objetos.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_04.md, Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_05.md, Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_07.md

Ultima actualizacion: 2026-06-24

## Estructura basica de una clase

Una clase en Java se define con la palabra reservada class, seguida del nombre de la clase y un cuerpo delimitado por llaves. Dentro del cuerpo se definen las variables miembro (los atributos que tendran los objetos de esa clase) y sus constructores y metodos (fuente: TD_03_04.md):

```java
class Circulo {
    double x;
    double y;
    double r;
}
```

Una vez definida la clase, se crean objetos de ella con la palabra reservada new (ver [[td3-objetos-y-referencias]]).

## El constructor

Un constructor es un metodo especial que tiene el mismo nombre que la clase y que se ejecuta cuando se crea un nuevo objeto con new. Su funcion habitual es asignar valores iniciales a las variables miembro a partir de los argumentos que recibe. Es habitual que los nombres de los parametros coincidan con los nombres de las variables miembro que van a inicializar, por comodidad y claridad (fuente: TD_03_04.md):

```java
Circulo (double x, double y, double r) {
    ...
}
```

## El problema de los nombres iguales: la palabra reservada this

Cuando el nombre de un parametro coincide con el nombre de una variable miembro, dentro del cuerpo del constructor el nombre simple (por ejemplo, x) hace referencia al parametro local, no a la variable miembro de la clase: se dice que el parametro oculta (shadow) a la variable miembro. Para referirse explicitamente a la variable miembro del objeto actual se usa this, una referencia al objeto sobre el que se esta ejecutando el constructor o el metodo (fuente: TD_03_04.md):

```java
class Circulo {
    double x;
    double y;
    double r;
    Circulo (double x, double y, double r) {
        this.x = x;
        this.y = y;
        this.r = r;
    }
}
```

En cada linea, this.x se refiere a la variable miembro del objeto, mientras que x sin this se refiere al parametro recibido por el constructor. Sin this, una asignacion como x = x no tendria ningun efecto util, porque asignaria el parametro a si mismo en lugar de a la variable miembro (fuente: TD_03_04.md).

Cuando no hay ningun parametro con el mismo nombre que una variable miembro, no es necesario usar this para referirse a ella, porque no hay ninguna variable local que la oculte. Esto se ve en un metodo print() de una clase P2 con variables posicion y cantidad, donde se accede directamente a posicion y cantidad sin this (fuente: TD_03_04.md).

## La clase Circulo completa

Reuniendo variables, constructores y metodos, la clase Circulo queda definida asi (fuente: TD_03_05.md):

```java
public class Circulo {
    static int numCirculos = 0;
    public static final double PI=3.14159265358979323846;
    public double x;
    public double y;
    public double r;

    public Circulo(double x, double y, double r) {
        this.x=x;
        this.y=y;
        this.r=r;
        numCirculos++;
    }
    public Circulo(double r) {
        this(0.0, 0.0, r);
    }
    public Circulo(Circulo c) {
        this(c.x, c.y, c.r);
    }
    public Circulo() {
        this(0.0, 0.0, 1.0);
    }
    public double perimetro() {
        return 2.0 * PI * r;
    }
    public double area() {
        return PI * r * r;
    }
    public Circulo elMayor(Circulo c) {
        if (this.r>=c.r) {
            return this;
        } else {
            return c;
        }
    }
    public static Circulo elMayor(Circulo c, Circulo d) {
        if (c.r>=d.r) {
            return c;
        } else {
            return d;
        }
    }
    public String toString() {
        return "x: " + x + " y: " + y + " r: " + r;
    }
}
```

## Variables de clase: static y final

Circulo tiene tres variables miembro de tipo double (x, y, r) que representan la posicion del centro y el radio. Ademas, tiene dos elementos declarados como static, lo que significa que pertenecen a la clase en si y no a cada objeto individual: numCirculos, un contador que se incrementa cada vez que se crea un circulo, y la constante PI, declarada tambien como final, de forma que su valor no puede cambiar una vez asignado (fuente: TD_03_05.md).

## Los cuatro constructores y la invocacion explicita con this(...)

La clase tiene cuatro constructores, cada uno pensado para un caso de uso distinto (fuente: TD_03_05.md):

- El primero recibe los tres valores (x, y, r) y los asigna usando this, ademas de incrementar numCirculos.
- El segundo recibe solo el radio r y llama al primer constructor con this(0.0, 0.0, r), creando un circulo centrado en el origen.
- El tercero recibe otro objeto Circulo y llama al primer constructor con sus coordenadas y radio (c.x, c.y, c.r), creando una copia.
- El cuarto no recibe argumentos y llama al primero con los valores por defecto (0.0, 0.0, 1.0).

Usar this(...) dentro de un constructor para llamar a otro constructor de la misma clase se conoce como invocacion explicita de constructor, y esa llamada debe ser la primera linea del constructor (fuente: TD_03_05.md).

## Sobrecarga de metodos: elMayor de instancia y elMayor de clase

La clase incluye dos metodos llamados elMayor, implementados de forma distinta. El primero es un metodo de instancia: se invoca sobre un objeto concreto (por ejemplo, circuloA.elMayor(circuloB)) y compara this.r con c.r. El segundo es un metodo de clase, marcado como static, que recibe los dos circulos como argumentos (Circulo c, Circulo d) y no necesita invocarse sobre ningun objeto en particular. Java permite que existan dos metodos con el mismo nombre dentro de la misma clase siempre que tengan distinta firma; esto se conoce como sobrecarga de metodos (fuente: TD_03_05.md).

## El metodo toString

toString() es un metodo que Java invoca automaticamente al intentar imprimir un objeto directamente, por ejemplo con System.out.println(unCirculo). En Circulo devuelve una cadena con el formato "x: valor y: valor r: valor" (fuente: TD_03_05.md).

## Otro ejemplo: la clase Complex e inmutabilidad

Complex representa numeros complejos (parte real e imaginaria), un ejemplo tomado del libro de Sedgewick y Wayne, de la Universidad de Princeton. Declara sus dos variables miembro como final (fuente: TD_03_07.md):

```java
private final double re;
private final double im;
```

Declarar estas variables como final significa que, una vez asignado su valor en el constructor, no pueden volver a modificarse: los objetos Complex son inmutables. Cualquier operacion que parezca modificar un numero complejo en realidad crea y devuelve un nuevo objeto Complex con el resultado (fuente: TD_03_07.md).

El constructor recibe los valores real e imag y los asigna a re e im. Como los nombres de los parametros son distintos de los nombres de las variables miembro, no es necesario usar this para distinguirlos, aunque tambien habria sido valido nombrarlos igual y usar this.re y this.im (fuente: TD_03_07.md).

## Operaciones que devuelven un nuevo objeto

Para sumar dos numeros complejos se define un metodo que recibe otro objeto Complex y devuelve un nuevo objeto Complex con el resultado, sin modificar ninguno de los dos objetos originales (fuente: TD_03_07.md):

```java
public Complex plus(Complex b) {
    Complex a = this;
    double real = a.re + b.re;
    double imag = a.im + b.im;
    return new Complex(real, imag);
}
```

Aqui this se guarda en una variable local llamada a por claridad, y se accede a a.re y a.im igual que a b.re y b.im. El resultado se devuelve como un objeto nuevo, manteniendo la inmutabilidad de la clase. Complex tambien define un toString() y metodos sin argumentos como abs() (el modulo, con Math.hypot(re, im)) y phase() (la fase, con Math.atan2(im, re)), que no necesitan parametros porque toda la informacion ya esta en las variables miembro del propio objeto (fuente: TD_03_07.md).

## Paginas relacionadas

- [[td3-objetos-y-referencias]]
- [[td3-practica-clases-objetos]]
- [[td2-tipos-y-variables]]
- [[td4-static]]
- [[td4-herencia]]
- [[td4-modificadores-de-acceso]]
