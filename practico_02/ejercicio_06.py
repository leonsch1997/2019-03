# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

from datetime import date
class Persona:

    # nacimiento es un objeto datetime.datetime
    def __init__(self, nacimiento):
        self.fecha_nac=nacimiento

    def edad(self):
        naci=self.fecha_nac
        hoy = date.today()
        año = naci.year
        mes = naci.month
        dia = naci.day

        fecha = naci
        edad = 0
        while fecha <= hoy:
            edad += 1
            fecha = date(año+edad, mes, dia)
        return (edad-1)


per=Persona(date(1997, 3, 2))
print(per.edad())
assert (per.edad()==22)

