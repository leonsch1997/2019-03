# Implementar la funcion agregar_peso, que inserte un registro en la tabla PersonaPeso.
# Debe validar:
# - que el ID de la persona ingresada existe (reutilizando las funciones ya implementadas).
# - que no existe de esa persona un registro de fecha posterior al que queremos ingresar.

# Debe devolver:
# - ID del peso registrado.
# - False en caso de no cumplir con alguna validacion.

import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, inspect
from sqlalchemy.orm import sessionmaker, relationship
from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session, crear_tabla, borrar_tabla, base
from practico_03A.ejercicio_06 import PersonaPeso
from practico_03A.ejercicio_02 import agregar_persona
from practico_03A.ejercicio_04 import buscar_persona

def fecha_ultimo_peso(id_persona):
     session = crear_session()
     ultima_peso = session.query(PersonaPeso).join(Persona).\
         order_by(PersonaPeso.fecha_peso).first()
     return ultima_peso.fecha_peso


def agregar_peso(id_persona, fecha_peso, peso):
    nuevo_peso = PersonaPeso()
    nuevo_peso.id_persona = id_persona
    nuevo_peso.fecha_peso = fecha_peso
    nuevo_peso.peso = peso
    ultima_fecha = fecha_ultimo_peso(id_persona)
    exists = buscar_persona(id_persona)

    if exists is False:
        return False
    elif not(ultima_fecha is None) \
            and fecha_peso < datetime.datetime.strptime(ultima_fecha, '%Y-%m-%d %H:%M:%S'):
        return False
    else:
        session = crear_session()
        session.add(nuevo_peso)
        session.commit()
        return nuevo_peso.id_peso


# @reset_tabla
# def pruebas():
#     id_juan = agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180)
#     assert agregar_peso(id_juan, datetime.datetime(2018, 5, 26), 80) > 0
#     # id incorrecto
#     assert agregar_peso(200, datetime.datetime(1988, 5, 15), 80) == False
#     # registro previo al 2018-05-26
#     assert agregar_peso(id_juan, datetime.datetime(2018, 5, 16), 80) == False

if __name__ == '__main__':
    # pruebas()
    print(fecha_ultimo_peso(1))
