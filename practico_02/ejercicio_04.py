# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from datetime import datetime
from practico_02.ejercicio_03.py import Persona

class Estudiante(Persona):

    def __init__(self, nombre, edad, sexo, peso, altura, carrera, anio, cantidad_materias, cantidad_aprobadas):
        super().__init__(nombre, edad, sexo, peso, altura)
        self.c=carrera
        self.a=anio
        self.cm=cantidad_materias
        self.ca=cantidad_aprobadas

    def avance(self):
        cant_mate=100/self.cm
        porcent_aprob=cant_mate*self.ca
        return(round(porcent_aprob,2))


    # implementar usando modulo datetime
    def edad_ingreso(self):
        dt=datetime.now()
        edad_ing= self.e - (dt.year - self.a)
        return edad_ing

estu=Estudiante("Mauro",28,'H',85,185,"Ingenieria en Sistemas de Información",2015,42,21)
print("tiene un ",estu.avance(),"% de la carrera aprobada")
assert (estu.avance()==50)
edad_año=estu.edad_ingreso()
print("ingreso  con ",edad_año," años")
assert(edad_año==24)
