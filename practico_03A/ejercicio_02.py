# Implementar la funcion agregar_persona, que inserte un registro en la tabla Persona
# y devuelva los datos ingresados el id del nuevo registro.

import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session


def agregar_persona(nombre, fecha_nacimiento, dni, altura):
    nueva_persona = Persona()
    nueva_persona.nombre = nombre
    nueva_persona.fecha_nacimiento=fecha_nacimiento
    nueva_persona.dni=dni
    nueva_persona.altura=altura
    session = crear_session()
    session.add(nueva_persona)
    session.commit()
    return nueva_persona.id_persona


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    id_marcela = agregar_persona('marcela gonzalez', datetime.datetime(1980, 1, 25), 12164492, 195)
    assert id_juan > 0
    assert id_marcela > id_juan


if __name__ == '__main__':
    pruebas()
