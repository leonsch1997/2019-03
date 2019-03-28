# Implementar la clase Rectangulo que contiene una base y una altura, y el método area.


class Rectangulo:

    def __init__(self, base, altura):
        self.b=base
        self.h=altura

    def area(self):
        area=(self.b)*(self.h)
        return area



rec1=Rectangulo(8,5)
print(rec1.area())
