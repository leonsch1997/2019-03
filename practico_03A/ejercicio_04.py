# Implementar la funcion buscar_persona, que devuelve el registro de una persona basado en su id.
# El return es una tupla que contiene sus campos: id, nombre, nacimiento, dni y altura.
# Si no encuentra ningun registro, devuelve False.

import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session
from practico_03A.ejercicio_02 import agregar_persona


def buscar_persona(id_persona):
    session = crear_session()
    persona_buscada = session.query(Persona).get(id_persona)
    if persona_buscada is None:
        return False
    else:
        persona_tupla = (persona_buscada.id_persona,
                         persona_buscada.nombre,
                         persona_buscada.fecha_nacimiento,
                         persona_buscada.dni,
                         persona_buscada.altura)
    return persona_tupla


@reset_tabla
def pruebas():
    juan = buscar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert juan == (1, 'juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    assert buscar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
