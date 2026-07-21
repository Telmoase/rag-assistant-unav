Practica 5: Packages y herencia

Resumen: ejercicios de la quinta practica, que sustituyen la clase Matrix propia por la del package externo Jama, gestionan las matrices con un Vector en lugar de variables sueltas, y crean una clase NMatrix que extiende Matrix para anadirle un nombre.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/Practica 5. Packages y herencia.md

Ultima actualizacion: 2026-06-24

## Ejercicio 5.1: Packages

Parte de la solucion del [[td3-practica-clases-objetos|Ejercicio 3.2]] (gestion de matrices) y la modifica en varios pasos (fuente: Practica 5. Packages y herencia.md):

1. En lugar de usar la clase propia Matrix.java, utilizar la del [[td4-packages|package]] externo Jama, incluyendo `import Jama.Matrix;` y anadiendo el fichero Jama-1.0.2.jar a la variable classpath: `set classpath=%classpath%;.;Q:\Java\Jama-1.0.2.jar` (esta sentencia se puede anadir al mismo fichero .bat donde se define la variable PATH).

2. Sustituir las dos instancias sueltas de Matrix (matrizA y matrizB) por un [[td4-vector|Vector]] de objetos Matrix:

```java
static Vector<Matrix> matrices = new Vector<Matrix>();
```

Usando los metodos `addElement(Object)`, `int size()`, `elementAt(int i)` y `remove(int i)` (que borra el elemento en la posicion i y reajusta el tamano). En el metodo Opcion1(), por ejemplo:

```java
matrices.addElement(LeerMatriz());
matrices.addElement(LeerMatriz());
```

3. Generalizar el programa para que gestione un numero indefinido de matrices: la opcion 1 lee una sola matriz y la anade al vector, y al multiplicar dos matrices se pregunta cuales son las matrices a multiplicar, con un metodo `int SeleccionMatriz()` que pide el numero de matriz y lo devuelve.

4. Implementar las funciones restantes de gestion de matrices usando los metodos de la clase Matrix de Jama: matriz traspuesta, matriz inversa, borrar matriz y calcular el determinante (documentacion de Jama en `http://math.nist.gov/javanumerics/jama/`).

## Ejercicio 5.2: Herencia, la clase NMatrix

Las matrices del ejercicio anterior se identifican solo por su numero. Para darle un nombre a cada matriz sin modificar la clase Matrix del package Jama, se crea una nueva clase NMatrix que [[td4-herencia|extiende]] de Matrix (fuente: Practica 5. Packages y herencia.md):

```java
import Jama.Matrix;
public class NMatrix extends Matrix {
    String name;

    public NMatrix (String nombre, double[][] A, int m, int n) {
        super(A, m, n);
        name = nombre;
    }
    public void print (int w, int d) {
        System.out.println("Matrix " + name);
        super.print(w,d);
    }
}
```

El constructor de NMatrix llama a `super(A, m, n)` para reutilizar el constructor de Matrix, y guarda el nombre en su propia variable. El metodo print() sobrescribe el de Matrix: imprime primero el nombre y despues llama a `super.print(w,d)` para reutilizar la impresion original de Matrix (fuente: Practica 5. Packages y herencia.md).

Se debe usar NMatrix en el ejercicio de gestion de matrices de forma que, al crear una nueva matriz, se pida su nombre, y al imprimirla se muestre. No es necesario usar NMatrix en el resto de funciones, lo que permite observar que, al imprimir las matrices, unas se imprimen con el nuevo metodo (con nombre) y otras con el original, sin nombre (fuente: Practica 5. Packages y herencia.md).

## Paginas relacionadas

- [[td4-herencia]]
- [[td4-packages]]
- [[td4-vector]]
- [[td3-practica-clases-objetos]]
- [[td5-practica-html-basico]]
