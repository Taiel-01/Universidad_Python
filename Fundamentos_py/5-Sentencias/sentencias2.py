condicion = True

print("Condición verdadera") if condicion else print("Condicion Falsa") 
if condicion:
    print("La condición es verdadera")
else:
    print("La condición es falsa")
    
numero = int(input("Proporciona un número entre 1 y 3:"))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de rango"
    
print("numero proporcionado:", numeroTexto)