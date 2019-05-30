# Implementar la funcion listar_pesos, que devuelva el historial de pesos para una persona dada.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).

# Debe devolver:
# - Lista de (fecha, peso), donde fecha esta representado por el siguiente formato: AAAA-MM-DD.
#   Ejemplo:
#   [
#       ('2018-01-01', 80),
#       ('2018-02-01', 85),
#       ('2018-03-01', 87),
#       ('2018-04-01', 84),
#       ('2018-05-01', 82),
#   ]
# - False en caso de no cumplir con alguna validacion.

import datetime

from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session, crear_tabla, borrar_tabla, base
from practico_03A.ejercicio_06 import PersonaPeso
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona


def listar_pesos(id_persona):
    persona_buscada = buscar_persona(id_persona)
    if persona_buscada is not False:
        session = crear_session()
        pesos = session.query(PersonaPeso).filter(PersonaPeso.idPer == id_persona).all()
        if len(pesos) == 0:
            print("La persona no registra pesos")
            return False
        else:
            pesos_lista = []
            i = 1
            for peso in pesos:
                pesos_lista.append((peso.fecha_peso, peso.peso))
            return pesos_lista
    else:
        return False


@reset_tabla
def pruebas():
    id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
    agregar_peso(id_juan, datetime.datetime(2018, 5, 1), 80)
    agregar_peso(id_juan, datetime.datetime(2018, 6, 1), 85)
    pesos_juan = listar_pesos(id_juan)
    pesos_esperados = [
        ('2018-05-01', 80),
        ('2018-06-01', 85),
    ]
    assert pesos_juan == pesos_esperados
    # id incorrecto
    assert listar_pesos(200) == False


if __name__ == '__main__':
    pruebas()
