class FiguraGeometrica:
    def __init__(self, alto, ancho):
        self.__alto = alto
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def __str__(self):
        return f'alto: {self.__alto}, ancho: {self.__ancho}'


# Figura1 = FiguraGeometrica(2, 2)
# print(Figura1)
