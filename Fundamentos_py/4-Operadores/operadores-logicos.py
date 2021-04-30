# a = input("Proporciona un valor")
a = 3
valorMinimo = 0
valorMaximo = 5
dentroRango = (a >= valorMinimo and a <= valorMaximo)
#print(dentroRango)
if(dentroRango):
    print("dentro de rango")
else:
    print("fuera de rango")
    
    
vacaciones = False
diaDescanso = False
if(not(vacaciones or diaDescanso)):
    print("Tienes deberes que hacer")
else:
    print("Puedes ir al parque")
    
print(not(vacaciones))