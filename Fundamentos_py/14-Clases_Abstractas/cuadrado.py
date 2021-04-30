from figura_geometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def area(self):
        return self.get_alto() * self.get_ancho() 
        
    def __str__(self):
        return f'{super().__str__()}, color: {super().get_color()}, area: {self.area()}'

# Cuadrado1 = Cuadrado(4, "rojo")
# print(Cuadrado1)

# print(Cuadrado1.area())
# print(Cuadrado1.get_alto())
# print(Cuadrado1.get_ancho())
# print(Cuadrado1.get_color())

