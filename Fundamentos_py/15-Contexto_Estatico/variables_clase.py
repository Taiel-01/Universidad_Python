class MiClase:
    variable_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        

objeto1 = MiClase("Variable instancia")

# # !NO Podemos acceder a las variables de clase 
# # ?con el nombre de las clases
# print(MiClase.variable_instancia)

# *Podemos acceder a las variables de instancia 
# ?desde los objetos
print(objeto1.variable_instancia)

# *Podemos acceder a las variables de clase 
# ?con el nombre de las clases
print(MiClase.variable_clase)

# *Podemos acceder a las variables de clase 
# ?desde los objetos
print(objeto1.variable_clase)


# podemos acceder a la modificacion desde la clase
# pero al acceder desde el objeto vemos el valor original
# la modificacion se asocia a la clase
MiClase.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia)
print(objeto1.variable_instancia)

objeto1.variable_instancia = "Modificando variable de instancia"
print(MiClase.variable_instancia)
print(objeto1.variable_instancia)


# MiClase.variable_clase = "Modificando variable de clase"
# print(MiClase.variable_clase)
# print(objeto1.variable_clase)

# objeto1.variable_clase = "Modificando variable de clase"
# print(MiClase.variable_clase)
# print(objeto1.variable_clase)