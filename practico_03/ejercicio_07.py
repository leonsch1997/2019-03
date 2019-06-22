# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from practico_03.ejercicio_01 import reset_tabla, crear_conexion
from practico_03.ejercicio_02 import agregar_persona
from practico_03.ejercicio_04 import buscar_persona
from practico_03.ejercicio_06 import reset_tabla

def fecha_ultimo_peso(id_persona):

    cSQL = """SELECT MAX(PersonaPeso.fecha)
              FROM Persona
              JOIN PersonaPeso
              ON PersonaPeso.idPersona = Persona.idPersona
              WHERE Persona.idPersona = ?;"""
    datos = (id_persona,)

    with crear_conexion() as db:
        cursor = db.cursor()
        ultima_fecha = cursor.execute(cSQL, datos).fetchone()[0]

        if ultima_fecha is None:
            return None
        else:
            return ultima_fecha


def agregar_peso(id_persona, fecha, peso):

    cSQL = """INSERT into PersonaPeso (idPersona, fecha, peso) VALUES(?, ?, ?)"""
    datos = (id_persona, fecha, peso)
    ultima_fecha = fecha_ultimo_peso(id_persona)
    exists = buscar_persona(id_persona)

    with crear_conexion() as db:
        cursor = db.cursor()

        if exists is False:
            return False
        elif not(ultima_fecha is None) \
        and fecha < datetime.datetime.strptime(ultima_fecha, '%Y-%m-%d %H:%M:%S'):
            return False
        else:
            cursor.execute(cSQL, datos)
            id_peso = cursor.lastrowid
            return id_peso


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
    # id incorrecto
    assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
    # registro previo al 2018-05-26
    assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    pruebas()

