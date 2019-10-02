
# Create and activate the virtual environment

py -3 -m venv .venv
.venv\scripts\activate

If the activate command generates the message "Activate.ps1 is not digitally signed. You cannot run this script on the current system.", then you need to temporarily change the PowerShell execution policy to allow scripts to run (see About Execution Policies in the PowerShell documentation):

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Lineamientos para entrega de trabajos prácticos


## Repositorio

Crear un fork de este repositorio en Github siguiendo el siguiente formato de nombre "frro-soporte-YYYY-NN"

donde
- `YYYY`: año de cursado
- `NN`: número de grupo

Ejemplo:
```
frro-soporte-2018-07
```

En las settings del proyecto, se deben agregar los siguientes perfiles como colaboradores:

- Franr (Francisco Rivera)
- mac3333 (Mario Castagnino)
- ealuque (Ernesto Luque)

## Trabajos Prácticos

Cada trabajo práctico se desarrollara netamente sobre una rama. La rama base sera "master" (por defecto).

La entrega del trabajo práctico es un Pull Request contra "master". Se deben agregar a los colaboradores del punto anterior como revisores de la Pull Request una vez el trabajo practico listo.

Se considera el trabajo aprobado y listo para mergeo una vez que el profesor apruebe la Pull Request.

El nombre de cada rama debera seguir el siguiente formato "practico-NN"

donde
- `NN`: número de trabajo práctico

Ejemplo:
```
practico-05
```
