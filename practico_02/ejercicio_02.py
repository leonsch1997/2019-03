# Implementar la clase Circulo que contiene un radio, y sus métodos area y perimetro.


import math
class Circulo:

    def __init__(self, radio):
        self.r=radio

    def area(self):
        ar=math.pi*self.r**2
        return ar

    def perimetro(self):
        per=math.pi*self.r*2
        return per
cir=Circulo(4)
print(round(cir.area(),2))
assert (round(cir.area(),2)==50.27)
print(round(cir.perimetro(),2))
assert (round(cir.perimetro(),2)==25.13)

