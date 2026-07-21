Practica 1: Compilar y ejecutar en Java

Resumen: ejercicios de la primera practica de Tecnologia Digital, desde el primer programa Hello World hasta la lectura y escritura de ficheros, pasando por argumentos, entrada por teclado y menus con switch.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 2 - Variables y sentencias de control/Practica 1. Compilar y ejecutar en Java.md

Ultima actualizacion: 2026-06-24

## Ejercicio 1.0: Primer programa en Java

Se escribe el siguiente programa con un editor de texto, respetando exactamente mayusculas y minusculas, y se guarda como `PrimerPrograma.java` (fuente: Practica 1. Compilar y ejecutar en Java.md):

```java
/* Estructura general de un programa en Java */
// Otra forma de comentar solo una linea
public class PrimerPrograma {
    public static void main (String args[]){
        System.out.println("Primer programa en Java");
    } // Fin de main()
} // Fin de la clase MiPrograma
```

Pasos para compilar y ejecutar:

1. Definir la variable PATH con el directorio de las herramientas JDK: `set PATH=.;Q:\Java\jdk1.6.0_04\bin;%PATH%`
2. Navegar hasta el directorio donde esta el fichero.
3. Compilar: `javac PrimerPrograma.java`
4. Ejecutar: `java PrimerPrograma`

Este paso de definir el PATH manualmente correspondia a los ordenadores de las aulas de la universidad, donde el JDK estaba instalado en una unidad de red (Q:) y no formaba parte del PATH por defecto del sistema. En un ordenador personal con el JDK instalado y anadido al PATH, este paso no es necesario (ver [[td1-compilacion-java|Nota sobre PATH]]).

## Ejercicio 1.1: Pasando argumentos al programa

Se pasan dos numeros al programa desde la linea de comandos y el programa indica cual es el mayor. Los argumentos se convierten de String a float con `Float.parseFloat()`, y se usa `Math.max()` para comparar (fuente: Practica 1. Compilar y ejecutar en Java.md).

```java
public class Ejer1{
    public static void main(String args[]){
        float x1=0;
        float x2=0;
        if ( args.length<2 ) {
            System.out.println("Faltan los dos numeros");
        } else {
            x1 = Float.parseFloat(args[0]);
            x2 = Float.parseFloat(args[1]);
            System.out.println("El mayor es: " + Math.max(x1,x2));
        }
    }
}
```

Ejecucion: `java Ejer1 20 25`

## Ejercicio 1.2: Lectura de datos desde el teclado

Usa `Scanner` para leer numeros introducidos por el usuario en tiempo de ejecucion (fuente: Practica 1. Compilar y ejecutar en Java.md):

```java
import java.io.*;
import java.util.*;
public class Ejer2 {
    public static void main(String args[]) throws IOException {
        float x1=0;
        float x2=0;
        Scanner in = new Scanner(System.in);
        System.out.println("Primer Numero: ");
        x1=in.nextFloat();
        System.out.println("Segundo Numero: ");
        x2=in.nextFloat();
        System.out.println("El Mayor es: " + Math.max(x1,x2));
    }
}
```

## Ejercicio 1.3: Menu de aplicacion con switch

Programa que muestra un menu en bucle, lee la opcion del usuario y la ejecuta con una sentencia `switch`. El bucle `while` continua hasta que el usuario elige la opcion de salir. Las funciones son `static` por simplicidad (fuente: Practica 1. Compilar y ejecutar en Java.md):

```java
import java.util.*;
public class Ejer3 {
    static Scanner in = new Scanner(System.in);
    public static void main(String args[]) {
        char tecla=0;
        while( tecla != '4') {
            Ejer3.Menu();
            tecla = Ejer3.LeeTecla();
            switch (tecla) {
                case '1': Ejer3.Opcion1(); break;
                case '2': Ejer3.Opcion2(); break;
                case '3': Ejer3.Opcion3(); break;
                case '4': Ejer3.Opcion4(); break;
                default: Ejer3.NoOpcion(); break;
            }
        }
    }
    // ... metodos Menu(), LeeTecla(), Opcion1()-Opcion4(), NoOpcion()
}
```

## Ejercicio 1.4: Escritura de un fichero

Para abrir un fichero y escribir en el se usa `FileWriter` y `PrintWriter`. Permite usar `print()` y `println()` igual que con la salida estandar. Se cierra con `fileWriter.close()` (fuente: Practica 1. Compilar y ejecutar en Java.md):

```java
import java.io.*;
import java.util.*;
public class Ejer4 {
    static Scanner in = new Scanner(System.in);
    public static void main(String args[]) throws IOException {
        System.out.println("Escriba el numero del que desea la tabla: ");
        int numero = in.nextInt();
        FileWriter fileWriter = new FileWriter("tabla_del_" + numero, false);
        PrintWriter toFile = new PrintWriter(fileWriter);
        for (int i=1; i<= 10; i++) {
            toFile.println(numero + " x " + i + " = " + i*numero);
        }
        fileWriter.close();
    }
}
```

El segundo argumento de `FileWriter` controla si se anade al fichero existente (`true`) o se sobreescribe (`false`).

## Ejercicio 1.5: Lectura de un fichero

Usa `Scanner` sobre un objeto `File` para leer y mostrar linea a linea el contenido de un fichero (fuente: Practica 1. Compilar y ejecutar en Java.md):

```java
import java.io.*;
import java.util.*;
public class Ejer5 {
    static Scanner in = new Scanner(System.in);
    public static void main(String args[]) throws IOException {
        System.out.println("Escriba el nombre del fichero");
        String fichero = in.next();
        File file = new File(fichero);
        Scanner inFile = new Scanner(file);
        String line = null;
        while (inFile.hasNext()) {
            line = inFile.nextLine();
            System.out.println(line);
        }
    }
}
```

## Paginas relacionadas

- [[td1-compilacion-java]]
- [[td1-programas-basicos-java]]
- [[td2-practica-lenguaje-java]]
- [[td5-practica-html-basico]]
