
# Implementar la clase Persona que cumpla las siguientes condiciones:
# Atributos:
# - nombre.
# - edad.
# - sexo (H hombre, M mujer).
# - peso.
# - altura.
# Métodos:
# - es_mayor_edad(): indica si es mayor de edad, devuelve un booleano.
# - print_data(): imprime por pantalla toda la información del objeto.
# - generar_dni(): genera un número aleatorio de 8 cifras y lo guarda dentro del atributo dni.

import random
class Persona:

    def __init__(self, nombre, edad, sexo, peso, altura):
        self.n=nombre
        self.e=edad
        self.s=sexo
        self.p=peso
        self.a=altura
        self.dni= self.generar_dni()

    def es_mayor_edad(self):
        if(self.e>=18):
            return True
        else:
            return False

    # llamarlo desde __init__
    def generar_dni(self):
        dni=random.randint(00000000,99999999)
        return dni

    def print_data(self):
        print(self.n,self.e,self.s,self.dni,self.p,self.a)
        return[self.n,self.e,self.s,self.dni,self.p,self.a]

perso=Persona("Marcela",48,'M',65,185)
print(perso.es_mayor_edad())
assert(perso.es_mayor_edad()==True)
datos_per=perso.print_data()
assert(datos_per==["Marcela",48,'M',datos_per[3],65,185])
