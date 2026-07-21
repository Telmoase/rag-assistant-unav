Practica 2: Lenguaje Java

Resumen: ejercicios de la segunda practica de Tecnologia Digital, que cubren secuencias de escape en strings, sentencias de control segun Java Code Conventions, factorial con bucle for e iteracion recursiva, bucle while con numeros aleatorios y matrices bidimensionales.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 2 - Variables y sentencias de control/Practica 2. Lenguaje Java.md

Ultima actualizacion: 2026-06-24

## Ejercicio 2.1: Cadenas de caracteres con comillas dobles

Para incluir comillas dobles dentro de un String en Java se usa la secuencia de escape `\"`. Por ejemplo, `"Num: \"20\"."` produce la salida `Num: "20".` (fuente: Practica 2. Lenguaje Java.md).

El ejercicio consiste en adaptar Ejer1 de la practica anterior para que la salida sea del tipo:

```
El Mayor de "20" y "25" es: "25"
```

## Ejercicio 2.2: Sentencias de control segun Java Code Conventions

A partir de la estructura del capitulo 7 de [[td2-estilo-de-codigo-java|Java Code Conventions]] (Statements), se completa una clase que incluya ejemplos de los distintos tipos de sentencias: `if`, `for`, `while`, `switch`, etc. El ejemplo de partida muestra la sentencia `if` (fuente: Practica 2. Lenguaje Java.md):

```java
public class Ejer2{
    public static void main(String args[]){
        int a = 10;
        int b = 7;
        // 7.4 if
        if (a > b) {
            System.out.println("a es mayor");
        }
    }
}
```

## Ejercicio 2.3: Factorial con bucle for

Calcula el factorial de un numero leido por teclado usando un bucle `for` descendente. El acumulador `Fact` se inicializa con el valor de entrada y se multiplica por cada entero anterior hasta 1 (fuente: Practica 2. Lenguaje Java.md):

```java
import java.util.*;
public class Ejer3 {
    public static void main(String args[]) {
        int x1;
        long Fact;
        Scanner in = new Scanner(System.in);
        System.out.println("Introduzca el numero: ");
        x1=in.nextInt();
        Fact=x1;
        for (int i=x1-1; i>0; i--){
            Fact *= i;
        }
        System.out.println("\rFactorial de "+x1+" es: "+Fact);
    }
}
```

Variacion: realizar el mismo calculo con el bucle `for` ascendente (de 1 hasta x1).

## Ejercicio 2.4: Factorial recursivo

Implementa el factorial con una funcion recursiva: el factorial de 1 es 1, y el factorial de n es n multiplicado por el factorial de n-1 (fuente: Practica 2. Lenguaje Java.md):

```java
import java.util.*;
public class Ejer4 {
    public static void main(String args[]) {
        int x1;
        Scanner in = new Scanner(System.in);
        System.out.println("Introduzca el numero: ");
        x1=in.nextInt();
        System.out.println("\rFactorial de "+x1+" es: "+factorial(x1));
    }

    public static long factorial (long num) {
        if (num == 1) {
            return 1;
        } else {
            return num * factorial(num - 1);
        }
    }
}
```

## Ejercicio 2.5: Bucle while con numeros aleatorios

Genera con un bucle `while` una cantidad de numeros reales aleatorios entre 0 y 10. El metodo `Math.random()` devuelve un valor entre 0.0 y 1.0, que se multiplica por 10 para escalar al rango deseado (fuente: Practica 2. Lenguaje Java.md):

```java
import java.util.*;
public class Ejer5 {
    public static void main(String args[]) {
        int x1;
        double val;
        Scanner in = new Scanner(System.in);
        System.out.print("Cuantos Numeros?: ");
        x1=in.nextInt();
        while((x1--)>0) {
            val = Math.random();
            val = val * 10;
            System.out.println("Numero: " + val);
        }
    }
}
```

Variacion: introducir por teclado los limites del rango de generacion.

## Ejercicio 2.6: Lectura y escritura de matrices bidimensionales

Implementa las tres primeras opciones del menu de matrices del [[td1-practica-compilar-java|Ejercicio 1.3]]: introducir, mostrar y multiplicar matrices. Las variables de las matrices se declaran como arrays bidimensionales de tipo `float` (fuente: Practica 2. Lenguaje Java.md):

```java
static int filas;
static int columnas;
static float [][]matrizA;
static float [][]matrizB;
```

La funcion auxiliar `LeerMatriz()` recorre filas y columnas con dos bucles `for` anidados y devuelve el array relleno:

```java
public static float[][] LeerMatriz() {
    float[][] matriz = new float[filas][columnas];
    for (int i=0; i< filas; i++) {
        for (int j=0; j< columnas; j++) {
            System.out.println("Celda (" + (i + 1) + ", " + (j + 1) + "): ");
            matriz[i][j] = in.nextFloat();
        }
    }
    return matriz;
}
```

La multiplicacion de matrices solo funciona correctamente con matrices cuadradas en la estructura actual.

## Paginas relacionadas

- [[td1-practica-compilar-java]]
- [[td2-tipos-y-variables]]
- [[td2-estilo-de-codigo-java]]
- [[td3-practica-clases-objetos]]
