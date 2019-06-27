# Implementar un modelo Socio a traves de Alchemy que cuente con los siguientes campos:
# - id_socio: entero (clave primaria, auto-incremental, unico)
# - dni: entero (unico)
# - nombre: string (longitud 250)
# - apellido: string (longitud 250)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, inspect

Base = declarative_base()

class Socio(Base):
    __tablename__ = 'socios'
    id_socio = Column(Integer, primary_key=True, unique=True)
    dni = Column(Integer)
    nombre = Column(String(250))
    apellido = Column(String(250))

    def __repr__(self):
        return f"<User(id_socio='{self.id_socio}', " \
            f"dni={self.dni}, " \
            f"nombre='{self.nombre}', " \
            f"apellido='{self.apellido}')>"


