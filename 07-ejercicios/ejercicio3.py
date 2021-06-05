"""
Ejercicio 3: 
Escribir un programa que muestre los cuadrados
(un numero multiplicado por si mismo) de los 60 primeros
numeros naturales. Resolverlo con for y con while

"""

#while

contador = 0
while contador <= 60:

    cuadrado = contador * contador
    print(f"El cuadrado es {contador} es {cuadrado}")

    contador += 1

#for

for numero in range (61):

    cuadrado = numero * numero
    print(f"El cuadrado es {numero} es {cuadrado}")

    contador += 1
