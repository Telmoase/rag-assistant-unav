Programas basicos en Java

Resumen: coleccion de nueve programas de ejemplo en Java que ilustran los elementos basicos del lenguaje: argumentos, tipos de variables, estructuras de control, bucles y funciones.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 1 - Java y Command Prompt/Practica 1. Java y Command Prompt.md

Ultima actualizacion: 2026-06-24

## Programa 1: Hello World

El programa mas basico, que imprime un saludo fijo en pantalla (fuente: Practica 1. Java y Command Prompt.md).

```java
class Hello {
    public static void main(String[] args){
        System.out.println("Hello, World!");
    }
}
```

## Programa 2: Name

Imprime un saludo incluyendo el nombre que se pasa como argumento al programa. Los argumentos se acceden mediante el array `args`, donde `args[0]` es el primer argumento (fuente: Practica 1. Java y Command Prompt.md).

```java
class Name {
    public static void main(String[] args){
        System.out.println("Hello, " + args[0] + "!");
    }
}
```

## Programa 3: Factor2

Multiplica por 2 el argumento que se pasa. Como los argumentos llegan siempre como texto (String), primero hay que convertirlos a un tipo numerico usando `Float.parseFloat()` (fuente: Practica 1. Java y Command Prompt.md).

```java
class Factor2 {
    public static void main(String[] args){
        float x = Float.parseFloat(args[0]);
        System.out.println(x*2);
    }
}
```

## Programa 4: Compare

Imprime `positive` o `negative` segun el valor del argumento, usando una estructura condicional if-else (fuente: Practica 1. Java y Command Prompt.md).

```java
class Compare {
    public static void main(String[] args){
        float x = Float.parseFloat(args[0]);
        if (x >= 0) {
            System.out.println("positive");
        } else {
            System.out.println("negative");
        }
    }
}
```

## Programa 5: Arguments

Imprime todos los argumentos que se pasan al programa, recorriendo el array `args` con un bucle for. `args.length` da el numero total de argumentos recibidos (fuente: Practica 1. Java y Command Prompt.md).

```java
public class Arguments {
    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            System.out.println(i + ": " + args[i]);
        }
        System.out.println("");
    }
}
```

## Programa 6: Types

Muestra el uso de los tipos `boolean` y `char`, dos de los tipos de datos basicos de Java (fuente: Practica 1. Java y Command Prompt.md).

```java
class Types {
    public static void main(String[] args)  {
        boolean b = (1 == 2);
        char c = 'a';
        System.out.println("boolean: " + b + "\t\tchar: " + c); 
   }
}
```

## Programa 7: Numbers

Muestra el comportamiento de los distintos tipos numericos de Java (`byte`, `short`, `int`, `long`, `float`, `double`) al duplicar su valor repetidamente, evidenciando los limites de capacidad de cada tipo cuando se desbordan (fuente: Practica 1. Java y Command Prompt.md).

```java
class Numbers {
    public static void main(String[] args)  {
        byte num_b = 1;
        short num_s = 1;
        int num_i = 1;
        long num_l = 1;
        float num_f = 1;
        double num_d = 1;
        for (int i=1; i<70; i++) {
            num_b *= 2;
            num_s *= 2;
            num_i *= 2;
            num_l *= 2;
            num_f *= 2;
            num_d *= 2;
            System.out.println("i: " + i 
              + " \t\tnum_b: " + num_b 
              + " \t\tnum_s: " + num_s 
              + " \t\tnum_i: " + num_i 
              + " \t\tnum_l: " + num_l
              + " \t\tnum_f: " + num_f
              + " \t\tnum_d: " + num_d);
        }
        System.out.println("End");
   }
}
```

## Programa 8: Letters

Recorre caracter a caracter el argumento recibido, usando `length()` para conocer el numero de caracteres y `charAt(i)` para acceder a cada uno individualmente (fuente: Practica 1. Java y Command Prompt.md).

```java
public class Letters {
    public static void main(String[] args) {
        String nombre = args[0];
        int n = nombre.length();
        String res = "";
        System.out.println(res);
        for (int i=0; i<n; i++) {
            System.out.println(i + ": " + nombre.charAt(i));
        }
    }
}
```

## Programa 9: Factorial

Calcula el factorial de cada numero que se pasa como argumento, usando una funcion auxiliar `factorial()` independiente del metodo main. Muestra como definir y llamar a metodos propios en Java (fuente: Practica 1. Java y Command Prompt.md).

```java
class Factorial{
    public static void main(String[] args) {
        for (int i=0; i<args.length; i++) {
            int n = Integer.parseInt(args[i]);
            float sol = factorial(n);
            System.out.println("Factorial de " + args[i] + " = " + sol);
        }
    }
    static float factorial(int n) {
        float res = 1;
        for (int i=1; i<=n; i++) {
            res = res * i;
            System.out.println("i: " + i + " res: " + res);
        }
        return res;
    }
}
```

## Paginas relacionadas

- [[td1-compilacion-java]]
- [[td1-command-prompt]]
