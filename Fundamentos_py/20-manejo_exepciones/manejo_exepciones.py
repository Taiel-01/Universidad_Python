from numeros_identicos_exeption import NumerosIdenticosExeption

resultado = None
a = "10"
b = 0

try:
    a = int(input("Primer numero: "))
    b = int(input("Segundo numero: "))
    if a == b:
        raise NumerosIdenticosExeption("numeros identicos")
    resultado = a / b
# except ZeroDivisionError as e:
except ZeroDivisionError as e:
    print("Ocurrio un error con ZeroDivisionError", e)
    print(type(e))
except TypeError as e:
    print("Ocurrio un error con TypeError", e)
    print(type(e))
except Exception as e:
    print("Ocurrio un error con Exeption", e)
    print(type(e))
else: 
    print("No hubo ninguna excepcion")
finally:
    print("Fin del manejo de excepciones")

print("resultado: ", resultado)
print("continuamos...")