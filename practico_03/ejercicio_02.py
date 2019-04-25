# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from practica_03ejercicio_01 import reset_tabla, crear_conexion

db=crear_conexion()


def agregar_persona(nombre, nacimiento, dni, altura):
    SQL='INSERT into Persona (Nombre, FechaNacimiento, Dni, Altura) VALUES(?, ?, ?, ?)'
    datos=(nombre,nacimiento,dni,altura)

    with crear_conexion() as db:
        cursor = db.cursor()
        cursor.execute(SQL, datos)
        IdPersona = cursor.lastrowid
        db.commit()

    return IdPersona

@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan

if __name__ == '__main__':
    pruebas()

