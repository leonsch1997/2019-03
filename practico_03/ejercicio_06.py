# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from practico_03.ejercicio_01 import reset_tabla, crear_conexion, crear_tabla, borrar_tabla


def crear_tabla_peso():
    cSQL = """CREATE TABLE IF NOT EXISTS 
               PersonaPeso(
               idPeso INTEGER PRIMARY KEY, 
               idPersona INTEGER ,
               fecha TEXT ,
               peso INTEGER, 
               FOREIGN KEY (idPersona) REFERENCES Persona(idPersona)
               ) """

    with crear_conexion() as db:
        cursor = db.cursor()
        cursor.execute(cSQL)
        db.commit()


def borrar_tabla_peso():
    cSQL = 'DROP TABLE IF EXISTS PersonaPeso'

    with crear_conexion() as db:
        cursor = db.cursor()
        cursor.execute(cSQL)
        db.commit()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla()
    return func_wrapper
