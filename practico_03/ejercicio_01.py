# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import sqlite3

db = sqlite3.connect(':memory:')

cursor = db.cursor()

def crear_tabla():
    cSQL = 'CREATE TABLE IF NOT EXISTS Persona(IdPersona INTEGER PRIMARY KEY ASC, Nombre TEXT(25), FechaNacimiento DATE(),' \
          'Dni INT(), Altura INT())'
    cursor.execute(cSQL)
    db.commit()

def borrar_tabla():
    cSQL = 'DROP TABLE IF EXISTS Persona'
    cursor.execute(cSQL)
    db.commit()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper

cursor.close()
db.close()
