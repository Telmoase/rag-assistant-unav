La clase Vector en Java

Resumen: explica la limitacion de tamano fijo de los arrays, y como la clase Vector de java.util permite almacenar colecciones de objetos que crecen automaticamente, con un ejemplo completo usando addElement, size y elementAt.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_05.md, Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_06.md

Ultima actualizacion: 2026-06-24

## La limitacion de los arrays

Para contener varios elementos del mismo tipo se puede usar un [[td3-objetos-y-referencias|array]]. Los arrays son comodos para este tipo de operaciones, pero tienen una limitacion importante: hay que definir su tamano antes de utilizarlos. Hay casos en los que ese tamano no se conoce de antemano, por ejemplo si el usuario va introduciendo elementos mientras el programa se ejecuta. Se podria gestionar esto manualmente (comprobar cuando el array se llena, crear otro mas grande, copiar los elementos antiguos), pero seria una labor tediosa de programar cada vez (fuente: TD_04_05.md).

## La clase Vector como alternativa

Java ofrece clases de utilidad para resolver este problema, disponibles en el package java.util (ver [[td4-packages]]). Una de ellas es Vector, que permite almacenar una coleccion de objetos sin necesidad de fijar su tamano de antemano: crece automaticamente segun se le van anadiendo elementos (fuente: TD_04_05.md).

## Declarar un Vector de un tipo concreto

Vector indica entre simbolos de angulo que tipo de objetos va a contener. Por ejemplo, para declarar un vector de objetos String (fuente: TD_04_05.md):

```java
Vector<String> vs = new Vector<String>();
```

Tras esta sentencia, vs ya es un objeto Vector de String, aunque todavia no contiene ningun elemento.

## Los tres metodos basicos

- **addElement(objeto)**: anade un objeto al vector. Se puede repetir tantas veces como se quiera para ir anadiendo mas elementos.
- **size()**: no necesita argumentos, y devuelve un numero entero con la cantidad de elementos que contiene actualmente el vector.
- **elementAt(posicion)**: recupera el elemento en la posicion indicada (empezando a contar desde 0).

(fuente: TD_04_05.md)

```java
vs.addElement("Matthew");
int n = vs.size();
String l = vs.elementAt(0);
```

Combinando size() y elementAt() se puede construir un bucle que recorra todos los elementos del vector (fuente: TD_04_05.md):

```java
for (int i=0; i<vs.size(); i++) {
    System.out.println("Element " + i + ": " + vs.elementAt(i));
}
```

## Programa de ejemplo completo

```java
import java.util.Vector;
public class UseVector{
    public static void main(String[] args) {
        Vector<String> vs = new Vector<String>();
        vs.addElement("Matthew");
        vs.addElement("Mark");
        vs.addElement("Luke");
        vs.addElement("John");
        System.out.println("Size: " + vs.size());
        for (int i=0; i<vs.size(); i++) {
            System.out.println("Element " + i + ": " + vs.elementAt(i));
        }
    }
}
```

(fuente: TD_04_06.md)

Primero se declara y crea un Vector de String llamado vs con el constructor por defecto. Despues se anaden cuatro elementos llamando a addElement cuatro veces. A continuacion se imprime el tamano con size(), que en este punto devuelve 4. Finalmente, un bucle for recorre todas las posiciones desde 0 hasta una posicion menor que vs.size(), recuperando cada elemento con elementAt(i) (fuente: TD_04_06.md).

Resultado esperado:

```
Size: 4
Element 0: Matthew
Element 1: Mark
Element 2: Luke
Element 3: John
```

(fuente: TD_04_06.md)

## Idea clave

De los muchos metodos que ofrece Vector segun su documentacion oficial, este patron usa solo tres: addElement, size y elementAt. Son suficientes para sustituir el patron tipico de uso de un array cuando no se conoce de antemano cuantos elementos se van a necesitar, y el mismo patron se aplica a vectores de cualquier otro tipo de objeto, cambiando unicamente el tipo indicado entre los simbolos de angulo (fuente: TD_04_06.md).

## Paginas relacionadas

- [[td3-objetos-y-referencias]]
- [[td4-packages]]
- [[td4-practica-packages-herencia]]
