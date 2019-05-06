# Implementar la funcion borrar_persona, que elimina un registro en la tabla Persona. 
# Devuelve un booleano en base a si encontro el registro y lo borro o no. 
 
import datetime 
from practico_03.ejercicio_01 import reset_tabla, crear_conexion
from practico_03.ejercicio_02 import agregar_persona
 
 
def borrar_persona(id_persona): 
    cSQL= """SELECT IdPersona 
             FROM Persona 
             WHERE (IdPersona = ?)"""
    cSQL2="""DELETE 
             FROM Persona 
             WHERE (IdPersona=?)"""
    dato= (id_persona,) 
    with crear_conexion() as db: 
        cursor = db.cursor() 
        exists = cursor.execute(cSQL, dato).fetchone() 
 
        if exists is None: 
            return False 
        else: 
            cursor.execute(cSQL2, dato)
            return True
 
 
 
@reset_tabla 
def pruebas(): 
    borrar_persona(12345) 
    assert borrar_persona(agregar_persona('juan perez', datetime.datetime(1988, 5, 15), 32165498, 180))
    assert borrar_persona(12345) is False 
 
if __name__ == '__main__': 
    pruebas() 
