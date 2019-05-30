# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona.
# Devuelve un booleano en base a si encontro el registro y lo borro o no.

import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session
from practico_03A.ejercicio_02 import agregar_persona


def borrar_persona(id_persona):
    session = crear_session()
    persona_buscada = session.query(Persona).get(id_persona)
    if persona_buscada is None:
        print("Persona no encontrada")
        return False
    else:
        session.delete(persona_buscada)
        session.commit()
        print("Persona borrada: ID", persona_buscada.id_persona, " ", persona_buscada.nombre)
    return True


@reset_tabla
def pruebas():
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False

if __name__ == '__main__':
    pruebas()
