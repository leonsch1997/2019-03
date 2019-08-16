# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.
import sqlite3

def crear_conexion():
    return sqlite3.connect('base.db')

def crear_tabla():

    cSQL = """
      CREATE TABLE IF NOT EXISTS 
      Persona(
          IdPersona INTEGER PRIMARY KEY,
          Nombre TEXT(25),
          FechaNacimiento TEXT,
          Dni INTEGER,
          Altura INTEGER
        )
    """

    with crear_conexion() as db:
        cursor = db.cursor()
        cursor.execute(cSQL)
        db.commit()


def borrar_tabla():
    cSQL = 'DROP TABLE IF EXISTS Persona'

    with crear_conexion() as db:
        cursor = db.cursor()
        cursor.execute(cSQL)
        db.commit()

# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper


    




# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
