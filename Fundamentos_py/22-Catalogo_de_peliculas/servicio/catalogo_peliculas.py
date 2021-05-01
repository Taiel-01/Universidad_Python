import os 

class CatalogoPeliculas:
    ruta_archivo = "peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            #a - modo append
            archivo = open(CatalogoPeliculas.ruta_archivo, "a")
            archivo.write(pelicula.__str__() + "\n")
        except Exception as e:
            print(f'Ocurrio una exepcion al agregar: {e}')
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo, "r")
            print("Catalogo de peliculas:")
            print(archivo.read())
        except Exception as e:
            print(f'Ocurrio una error al listar peliculas: {e}')
        finally:
            archivo.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print(f'archivo eliminado: {CatalogoPeliculas.ruta_archivo}')
        except Exception as e:
            print(f'Ocurrio un error al eliminar peliculas: {e}')