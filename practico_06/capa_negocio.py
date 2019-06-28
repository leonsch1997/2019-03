# Implementar los metodos de la capa de negocio de socios.

from practico_05.ejercicio_01 import Socio
from practico_05.ejercicio_02 import DatosSocio


class DniRepetido(Exception):
    def dni_repe(self,dniingresado):
        for t in Socio.dni:
            if t.dni == NegocioSocio.buscar_dni(dniingresado):
                print("ya existe una persona con ese dni")
            else:
                print("dni valido")


class LongitudInvalida(Exception):
    def long_invalid(self,nom,ape,carac_min,carac_max):
        if len(nom)<= carac_min:
            print("nombre ingresado muy corto")
            return True
        if len(nom)>= carac_max:
            print("nombre ingresado muy largo")
            return True
        if len(ape)<= carac_min:
            print("apellido ingresado muy corto")
            return True
        if len(ape)>= carac_max:
            print("apellido ingresado muy largo")
            return True
        if len(nom)>carac_min and len(ape)>carac_min and len(nom)<carac_max and len(ape)<carac_max:
            return False


class MaximoAlcanzado(Exception):
    def maxi(self,maximo):
        cont=0
        for t in Socio.id_socio:
            cont+=1
        if cont<=maximo:
            print("todo bien")
            return False
        else:
            print("supero el maximo")
            return True


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """     
        return DatosSocio.buscar(id_socio)

    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """
        return DatosSocio.buscar_dni(dni_socio)

    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        return DatosSocio.todos()


    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """
        nuevosocio=DatosSocio.alta(socio)
        if self.regla_1(nuevosocio):
            if self.regla_2(nuevosocio):
                if self.regla_3():
                    return True #alta realizada con exito
                else:
                    MaximoAlcanzado.maxi(NegocioSocio.MAX_SOCIOS)
            else:
                LongitudInvalida.long_invalid(nuevosocio.nombre,nuevosocio.apellido,NegocioSocio.MIN_CARACTERES,NegocioSocio.MAX_CARACTERES)
        else:
            DniRepetido.dni_repe(nuevosocio.dni)

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        return DatosSocio.baja(id_socio)

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        sociomodificado=DatosSocio.modificacion(socio)
        if self.regla_2(sociomodificado):
            return True   #Modificacion exitosa!!
        else:
            LongitudInvalida.long_invalid(sociomodificado.nombre,sociomodificado.apellido,NegocioSocio.MIN_CARACTERES,NegocioSocio.MAX_CARACTERES)


    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        
        try:
            if DatosSocio.buscar(socio.id_socio) == socio.id_socio:
                  if DniRepetido.dni_repe(socio.id_socio):
                      return True
                  else:
                    return False
        except(ValueError):
            print("no existe ese socio")
            
    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        try:
            if DatosSocio.buscar(socio.id_socio) == socio.id_socio:
                  if LongitudInvalida.long_invalid(socio.nombre,socio.apellido,self.MIN_CARACTERES,self.MAX_CARACTERES):
                      return True
                  else:
                      return False
        except(ValueError):
            print("no existe ese socio")


    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if MaximoAlcanzado.maxi(NegocioSocio.MAX_SOCIOS):
            return True
        else:
            return False

