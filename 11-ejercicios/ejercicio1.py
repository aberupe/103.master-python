"""
Ejercicio 1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- recorrer la lista y mostrarla
- Hacer una funcion que recorra listas de numeros y devuelva un string
- ordenarla y mostrarla
- mostrar su longitud
- buscar algun elemento (que el usuario pida por teclado)
"""

# crear la lista
numeros = [13, 64, 52, 73, 21, 7, 91, 63]

# recorrer y mostrar
print("####### Recorrer y Mostrar #######")
for numero in numeros:
    print(numero)

# Crear funcion que recorra y devuelva string
print("####### Funcion y devuelve string #######")


def mostrarlista(lista):
    resultado = ""
    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"
    return resultado


print(mostrarlista(numeros))

# Ordenar y mostrarla
print("####### Ordenar y mostrar #######")
numeros.sort()
print(numeros)

# Longitud y mostrarla
print("####### Mostrar longitud #######")
print(len(numeros))

try:
    # Buscar algun elemento
    print("####### Buscar elemento en la lista #######")
    busqueda = int(input("Introduce el Número: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el Número: "))
    else:
        print(f"Has introducido el {busqueda}")
    print(f"######Buscar en la lista el numero  {busqueda} #######")

    search = numeros.index(busqueda)

    print(f"El número buscado existe en la lista, es el indice:  {search}")
except:
    print("El numero no esta en la lista, lo siento.")
