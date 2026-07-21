Herencia en Java

Resumen: explica el concepto de herencia entre clases mediante extends, y desarrolla el ejemplo completo de la clase Esfera, que hereda de Circulo y usa super para reutilizar su constructor.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_02.md, Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_03.md

Ultima actualizacion: 2026-06-24

## Que es la herencia

Uno de los conceptos centrales de la programacion orientada a objetos es la herencia: construir una clase que deriva de otra clase ya existente. Si se tiene una clase base, se puede definir otra clase derivada que herede de ella. La clase derivada tiene automaticamente todos los metodos y variables de la clase base, ademas de los que se definan especificamente en ella (fuente: TD_04_02.md).

## Declarar la herencia con extends

Para crear una nueva clase que derive de otra se utiliza la palabra reservada extends. Por ejemplo, para que una clase Esfera derive de [[td3-definicion-de-clases|Circulo]] (fuente: TD_04_02.md):

```java
class Esfera extends Circulo {
    ...
}
```

Aunque no se vuelvan a escribir explicitamente en la definicion de Esfera, esta clase ya tiene implicitas las variables x, y, r y metodos como perimetro(), simplemente por derivar de Circulo (fuente: TD_04_02.md).

## Anadir nuevas propiedades en la clase derivada

Una vez heredadas las propiedades de la clase base, se le pueden anadir variables y metodos propios, especificos de la clase derivada. Una esfera necesita una tercera coordenada z, ademas de x e y que ya hereda de Circulo, y un metodo nuevo volumen() que no tiene sentido para un circulo (fuente: TD_04_02.md):

```java
class Esfera extends Circulo {
    double z;

    double volumen() {
        ...
    }
}
```

Una clase que extiende a otra termina teniendo el conjunto de propiedades de la clase base, mas las propiedades nuevas anadidas en la derivada. La herencia permite reutilizar codigo ya escrito en la clase base, evitando repetir la definicion de variables y metodos comunes en cada nueva clase relacionada (fuente: TD_04_02.md).

## La clase Esfera completa

```java
public class Esfera extends Circulo {
    double z;
    Esfera(double x, double y, double z, double r) {
        super(x, y, r);
        this.z = z;
    }
    double volumen() {
        return 4./3.*Math.PI*r*r*r;
    }
    public static void main(String[] args) {
        Esfera e1 = new Esfera(3, 4, 5, 2);
        System.out.println(e1.volumen());
    }
}
```

(fuente: TD_04_03.md)

## El constructor y la palabra reservada super

El constructor de Esfera recibe cuatro argumentos (x, y, z, r). El primer paso es inicializar las propiedades heredadas de Circulo, y para eso se llama al constructor de la clase base usando la palabra reservada super:

```java
super(x, y, r);
```

super(...) funciona de forma parecida a this(...) (que llama a otro constructor de la misma clase), pero en este caso llama al constructor de la clase base, pasandole los argumentos que ese constructor espera. Esta llamada con super debe ser la primera linea del constructor. Una vez que super(x, y, r) ha inicializado las propiedades heredadas, el constructor completa la inicializacion asignando z (fuente: TD_04_03.md):

```java
this.z = z;
```

## El metodo volumen

volumen() no recibe ningun argumento, porque toda la informacion necesaria (el radio r, heredado de Circulo) ya esta disponible como variable miembro del propio objeto. Devuelve `4./3.*Math.PI*r*r*r`. Es importante escribir los numeros 4 y 3 con punto decimal (4. y 3.) para que Java los trate como valores double en la division, y no como una division entera que truncaria el resultado a 1 en lugar del valor decimal correcto de 4 dividido entre 3 (fuente: TD_04_03.md).

## Requisito para compilar: tener tambien la clase base

Para compilar Esfera es necesario que el fichero Circulo.java (o su version compilada, Circulo.class) este disponible en el mismo directorio. Si no esta presente, el compilador da un error indicando que no encuentra la clase Circulo, ya que Esfera depende directamente de ella por la herencia (fuente: TD_04_03.md).

## Idea clave

La clase Esfera ilustra el patron general de una clase derivada: declara la herencia con extends, anade las variables y metodos propios que necesita, y en su constructor utiliza super(...) para reutilizar la logica de inicializacion ya definida en la clase base, en lugar de repetirla (fuente: TD_04_03.md).

## Paginas relacionadas

- [[td3-definicion-de-clases]]
- [[td4-practica-packages-herencia]]
- [[td4-static]]
