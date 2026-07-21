Modificadores de acceso en Java

Resumen: describe los cuatro niveles de acceso de Java (public, protected, sin modificador y private), su efecto sobre la visibilidad de variables y metodos, y las recomendaciones generales sobre cuando usar cada uno.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 4 - Librerias, herencia y API de Java/TD_04_07.md

Ultima actualizacion: 2026-06-24

## Los cuatro niveles de acceso

Java define modificadores de acceso que controlan quien puede acceder a una clase, o a las variables y metodos de una clase (fuente: TD_04_07.md):

- **public**: cualquier otra clase puede acceder al metodo o variable.
- **protected**: el acceso esta permitido dentro del mismo package, y tambien desde subclases (ver [[td4-herencia]]) aunque esten en un package distinto.
- **sin modificador** (package-private): el acceso esta permitido unicamente dentro del mismo package, sin importar si la clase que accede es una subclase o no.
- **private**: el acceso esta restringido unicamente a la propia clase donde se define el miembro.

## Ejemplos contrastados: Circulo y Complex

En la clase [[td3-definicion-de-clases|Circulo]], tanto la clase en si como sus variables miembro, constructores y metodos estan declarados con public, lo que significa que cualquier otra clase puede acceder a ellos libremente. En cambio, en la clase Complex, las variables miembro re e im estan declaradas con private (fuente: TD_04_07.md):

```java
private final double re;
private final double im;
```

Esto significa que solo el codigo de la propia clase Complex puede acceder directamente a estas variables. Desde fuera de la clase no es posible leer o modificar re o im directamente; el unico modo de obtener esa informacion desde fuera es a traves de metodos publicos que la propia clase decida exponer, como re() e im() (fuente: TD_04_07.md).

## Por que declarar variables como private

Declarar las variables miembro como private es una forma de proteger el estado interno de un objeto, evitando que codigo externo pueda modificarlas directamente sin pasar por la logica de la propia clase. En el caso de Complex, esto refuerza la inmutabilidad de la clase: si re e im fuesen public, cualquier codigo externo podria intentar modificarlas directamente, aunque al ser tambien final esa modificacion fallaria igualmente en tiempo de compilacion (fuente: TD_04_07.md).

## Tabla de visibilidad segun el nivel de acceso

| Modificador | Misma clase | Mismo package | Subclase en otro package | Cualquier clase |
|---|---|---|---|---|
| public | Si | Si | Si | Si |
| protected | Si | Si | Si | No |
| sin modificador | Si | Si | No | No |
| private | Si | No | No | No |

(fuente: TD_04_07.md)

## Recomendaciones generales

- Usar el nivel de acceso mas restrictivo que tenga sentido para cada miembro: por defecto conviene usar private, salvo que haya una buena razon para no hacerlo.
- Evitar declarar variables como public, salvo en el caso de constantes. Tener variables publicas ata el codigo a una implementacion concreta y limita la flexibilidad para cambiarla mas adelante.

En las clases vistas hasta ahora en el curso se ha optado principalmente por public y private, dejando de lado protected y el nivel sin modificador, ya que en general no hay necesidad de restringir el acceso de forma mas fina en estos ejemplos (fuente: TD_04_07.md).

## Paginas relacionadas

- [[td3-definicion-de-clases]]
- [[td4-herencia]]
- [[td4-static]]
