Documentacion de Java y de Servlets

Resumen: explica como navegar la documentacion oficial de Java SE y la de los servlets (Java EE), y la diferencia entre interfaces y clases al consultar HttpServletRequest y HttpServletResponse.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 8 - Servlets y clases/TD_08_04.md

Ultima actualizacion: 2026-06-25

## Navegar la documentacion oficial de Java SE

La documentacion oficial de la API de Java (Java Platform, Standard Edition) muestra en su panel izquierdo todos los packages disponibles. Al seleccionar uno (por ejemplo, java.lang), se muestran sus clases e interfaces; al seleccionar una clase concreta (por ejemplo, la clase System), se muestran sus variables miembro, constructores y metodos. Dentro de la clase System se encuentran las variables in y out, los objetos sobre los que habitualmente se escribe (out) o se lee (in) en los programas Java; el tipo de out es PrintStream, una clase sobre la que se pueden invocar metodos de escritura (fuente: TD_08_04.md).

## Donde se encuentra la documentacion de los servlets

La documentacion de los [[td7-servlets|servlets]] se encuentra en un lugar distinto a la documentacion estandar de Java, porque los servlets forman parte de una extension de Java orientada a aplicaciones empresariales (Java EE), no del nucleo basico del lenguaje (Java SE). Esta extension tiene un numero de packages bastante mas extenso, entre los que se encuentra javax.servlet. El package que define que es un servlet, y que se utiliza en este curso, es javax.servlet.http; las clases e interfaces usadas en los ejemplos del curso son HttpServlet, HttpServletRequest y HttpServletResponse (fuente: TD_08_04.md).

## Interfaces frente a clases

HttpServletRequest y HttpServletResponse son tecnicamente interfaces, no clases: una interfaz declara que metodos debe tener cualquier clase que la implemente, pero no proporciona directamente el codigo de esos metodos, que aportan los distintos implementadores. A efectos practicos, sin embargo, se comportan de forma muy similar a una clase, sobre todo porque en este curso se utiliza la implementacion de Apache Tomcat de estas interfaces, ya completamente implementada: se reciben objetos de estos tipos como parametros del metodo doGet, sin necesidad de preocuparse de los detalles de su implementacion interna (fuente: TD_08_04.md).

## Consultar los metodos heredados

Al consultar la documentacion de HttpServletResponse, se ve la lista de sus metodos propios. Si se busca un metodo concreto (por ejemplo, getWriter) y no aparece entre los metodos propios de esa interfaz, puede encontrarse entre los metodos heredados de otra interfaz de la que esta deriva. El metodo getWriter devuelve un objeto de tipo PrintWriter; para conocer sus propiedades hay que consultar la documentacion de Java SE, ya que PrintWriter pertenece al package java.io, no a los servlets. Alli se encuentra la lista completa de sus metodos, entre los que estan println y otros usados en los ejemplos del curso (fuente: TD_08_04.md).

## Idea clave sobre como usar la documentacion

Cuando se trabaja con clases o interfaces que no se conocen en detalle, la documentacion oficial permite localizar exactamente que metodos estan disponibles, que argumentos requieren y que devuelven, y de que paquete o libreria proviene cada elemento, ya sea del nucleo del lenguaje (Java SE) o de una extension especifica como los servlets (Java EE) (fuente: TD_08_04.md).

## Paginas relacionadas

- [[td7-servlets]]
- [[td7-parametros-en-servlets]]
