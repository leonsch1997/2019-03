# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03.ejercicio_01 import reset_tabla, crear_conexion
from practico_03.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    cSQL = """SELECT IdPersona, Nombre, FechaNacimiento, Dni, Altura 
              FROM Persona 
              WHERE (IdPersona = ?)"""
    dato = (id_persona,)
    with crear_conexion() as db:
        cursor = db.cursor()
        exists = cursor.execute(cSQL, dato).fetchone()

        if exists is None:
            return False
        else:
            return exists


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', str(datetime.datetime(1988, 5, 15)), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()

