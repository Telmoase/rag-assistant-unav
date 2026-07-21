Depuracion de programas en Java

Resumen: presenta la depuracion como una ciencia experimental, con una lista de verificacion practica, la tecnica de busqueda binaria del error, y la dimension emocional de depurar codigo propio.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 3 - Clases y objetos/TD_03_08.md

Ultima actualizacion: 2026-06-24

## Que es la depuracion

Disenar algoritmos y escribir codigo es una tarea dificil y propensa a errores. Por razones historicas, los errores de programacion se llaman bugs, y el proceso de localizarlos y corregirlos se llama depuracion (debugging) (fuente: TD_03_08.md).

## La depuracion como ciencia experimental

La depuracion se puede entender como una ciencia experimental: cuando se tiene una idea sobre que esta fallando, se modifica el programa y se vuelve a probar. Si la hipotesis era correcta, se puede predecir el resultado de la modificacion, acercandose un paso mas a un programa que funcione correctamente; si era incorrecta, hay que formular una nueva hipotesis y volver a intentarlo (fuente: TD_03_08.md).

## Programar y depurar deben ir de la mano

No conviene escribir mucho codigo de golpe y depurarlo todo despues por ensayo y error. Es mejor empezar con un programa que ya haga algo, aunque sea muy simple, e ir introduciendo pequenas modificaciones, depurando cada una a medida que se anade. De esta forma siempre se dispone de un programa que funciona, y resulta mas facil aislar los errores que van apareciendo. Este principio coincide con la idea de [[td2-desarrollo-incremental|desarrollo incremental]]: avanzar en pasos pequenos y verificables, en lugar de intentar resolver todo el problema de una sola vez (fuente: TD_03_08.md).

## Experimentar con los errores de forma deliberada

Una forma util de aprender a depurar es provocar errores a proposito mientras se experimenta con una caracteristica nueva del lenguaje; por ejemplo, en el programa Hello World, ver que ocurre si se olvida una comilla o se escribe mal println. Estos experimentos ayudan a recordar lo aprendido y a reconocer de antemano que significan los distintos mensajes de error del compilador. Es mejor cometer estos errores ahora, de forma intencionada, que mas adelante, de forma accidental (fuente: TD_03_08.md).

## La dimension emocional de la depuracion

Programar puede generar emociones intensas. Si se esta atascado con un error dificil de resolver, es normal sentir frustracion, desanimo o incluso verguenza. Conviene recordar que esto le ocurre a practicamente todos los programadores en algun momento, y que pedir ayuda a otra persona y hacer preguntas es una parte normal del proceso, no un signo de fracaso (fuente: TD_03_08.md).

## Lista de verificacion practica para depurar

Cuando un programa da problemas, conviene repasar estos puntos en orden hasta encontrar el problema (fuente: TD_03_08.md):

1. El programa compila.
2. El programa se ejecuta sin errores.
3. La ejecucion del programa corresponde realmente al codigo fuente que se cree estar ejecutando; para verificarlo se introduce una traza al principio, por ejemplo `System.out.println("Prog 1");`.
4. Se introduce una traza para verificar el valor de la variable mas importante, por ejemplo `System.out.println("i: " + i);`.
5. Se repite el paso anterior para todas las variables relevantes del programa.
6. Se introduce una traza para verificar que el programa llega hasta la mitad del codigo, por ejemplo `System.out.println("Point A");`.

## Busqueda binaria del error

Si la traza de la mitad del codigo se imprime, se repite el proceso para la siguiente mitad; si no se imprime, se repite para la mitad anterior. El objetivo de esta tecnica es encontrar exactamente la linea que causa el problema, dividiendo el codigo en mitades sucesivas (fuente: TD_03_08.md).

## Si el programa no compila

Si el problema es que el programa ni siquiera compila, los pasos son distintos (fuente: TD_03_08.md):

1. Leer el mensaje de error de compilacion y corregirlo directamente.
2. Si no se sabe como corregirlo, comentar la linea o lineas que producen el error, usando `//`.
3. Como alternativa, empezar desde un programa que si funcione (por ejemplo, Hello World) e ir anadiendo poco a poco las lineas del programa problematico, hasta que vuelva a aparecer el error.

El objetivo, igual que en el caso anterior, es encontrar la linea exacta que causa el error (fuente: TD_03_08.md).

## Paginas relacionadas

- [[td2-desarrollo-incremental]]
- [[td1-compilacion-java]]
