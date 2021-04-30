from producto import Producto
from orden import Orden

producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Panalon", 200.00)
producto3 = Producto("Calcetines", 50.00)

productos = [producto1, producto2]

orden1 = Orden(productos)
print(orden1)

# productos.append(producto3)
orden2 = Orden(productos)
orden2.agregar_producto(producto3)
print(orden2)
print(orden2.calcular_total())