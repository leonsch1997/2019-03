# Implementar la funcion crear_tabla_peso, que cree una tabla PersonaPeso con:
# - IdPersona: Int() (Clave Foranea Persona)
# - Fecha: Date()
# - Peso: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, inspect
from sqlalchemy.orm import sessionmaker, relationship
from practico_03A.ejercicio_01 import reset_tabla, Persona, engine, crear_session, crear_tabla, borrar_tabla, base

# class PersonaPeso(base):
#     __tablename__ = 'PersonaPeso'
#     id_peso = Column(Integer, primary_key=True)
#     id_persona = Column(Integer, ForeignKey('Persona.id_persona'))
#     fecha_peso = Column(DateTime, nullable=False)
#     peso = Column(Integer, nullable=False)
#     to_persona = relationship(Persona, back_populates="to_personapeso")

def crear_tabla_peso():
    crear_tabla(PersonaPeso)


def borrar_tabla_peso():
    borrar_tabla(PersonaPeso)


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla(Persona)
        crear_tabla_peso()
        func()
        borrar_tabla_peso()
        borrar_tabla(Persona)
    return func_wrapper
