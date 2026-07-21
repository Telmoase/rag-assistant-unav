Variables y metodos static en Java

Resumen: explica el significado de la palabra reservada static aplicada a variables y metodos, las reglas de acceso entre miembros static y de instancia, y la convencion de nombres para constantes.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_01.md

Ultima actualizacion: 2026-06-24

## El significado de static

La palabra reservada static se puede aplicar tanto a variables como a metodos de una clase, y en ambos casos indica que ese elemento pertenece a la clase en si, no a cada objeto individual creado a partir de ella (fuente: TD_04_01.md).

## Variables static (variables de clase)

En la clase [[td3-definicion-de-clases|Circulo]], las variables x, y, r no son static: cada objeto tiene su propia copia, con valores independientes. En cambio, numCirculos si esta declarada como static:

```java
static int numCirculos = 0;
```

Esto significa que numCirculos no pertenece a ningun objeto Circulo en particular, sino a la clase Circulo como conjunto: existe una unica copia compartida por todos los objetos, y ya existe (con su valor inicial) incluso antes de crear ningun objeto. Cada vez que se crea un nuevo Circulo, el constructor incrementa esta variable compartida con `numCirculos++;` (fuente: TD_04_01.md).

## Constantes: static junto con final

Otro uso habitual de static, combinado con final, es definir constantes. En Circulo, PI esta declarada asi:

```java
public static final double PI=3.14159265358979323846;
```

final indica que el valor no puede modificarse una vez asignado; al ser tambien static, existe una unica copia de PI compartida por todos los circulos, lo cual tiene sentido porque no habria motivo para que cada circulo tuviese su propio valor independiente de pi. Las variables static se referencian dentro de la clase usando directamente su nombre, como ocurre en el metodo perimetro(), que usa PI sin ninguna cualificacion adicional (fuente: TD_04_01.md).

Por convencion, las constantes (variables static final) se escriben enteramente en mayusculas, separando palabras con guion bajo si el nombre tiene varias, por ejemplo MIN_WIDTH o MAX_WIDTH (fuente: TD_04_01.md).

## Metodos de instancia frente a metodos static

Los metodos de instancia (los que no son static) se aplican siempre sobre un objeto concreto: al invocar c1.perimetro(), el calculo usa el radio r del objeto c1 en particular, y el resultado depende de sobre que objeto se invoque. La clase Circulo tiene tambien un metodo static llamado elMayor, que recibe dos circulos como argumentos y los compara sin invocarse sobre ningun objeto concreto. Este metodo no usa this ni depende de ningun objeto, porque toda la informacion que necesita le llega como argumentos, por lo que se puede llamar de la forma mas parecida a una funcion global (fuente: TD_04_01.md).

Conceptualmente, un metodo static que no utiliza ninguna variable de instancia podria definirse incluso fuera de la clase, ya que no depende de ningun estado particular de un objeto; se mantiene dentro de la clase por motivos organizativos, para agrupar la funcionalidad relacionada (fuente: TD_04_01.md).

## Reglas de acceso entre miembros static y de instancia

- Los metodos de instancia pueden acceder directamente tanto a variables y metodos de instancia como a variables y metodos static.
- Los metodos static solo pueden acceder directamente a variables y metodos static. Para acceder a una variable o metodo de instancia desde un metodo static, es necesario hacerlo a traves de una referencia a un objeto concreto.
- Los metodos static no pueden usar this, porque this hace referencia al objeto actual, y un metodo static no se ejecuta sobre ningun objeto en particular.

(fuente: TD_04_01.md)

## Paginas relacionadas

- [[td3-definicion-de-clases]]
- [[td4-modificadores-de-acceso]]
- [[td4-practica-clases-algoritmos]]
