calificacion = int(input("proporciona un valor entre 0 y 10: "))

if calificacion >= 9 and calificacion <= 10:
    print("A")
elif calificacion >= 8 and calificacion < 9:
    print("B")
elif calificacion >= 7 and calificacion < 8:
    print("C")
elif calificacion >= 6 and calificacion < 7:
    print("D")
elif calificacion >= 0 and calificacion < 6:
    print("F")
else:
    print("Valor desconocido")