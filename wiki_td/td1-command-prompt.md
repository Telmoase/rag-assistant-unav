Command Prompt en Windows

Resumen: descripcion del interprete de linea de comandos de Windows y los comandos esenciales para navegar por el sistema de ficheros, gestionar variables de entorno y usar utilidades de edicion en la consola.

Asignatura: Tecnologia Digital

Fuentes: Tecnologia Digital/Tema 1 - Java y Command Prompt/TD_01_02.md

Ultima actualizacion: 2026-06-24

## Que es el Command Prompt

El Command Prompt es el interprete de linea de comandos de Windows. Permite navegar por el sistema de ficheros y ejecutar programas escribiendo comandos de texto, en lugar de usar el explorador de ficheros con el raton (fuente: TD_01_02.md).

## Como abrir el Command Prompt

Hay dos formas (fuente: TD_01_02.md):

- Pulsar la tecla Windows y escribir `cmd` o `Command Prompt`.
- Ir al boton de inicio, entrar en *Windows System* y seleccionar *Command Prompt*.

## Comandos de navegacion

| Accion | Comando |
|---|---|
| Cambiar de unidad de disco | `C:` (letra de la unidad seguida de dos puntos) |
| Listar ficheros y directorios | `dir` |
| Cambiar de directorio | `cd folder_name` |
| Ir al directorio superior | `cd ..` |
| Ir a una ruta absoluta | `cd \absolute_path` |
| Crear un directorio | `mkdir folder_name` |
| Ver contenido de un fichero | `type folder_name` |
| Cerrar la ventana | `exit` |

El comando `cd` no cambia de unidad de disco. Para moverse a otra unidad hay que escribir primero la letra de la unidad (`D:`) y despues usar `cd` para navegar dentro de ella (fuente: TD_01_02.md).

## Variables de entorno

- Ver el contenido de una variable: `set variable_name`
- Definir el valor de una variable: `set variable_name=value`

(fuente: TD_01_02.md)

## Utilidades de edicion en la consola

- **Tab**: autocompletar nombres de fichero o carpeta; pulsar Tab otra vez muestra la siguiente coincidencia.
- **Flechas arriba/abajo**: recuperar comandos escritos anteriormente.
- **Seleccionar texto con el cursor**: copia automaticamente al portapapeles.
- **Boton derecho del raton**: pega el texto del portapapeles en la consola.
- **Copiar ruta desde el explorador**: haciendo clic derecho sobre la ruta en la cabecera del explorador de Windows, se puede copiar y pegar directamente despues de `cd `.

(fuente: TD_01_02.md)

## Paginas relacionadas

- [[td1-compilacion-java]]
- [[td1-programas-basicos-java]]
- [[td7-apache-tomcat]]
