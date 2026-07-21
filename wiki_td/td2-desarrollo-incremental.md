Desarrollo incremental en Java

Resumen: tecnica de programacion que consiste en construir un programa en pequenos pasos verificados, usando variables intermedias y codigo de andamiaje temporal para detectar errores en el momento en que se introducen.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 2 - Variables y sentencias de control/TD_02_05.md

Ultima actualizacion: 2026-06-24

## Por que desarrollar de forma incremental

Un error habitual al programar es escribir mucho codigo de golpe antes de compilarlo y ejecutarlo, lo que despues obliga a invertir mucho tiempo depurando errores que podrian haberse detectado antes. El desarrollo incremental se basa en tres principios (fuente: TD_02_05.md):

1. Empezar con un programa que funcione y hacer pequenos cambios incrementales. Si aparece un error, lo mas probable es que este en el cambio mas reciente.
2. Usar variables para guardar valores intermedios, de forma que se puedan comprobar con instrucciones de impresion o con un depurador.
3. Una vez que el programa funciona, se pueden consolidar varias sentencias en expresiones compuestas, pero solo si eso no dificulta la lectura del codigo.

## Ejemplo: calculo de la distancia entre dos puntos

Para ilustrar el desarrollo incremental se usa un metodo que calcula la distancia euclidea entre dos puntos `(x1, y1)` y `(x2, y2)` (fuente: TD_02_05.md).

### Paso 1: el esqueleto del metodo (stub)

Antes de implementar nada, se define la firma del metodo y se anade un retorno provisional solo para que el codigo compile:

```java
public static double distance
        (double x1, double y1, double x2, double y2) {
    return 0.0;
}
```

Se compila en esta fase para detectar errores de sintaxis desde el principio.

### Paso 2: probar con valores conocidos

Se invoca el metodo desde `main` con valores cuyo resultado se conoce de antemano. Por ejemplo, los puntos `(1.0, 2.0)` y `(4.0, 6.0)` dan una diferencia horizontal de 3.0 y vertical de 4.0, por lo que el resultado esperado es 5.0 (triangulo 3-4-5). Conocer la respuesta correcta antes de programar es necesario para poder verificar cada paso (fuente: TD_02_05.md).

### Paso 3: calcular las diferencias con impresion de comprobacion

```java
public static double distance
        (double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    System.out.println("dx is " + dx);
    System.out.println("dy is " + dy);
    return 0.0;
}
```

Las instrucciones `System.out.println` temporales se llaman scaffolding (andamiaje): ayudan a construir el programa pero no forman parte de la version final (fuente: TD_02_05.md).

### Paso 4: elevar al cuadrado y sumar

```java
public static double distance
        (double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    double dsquared = dx * dx + dy * dy;
    System.out.println("dsquared is " + dsquared);
    return 0.0;
}
```

Con los valores de ejemplo, `dsquared` deberia valer 25.0. Se usa `dx * dx` en lugar de una funcion de potencia por simplicidad y eficiencia (fuente: TD_02_05.md).

### Paso 5: calcular la raiz cuadrada y devolver el resultado

Una vez verificados todos los valores intermedios, se anade el calculo final y se eliminan las instrucciones de andamiaje:

```java
public static double distance
        (double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    double dsquared = dx * dx + dy * dy;
    double result = Math.sqrt(dsquared);
    return result;
}
```

## Idea clave

En cada paso se compila y ejecuta el programa, comprobando que el valor intermedio coincide con el esperado antes de anadir el siguiente fragmento. Si en algun momento aparece un error, lo mas probable es que este en las lineas recien anadidas, lo que facilita mucho la deteccion y correccion de fallos (fuente: TD_02_05.md).

## Paginas relacionadas

- [[td1-compilacion-java]]
- [[td2-estilo-de-codigo-java]]
- [[td2-tipos-y-variables]]
- [[td3-depuracion-de-programas]]
