from figura_geometrica import FiguraGeometrica
from color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
        
    def area(self):
        return self.get_alto() * self.get_ancho()
        
    def __str__(self):
        return f'{super().__str__()}, color: {self.get_color()}, area: {self.area()}'
    
    
# Rectangulo1 = Rectangulo(2, 4, "Azul")
# print(Rectangulo1)

# print(Rectangulo1.area())
# print(Rectangulo1.get_alto())
# print(Rectangulo1.get_ancho())
# print(Rectangulo1.get_color())