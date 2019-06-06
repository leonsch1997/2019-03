from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Implementar la funcion crear_tabla, que cree una tabla Persona con:
# - IdPersona: Int() (autoincremental)
# - Nombre: Char(30)
# - FechaNacimiento: Date()
# - DNI: Int()
# - Altura: Int()

# Implementar la funcion borrar_tabla, que borra la tabla creada anteriormente.

Base = declarative_base() # Metadatos
engine=create_engine('sqlite:///sqlalchemy_ejemplo0.db')
Base.metadata.bind=engine

#---- creamos una sesión para admin datos
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

def crear_tabla():
    class Persona(Base):
        __tablename__='persona'
        IdPersona = Column(Integer, primary_key=True)
        Nombre = Column(String(30), nullable=False)
        FechaNacimiento= Column(String(30), nullable=False)
        DNI=Column(Integer, nullable=False)
        Altura=Column(Integer)
    Base.metadata.create_all(engine)



def borrar_tabla():
    Base.metadata.delete_table('Persona')
    




# no modificar
def reset_tabla(func):
    def func_wrapper():
        crear_tabla()
        func()
        borrar_tabla()
    return func_wrapper
