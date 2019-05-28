# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine, inspect
from sqlalchemy.orm import sessionmaker

base = declarative_base()
engine = create_engine('sqlite:///practico_03A.db')
base.metadata.bind = engine

class Persona(base):
    __tablename__ = 'persona'
    id_persona = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)
    fecha_nacimiento = Column(DateTime, nullable=False)
    dni = Column(Integer, nullable=False)
    altura = Column(Integer)


def crear_session():
    db_session = sessionmaker()
    db_session.bind = engine
    session = db_session()


def crear_tabla(nombre_clase_tabla):
    ins = inspect(engine)
    t_exists = False
    for t in ins.get_table_names():
        if t == nombre_clase_tabla.__tablename__:
            t_exists = True
    if t_exists == False:
        nombre_clase_tabla.__table__.create()


def borrar_tabla(nombre_clase_tabla):
    ins = inspect(engine)
    t_exists = False
    for t in ins.get_table_names():
        if t == nombre_clase_tabla.__tablename__:
            t_exists = True
    if t_exists == False:
        nombre_clase_tabla.__table__.drop()


crear_session()


# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla(Persona)
        func()
        borrar_tabla(Persona)
    return func_wrapper
