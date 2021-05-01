#archivo = open("C:\\Users\\Taiel\\Desktop\\universidad-python\\prueba.txt", "r")
archivo = open("prueba.txt", "r")
#print(archivo.read())


#*leer algunos caracteres
# print(archivo.read(5))
# print(archivo.read(3))


#*leer lineas completas
# print(archivo.readline())
# print(archivo.readline())


#*iterando
# for linea in archivo:
#     print(linea)


#*leer lineas
# print(archivo.readlines()[2])


#*abrimos un nuevo archivo
#*Con el parametro de a anexamos informacion al archivo
# archivo2 = open("copia.txt", "a")
archivo2 = open("copia.txt", "w")
archivo2.write(archivo.read())

archivo.close()
archivo2.close()