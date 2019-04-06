# Implementar la función organizar_estudiantes() que tome como parámetro una lista de Estudiantes
# y devuelva un diccionario con las carreras como keys, y la cantidad de estudiantes en cada una de ellas como values.

from practico_02.ejercicio_04 import Estudiante


def organizar_estudiantes(estudiantes):
    count1=count2=count3=count4=0
    for i in estudiantes:
        if (i.c=="Ingenieria en sistemas"):
            count1+=1
        elif(i.c=="Ingenieria quimica"):
            count2+=1
        elif(i.c=="Ingenieria mecanica"):
            count3+=1
        else:
            nueva_carre=i.c
            count4+=1
            if(nueva_carre == None):
                nueva_carre="Otras"
    dicci={"Ingenieria en sistemas":count1,"Ingenieria quimica":count2,"Ingenieria mecanica":count3, "Otras":count4}

    return dicci

est1=Estudiante("Ingenieria en sistemas",4,42,25)
est2=Estudiante("Ingenieria en sistemas",3,42,8)
est3=Estudiante("Ingenieria quimica",4,35,20)
est4=Estudiante("Ingenieria mecanica",3,39,12)
est5=Estudiante("Ingenieria quimica",2,35,5)

estudiantes=[est1,est2,est3,est4,est5]

diccionario=organizar_estudiantes(estudiantes)
print(diccionario)
assert (diccionario=={'Ingenieria en sistemas': 2, 'Ingenieria quimica': 2, 'Ingenieria mecanica': 1, 'Otras': 0})
