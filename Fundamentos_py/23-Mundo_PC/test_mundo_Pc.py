from orden import Orden
from computadora import Computadora
from monitor import Monitor 
from raton import Raton 
from teclado import Teclado

teclado_hp = Teclado("hp", "usb")
raton_hp = Raton("hp", "15 pulgadas")
monitor_hp = Monitor("hp", "15 pulgadas")
computadora_hp = Computadora("hp", monitor_hp, teclado_hp, raton_hp)

teclado_acer = Teclado("acer", "bluetooth")
raton_acer = Raton("acer", "bluetooth")
monitor_acer = Monitor("acer", "27 pulgadas")
computadora_acer = Computadora("acer", monitor_acer, teclado_acer, raton_acer)

teclado_gamer = Teclado("gamer", "bluetooth")
raton_gamer = Raton("gamer", "bluetooth")
monitor_gamer = Monitor("gamer", "47 pulgadas")
computadora_gamer = Computadora("gamer", monitor_gamer, teclado_gamer, raton_gamer)

computadora_armada = Computadora("armada", monitor_hp, teclado_acer, raton_gamer)

computadoras1 = [computadora_hp, computadora_acer]
orden1 = Orden(computadoras1)
orden1.agregar_computadora(computadora_gamer)
print(orden1)

computadoras2 = [computadora_gamer, computadora_armada, computadora_acer]
orden2 = Orden(computadoras2)
orden2.agregar_computadora(computadora_hp)
print(orden2)