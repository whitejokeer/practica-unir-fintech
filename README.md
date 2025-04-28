# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git y GitHub en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

## Ejemplo de Ejecución

### Paso 1: Crear un archivo de palabras
Crea un archivo llamado `words.txt` con el siguiente contenido:
```
gryffindor
slytherin
ravenclaw
hufflepuff
slytherin
gryffindor
```

### Paso 2: Ejecutar el programa
Para ejecutar el programa manteniendo palabras duplicadas:
```bash
python3 main.py words.txt no
```

Resultado esperado:
```
Se leerán las palabras del fichero words.txt
['gryffindor', 'gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin', 'slytherin']
```

Para ejecutar el programa eliminando duplicados:
```bash
python3 main.py words.txt yes
```

Resultado esperado:
```
Se leerán las palabras del fichero words.txt
['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
```

### Usando el Makefile
También puedes usar el comando predefinido en el Makefile:
```bash
make run
```
Este comando ejecutará la aplicación usando Docker, eliminando duplicados del archivo words.txt.

