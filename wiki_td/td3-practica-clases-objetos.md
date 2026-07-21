Practica 3: Clases y objetos

Resumen: ejercicios de la tercera practica, que cubren el uso de la clase Circulo (constructores sobrecargados, metodos de instancia y de clase, referencias compartidas) y la creacion de una clase Matrix para sustituir los arrays sueltos de matrices de la practica anterior.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 3 - Clases y objetos/Practica 3. Clases y objetos.md

Ultima actualizacion: 2026-06-24

## Ejercicio 3.1: Utilizacion de la clase Circulo

El ejercicio parte de la clase [[td3-definicion-de-clases|Circulo]] ya completa, con sus cuatro constructores, los metodos perimetro(), area(), los dos metodos elMayor (de instancia y de clase) y toString() (fuente: Practica 3. Clases y objetos.md).

Se debe completar un programa de prueba que cree varios objetos Circulo de formas distintas:

```java
class pruebaCirculos {
    public static void main(String[] args) {
        System.out.println(new Circulo());
        System.out.println(new Circulo(5.0));
        System.out.println(new Circulo(3,5,2));
        Circulo c1 = new Circulo(7);
        Circulo c2 = new Circulo(12, 10, 8);
        Circulo c3 = new Circulo(c1);
        Circulo c4 = c1;
        System.out.println("Circulo1: " + c1);
        //...
        System.out.println("Perimetro de Circulo1: " + c1.perimetro());
        //...
        System.out.println("El mayor de: " +c1+ ", " +c2+ " es " + c1.elMayor(c2));
        //...
        System.out.println("Cambio de radio de c3 a 10 y c4 a 15");
        c3.r = 10;
        //...
    }
}
```

Circulo3 se crea con el constructor `Circulo(Circulo c)` usando Circulo1 como argumento (una copia independiente), mientras que Circulo4 no se crea con new: se inicializa directamente con Circulo1, por lo que c4 es otra [[td3-objetos-y-referencias|referencia que apunta al mismo objeto]] que c1 (fuente: Practica 3. Clases y objetos.md).

La salida esperada confirma este comportamiento: al cambiar el radio de c3 a 10, solo Circulo3 refleja ese cambio; pero al cambiar despues el radio de c4 a 15, ese cambio se ve tanto en Circulo4 como en Circulo1, porque ambos son referencias al mismo objeto (fuente: Practica 3. Clases y objetos.md):

```
x: 0.0 y: 0.0 r: 1.0
x: 0.0 y: 0.0 r: 5.0
x: 3.0 y: 5.0 r: 2.0
Circulo1: x: 0.0 y: 0.0 r: 7.0
Circulo2: x: 12.0 y: 10.0 r: 8.0
Circulo3: x: 0.0 y: 0.0 r: 7.0
Circulo4: x: 0.0 y: 0.0 r: 7.0
Perimetro de Circulo1: 43.982297150257104
Area de Circulo1: 153.93804002589985
Perimetro de Circulo2: 50.26548245743669
El mayor de: x: 0.0 y: 0.0 r: 7.0, x: 12.0 y: 10.0 r: 8.0 es x: 12.0 y: 10.0 r: 8.0
El mayor de: x: 0.0 y: 0.0 r: 7.0, x: 12.0 y: 10.0 r: 8.0 es x: 12.0 y: 10.0 r: 8.0
Cambio de radio de c3 a 10 y c4 a 15
Circulo1: x: 0.0 y: 0.0 r: 15.0
Circulo2: x: 12.0 y: 10.0 r: 8.0
Circulo3: x: 0.0 y: 0.0 r: 10.0
Circulo4: x: 0.0 y: 0.0 r: 15.0
```

La primera comparacion de mayor se realiza con el metodo de instancia `Circulo elMayor(Circulo c)`; la segunda debe realizarse con el metodo estatico `static Circulo elMayor(Circulo c, Circulo d)` (fuente: Practica 3. Clases y objetos.md).

## Ejercicio 3.2: Aplicacion con objetos, la clase Matrix

En el [[td2-practica-lenguaje-java|Ejercicio 2.6]] de la practica anterior se creaba una aplicacion de matrices usando arrays sueltos. En este ejercicio se deben realizar las mismas funciones, pero encapsulando los datos en una clase Matrix con tres variables miembro: el numero de filas, el numero de columnas, y un array bidimensional con los valores de cada celda. De esta forma cada matriz puede tener sus propias dimensiones (fuente: Practica 3. Clases y objetos.md).

Definicion inicial de la clase Matrix:

```java
import java.util.*;
class Matrix {
    int filas;
    int columnas;
    float [][] value;
    public Matrix() {}
    public Matrix(int filas, int columnas) {
        this.filas = filas;
        this.columnas = columnas;
        value = new float[filas][columnas];
    }
    public String toString() {
        return "Matriz de: " + filas + " filas y " + columnas + " columnas.";
    }
}
```

Hay que completar la clase Matrix con las funciones de lectura, escritura y producto de matrices, esta ultima definida como estatica, y modificar el programa del ejercicio anterior para que use la clase Matrix en lugar de los arrays sueltos (fuente: Practica 3. Clases y objetos.md).

## Paginas relacionadas

- [[td3-definicion-de-clases]]
- [[td3-objetos-y-referencias]]
- [[td2-practica-lenguaje-java]]
- [[td4-practica-packages-herencia]]
