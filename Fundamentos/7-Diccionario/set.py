# set es una colección sin orden y sin índices,
# no permite elementos repetidos y los elementos no
# pueden modificar, pero si agregar nuevos o eliminar

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# largo
print(len(planetas))

# revisar si un elemento esta presente
print("Marte" in planetas)

# agregar
planetas.add("Tierra")
print(planetas)
planetas.add("Tierra")  # no se pueden agregar elementos duplicados
print(planetas)

# eliminar con remove posiblemente arroja una exepción
planetas.remove("Tierra")
print(planetas)

# elimitar con discard no arroja exepción
planetas.discard("Jupiter")
print(planetas)

# limpiar el set
planetas.clear()
print(planetas)

# eliminar el set
del planetas
print(planetas)
