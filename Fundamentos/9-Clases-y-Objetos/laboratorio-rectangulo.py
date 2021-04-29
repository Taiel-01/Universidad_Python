# class Rectangulo:
    
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def area(self):
#         return self.base * self.altura
    
    
# rectangulo = Rectangulo(2, 2)
# print("El area del rectangulo es:", rectangulo.area())
# =====================================================================


class Rectangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
    
base = int(input("Proporciona la base:"))    
altura = int(input("Proporciona la altura:"))  
 
rectangulo = Rectangulo(base, altura)
print("El area del rectangulo es:", rectangulo.calcular_area())


        
