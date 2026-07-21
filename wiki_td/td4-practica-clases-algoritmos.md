Practica 4: Clases y algoritmos

Resumen: ejercicios de la cuarta practica, que cubren variables y funciones de clase con la misma area en distintos ambitos, un algoritmo de ordenacion sobre un array de enteros, y la utilizacion de la clase Complex para crear, sumar, multiplicar y ordenar numeros complejos.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/Practica 4. Clases y algoritmos.md

Ultima actualizacion: 2026-06-24

## Ejercicio 4.1: Funciones de clase y variables de clase

Este ejercicio define y llama a una funcion (metodo) de una clase, junto con [[td4-static|variables de clase (static)]] y variables locales en las funciones. La variable area tiene deliberadamente el mismo nombre en los tres ambitos (clase, main y la funcion Area), a pesar de lo que recomiendan las guias de estilo, precisamente para observar cuando y como se utiliza cada una (fuente: Practica 4. Clases y algoritmos.md):

```java
class Ejer1 {
    static double area; // variable de la clase
    public static void main(String args[]){
        double radio; // variable de la funcion main
        double area; // variable de la funcion main

        if ( args.length < 1){
            System.out.println("Pasar el radio. Ej. : >java Ejer6 12.5");
            System.exit(0);
        }
        radio = Double.parseDouble(args[0]);
        area = Ejer1.Area(radio);
        System.out.println("Area del circulo r="+radio + "m. = " + area+" m2");
        area = Ejer1.area;
        System.out.println("Area del circulo r="+radio+"m. = "+area+" Has.");
    }
    public static double Area ( double rd) {
        double area; //variable local de la funcion Area
        //usar la variable local
        area = Math.PI*Math.pow(rd,2.0);
        //acceder a la variable de la clase
        Ejer1.area = area/10000; //obtener el area en Has.
        return area; //devuelve el valor
    }
}
```

La variable area de la clase puede ser accedida por cualquier metodo de la clase, a diferencia de las variables declaradas dentro de cada metodo, que son locales. El metodo estatico pow() de la clase Math eleva el primer argumento a la potencia del segundo (fuente: Practica 4. Clases y algoritmos.md).

Variacion: introducir la funcion Perimetro() para el calculo del perimetro en metros y kilometros, e imprimir ambos valores.

## Ejercicio 4.2: Algoritmo de ordenacion

Programa que ordena de menor a mayor los numeros recibidos como argumentos, usando variables miembro static (Numero y un array Datos) y un algoritmo de ordenacion por intercambio de pares (fuente: Practica 4. Clases y algoritmos.md):

```java
class Ejer2 {
    static int Numero;
    static int[] Datos;

    public static void main(String [] args) {
        Ejer2.Numero = args.length;
        Ejer2.Datos = new int[Ejer2.Numero];
        for (int i=0;i< Ejer2.Numero;i++ ) {
            Ejer2.Datos[i] = Integer.parseInt(args[i]);
        }
        Ejer2.Ordena();
    }
    public static void Ordena() {
        System.out.println("\nLos numeros sin ordenar son: ");
        for (int i=0;i<Numero;i++)
            System.out.println("Num: "+i+" valor: "+Datos[i]);
        for (int i=0;i < Numero-1;i++) {
            for (int j=i+1;j<Numero;j++) {
                if ( Datos[i] > Datos[j]) {
                    int tmp = Datos[j];
                    Ejer2.Datos[j] = Datos[i];
                    Ejer2.Datos[i] = tmp;
                }
            }
        }
        System.out.println("\nLos numeros ordenados de menor a mayor son: ");
        for (int i=0;i<Numero;i++)
            System.out.println("Num: "+i+" valor: "+Datos[i]);
    }
}
```

Uso: `java Ejer2 5 7 2 45 12 5 -4` (fuente: Practica 4. Clases y algoritmos.md).

Variacion: en lugar de recibir los numeros como argumentos, generarlos aleatoriamente entre 0 y 100, indicando la cantidad a generar como argumento del programa (por ejemplo, `java Ejer2 10`).

## Ejercicio 4.3: Utilizacion de la clase Complex

Como Java no tiene un tipo predefinido para numeros complejos, este ejercicio utiliza la clase Complex de Sedgewick y Wayne (la misma clase descrita en [[td3-definicion-de-clases|Definicion de clases en Java]]), descargable de `http://www.cs.princeton.edu/introcs/32class/Complex.java`. Se pide crear instancias de dos numeros complejos (por ejemplo 3+2i y 5-8i), realizar su suma y multiplicacion, obtener el conjugado de uno de ellos, y el producto de uno por su conjugado; ademas, crear un array de 10 posiciones, rellenarlas con numeros complejos aleatorios (parte real e imaginaria entre 0 y 10), y multiplicar cada numero por su conjugado, comprobando que la parte imaginaria resultante es nula (fuente: Practica 4. Clases y algoritmos.md).

## Ejercicio 4.4: Creacion de un metodo de ordenacion para Complex

A partir de la clase Complex del ejercicio anterior, se pide crear el metodo estatico `Ordena(Complex[])`, que recibe un vector de numeros complejos y los ordena en base a su modulo (obtenido con el metodo abs() de Complex). El metodo no devuelve ningun valor, por lo que se define como void (fuente: Practica 4. Clases y algoritmos.md).

## Ejercicio 4.5: Otra implementacion de Complex, en coordenadas polares

Repite el ejercicio 4.3 pero usando una implementacion distinta de la clase Complex, basada en coordenadas polares en lugar de coordenadas rectangulares, descargable de `http://www.cs.princeton.edu/introcs/33design/Complex.java`. Como tiene el mismo nombre que la version anterior, debe guardarse en un directorio distinto. Hay que completar la definicion con una funcion conjugado, donde el conjugado del complejo (r, angulo) es (r, -angulo), y repetir la creacion del array de 10 posiciones con los bucles de relleno y multiplicacion por el conjugado (fuente: Practica 4. Clases y algoritmos.md).

## Paginas relacionadas

- [[td4-static]]
- [[td3-definicion-de-clases]]
- [[td4-practica-packages-herencia]]
