Compilacion y ejecucion de programas Java

Resumen: explica el proceso completo por el que un programa Java pasa de codigo fuente a ejecucion, incluyendo el papel del compilador, el bytecode y la JVM, con una guia practica y una construccion incremental del primer programa.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 1 - Java y Command Prompt/TD_01_01.md, Tecnologia Digital/Tema 1 - Java y Command Prompt/TD_01_03.md, Tecnologia Digital/Tema 1 - Java y Command Prompt/TD_01_04.md

Ultima actualizacion: 2026-06-24

## El proceso de compilacion

Un ordenador solo puede ejecutar instrucciones en lenguaje maquina. Los programadores escriben en un lenguaje de alto nivel como Java y el codigo pasa por varios pasos antes de ejecutarse (fuente: TD_01_01.md):

1. **Escritura del codigo fuente**: el programador escribe el programa en un fichero de texto plano con extension `.java`.
2. **Compilacion con javac**: el compilador traduce el fichero `.java` a un fichero `.class`.
3. **Bytecode**: el fichero `.class` no contiene codigo nativo del procesador, sino bytecode, el lenguaje propio de la Maquina Virtual de Java.
4. **Ejecucion por la JVM**: la Maquina Virtual de Java interpreta el bytecode y lo convierte en instrucciones para el procesador concreto de cada maquina.
5. **Salida**: el resultado se muestra en pantalla.

```
MyProgram.java  --(javac)-->  MyProgram.class (bytecode)  --(JVM)-->  Ejecucion
```
(fuente: TD_01_01.md)

## Bytecode y portabilidad

Compilar a bytecode en lugar de codigo nativo permite que el mismo fichero `.class` se ejecute en distintos sistemas operativos (Windows, Linux, Mac OS, Solaris), siempre que cada uno tenga su propia JVM instalada. Este es el principio de "escribe una vez, ejecuta en cualquier lugar" de Java (fuente: TD_01_01.md).

## Como compilar y ejecutar el primer programa

Para escribir, compilar y ejecutar un programa Java se necesita un editor de texto y el [[td1-command-prompt|Command Prompt]] (fuente: TD_01_03.md):

1. Escribir el codigo fuente y guardarlo con el nombre `NombreClase.java`. El nombre del fichero debe coincidir exactamente con el nombre de la clase definida dentro.
2. Abrir el Command Prompt y navegar hasta el directorio donde esta el fichero.
3. Compilar con `javac NombreClase.java`. Esto genera el fichero `NombreClase.class`.
4. Ejecutar con `java NombreClase` (sin extension).

Ejemplo:

```java
class PrimerPrograma {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

Comandos:

```
javac PrimerPrograma.java
java PrimerPrograma
```

Resultado: `Hello, World!` (fuente: TD_01_03.md)

## Construccion incremental de un programa Java

Para entender el papel de cada elemento, es util construir el programa desde cero, paso a paso (fuente: TD_01_04.md):

1. **Fichero vacio**: `A.java` completamente vacio compila sin errores pero no genera `.class` ni produce salida.
2. **Clase vacia**: `class A {}` ya genera `A.class` al compilar. Sin embargo, intentar ejecutarlo con `java A` produce un error porque no existe el metodo main.
3. **Main obligatorio**: Java requiere la firma exacta `public static void main(String[] args)` para que una clase sea ejecutable. Con el metodo main vacio, el programa compila y ejecuta sin errores ni salida.
4. **Con System.out.println**: anadir esta instruccion dentro del main produce la salida visible en pantalla.

La clase es el contenedor obligatorio, el metodo main es el punto de entrada obligatorio de ejecucion, y `System.out.println` es la instruccion que produce salida visible (fuente: TD_01_04.md).

## Nota sobre PATH

La variable de entorno PATH se configura mas adelante, al trabajar con Servlets. Si el JDK ya esta instalado y anadido al PATH por defecto del sistema, caso habitual en un ordenador personal, no es necesario modificar el PATH para las primeras practicas (fuente: TD_01_03.md). En equipos donde el JDK no esta en una ubicacion estandar del sistema, como ocurria en los ordenadores de las aulas de la universidad con el JDK instalado en una unidad de red, si hace falta definir el PATH manualmente antes de compilar (ver [[td1-practica-compilar-java|Ejercicio 1.0]]).

## Paginas relacionadas

- [[td1-command-prompt]]
- [[td1-programas-basicos-java]]
- [[td4-packages]]
- [[td5-historia-de-la-computacion]]
