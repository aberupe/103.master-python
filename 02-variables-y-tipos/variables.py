""" Una variable es un contenedor de informacion
que dentro guradara un dato, se pueden crear
muchas variables y que cada una tenga un dato dsitinto.
"""
# Crear variables y asignarles un valor
texto ="Máster en Python"
texto2="Con Abel Rosales"
numero =1
decimal = 6.7
# Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print ("--------------------")
#Sustituir el valor de algunas variables
numero = 77
decimal = 8.9


print(numero)
print(decimal)

# Concatenación
nombre="Abel"
apellido="Rosales"
web="gemba.pe"

print (nombre + " " + apellido + " - " + web)

print (f"{nombre} {apellido} - {web}")

print ("Hola me llamo {} {} y mi web es: {}".format(nombre, apellido, web))

print(nombre, apellido, web)