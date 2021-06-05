"""
Modulos: son funcionalidades ya hechas para reutilizar
En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/es/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lengiaje,
modulos en internet y tambien podemos crear nuestrois modulos.

"""

#Importar modulo propio
import mimodulo

#Importar una funcion de mimodulo
from mimodulo import holaMundo

#Importar toda las funciones de mi modulo
from mimodulo import *

print(mimodulo.holaMundo("Victor Robles Web"))

print(mimodulo.calculadora(3, 5, True))

# modulo de fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Fecha_personalizada " + fecha_personalizada)


print(datetime.datetime.now().timestamp())

# modulo matematicas
import math

print("Raiz cuadradade 10: ", math.sqrt(10))

print("Numero PI: ", float(math.pi))

print("Redondear -: ", math.floor(6.56798))
print("Redondear +: ", math.ceil(6.56798))

#Modulo random
import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))