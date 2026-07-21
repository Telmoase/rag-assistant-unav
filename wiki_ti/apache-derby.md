# Apache Derby y la herramienta ij

**Resumen**: Apache Derby es un gestor de bases de datos relacional embebido en Java. La herramienta ij permite ejecutar sentencias SQL interactivamente desde la línea de comandos usando el driver JDBC de Derby.

**Asignatura**: Tecnología de la Información

**Fuentes**: Raw/Tecnologia de la informacion/Tema 6 - SQL/Step 2_ ij Basics.md

**Última actualización**: 2026-05-19

---

## Qué es Apache Derby

Apache Derby es un gestor de bases de datos relacional escrito en Java que puede funcionar de forma embebida dentro de una aplicación o como servidor independiente. Se usa en el curso como entorno de práctica de SQL alternativo a [[microsoft-access|Access]] (fuente: Step 2_ ij Basics.md).

## La herramienta ij

`ij` es la herramienta interactiva de scripting SQL incluida con Apache Derby. Permite ejecutar sentencias SQL directamente desde la línea de comandos usando el driver JDBC de Derby (fuente: Step 2_ ij Basics.md).

Para iniciarla:

```bash
java org.apache.derby.tools.ij
```

## Crear y conectar a una base de datos

```sql
-- Crear una base de datos nueva (create=true la crea si no existe)
ij> connect 'jdbc:derby:MyDbTest;create=true';

-- Conectar a una base de datos existente
ij> connect 'jdbc:derby:MyDbTest';

-- Con ruta completa
ij> connect 'jdbc:derby:/home/bill/databases/MyDbTest';
```

Derby crea un directorio con el nombre de la base de datos y un fichero `derby.log` para errores (fuente: Step 2_ ij Basics.md).

## Sentencias SQL básicas

Cada sentencia debe terminar con punto y coma (fuente: Step 2_ ij Basics.md):

```sql
ij> CREATE TABLE derbyDB(num INT, addr VARCHAR(40));
ij> INSERT INTO derbyDB VALUES (1956, 'Webster St.');
ij> INSERT INTO derbyDB VALUES (1910, 'Union St.');
ij> UPDATE derbyDB SET num=180, addr='Grand Ave.' WHERE num=1956;
ij> SELECT * FROM derbyDB;
```

## Desconectarse y salir

```sql
ij> disconnect;
ij> exit;
```

El comando `exit` cierra ij y, en modo embebido, apaga la base de datos Derby (fuente: Step 2_ ij Basics.md).

## Ejecutar scripts SQL

Desde dentro de ij, o directamente desde la línea de comandos (fuente: Step 2_ ij Basics.md):

```sql
ij> run 'mi_fichero.sql';
```

```bash
java org.apache.derby.tools.ij mi_fichero.sql
```

## Páginas relacionadas

- [[sql-select]]
- [[microsoft-access]]
- [[ti6-sql]]
