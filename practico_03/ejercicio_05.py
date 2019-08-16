# Implementar la funcion actualizar_persona, que actualiza un registro de una persona basado en su id.
# Devuelve un booleano en base a si encontro el registro y lo actualizo o no.

import datetime

from practico_03.ejercicio_01 import reset_tabla, crear_conexion
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona


def actualizar_persona(id_persona, nombre, nacimiento, dni, altura):
    cSQL = """UPDATE Persona
              SET nombre = ? , fechaNacimiento = ? , dni = ? , altura = ? 
              WHERE (IdPersona = ?)"""
    datos = (nombre, nacimiento, dni, altura, id_persona)
    exists = buscar_persona(id_persona)

    with crear_conexion() as db:
        cursor = db.cursor()

        if exists is False:
            return False
        else:
            cursor.execute(cSQL, datos)
            return True


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    actualizar_persona(id_juan, 'juan carlos perez', datetime.datetime(1988, 4, 16), 32165497, 181)
    assert buscar_persona(id_juan) == (id_juan, 'juan carlos perez', str(datetime.datetime(1988, 4, 16)), 32165497, 181)
    assert actualizar_persona(123, 'nadie', datetime.datetime(1988, 4, 16), 12312312, 181) is False

if __name__ == '__main__':
    pruebas()

