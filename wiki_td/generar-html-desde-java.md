Generar HTML desde Java

Resumen: explica como un programa Java puede generar una pagina web completa imprimiendo etiquetas HTML con System.out.println y redirigiendo esa salida a un fichero .html, ilustrado con el programa HelloWorld.java.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 6 - Formularios en HTML/TD_06_05.md

Ultima actualizacion: 2026-06-24

## La idea: imprimir HTML en lugar de texto plano

Un programa Java que imprime texto en pantalla con `System.out.println` puede imprimir cualquier texto, incluido texto que contenga etiquetas [[td5-html-basico|HTML]]. Si esa salida se redirige a un fichero con extension `.html` en lugar de mostrarse en la consola, el resultado es una pagina web generada por el programa (fuente: TD_06_05.md).

## El programa HelloWorld.java

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("<H1>Hello, World!</H1>");
        System.out.println("<H2>Second line</H2>");
        for (int i=0; i<10; i++) {
            System.out.println("<H3>Line " + i + "</H3>");
        }
    }
}
```

## Construccion paso a paso

El punto de partida es un programa que imprime un mensaje por pantalla como texto plano. El primer cambio es convertir ese mensaje en codigo HTML, por ejemplo envolviendolo en una etiqueta de cabecera `H1`. Tras modificar la linea, hay que volver a compilar el programa; al ejecutarlo, la salida se redirige a un fichero (por ejemplo, `FP1.html`) en lugar de mostrarse en consola, y se abre ese fichero en el navegador para ver el resultado con el formato aplicado (fuente: TD_06_05.md).

Cada cambio posterior en el codigo fuente (anadir una segunda linea con otro nivel de cabecera, por ejemplo) requiere el mismo ciclo: guardar, compilar, ejecutar de nuevo redirigiendo la salida al mismo fichero HTML, y recargar la pagina en el navegador (fuente: TD_06_05.md).

## Generar contenido repetitivo con un bucle

Escribir HTML desde Java resulta especialmente util cuando la pagina depende de algun parametro de entrada, o cuando hay que repetir una operacion varias veces. Por ejemplo, para escribir un mensaje diez veces se usa un bucle `for` que va de 0 a un valor menor que 10, generando dentro del bucle una linea de HTML con el numero de iteracion concatenado en el texto (fuente: TD_06_05.md).

Combinar la logica de un programa Java (bucles, condicionales, calculos) con la generacion de texto HTML permite crear paginas web de forma dinamica y automatizada, en lugar de escribir manualmente cada linea del fichero, especialmente cuando el contenido depende de datos variables o se repite con pequenas diferencias (fuente: TD_06_05.md).

## Paginas relacionadas

- [[td5-practica-html-basico]]
- [[td1-practica-compilar-java]]
- [[td5-html-basico]]
- [[td7-servlets]]
