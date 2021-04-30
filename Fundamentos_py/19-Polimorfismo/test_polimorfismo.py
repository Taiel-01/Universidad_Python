from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(objeto):
    print(objeto)
    print(objeto, end="\n\n")
    print(objeto.departamento)
    if isinstance(objeto, Gerente):
        print(objeto.departamento)
        
empleado = Empleado("Juan", 1000.00)
imprimir_detalles(empleado)

empleado = Gerente("Karla", 2000.00, "Sistemas")
imprimir_detalles(empleado)