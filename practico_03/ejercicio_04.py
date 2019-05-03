# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practica_03ejercicio_01 import reset_tabla, crear_conexion
from practica_03ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    cSQL="""SELECT IdPersona, Nombre, FechaNacimiento, Dni, Altura FROM Persona WHERE (IdPersona = ?)"""
    dato= (id_persona,)
    with crear_conexion() as db:
        cursor = db.cursor()
        exists = cursor.execute(cSQL, dato).fetchone()

        if exists is None:
            return False
        fechaNaci=datetime.datetime.strptime(exists[2],'%Y-%m-%d %H:%M:%S')
        del exists[2]
        exists.insert(2,fechaNaci)
        return exists


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    print(juan)
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
