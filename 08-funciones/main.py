"""
Funciones:
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando
la funcion tantas veces como sea necesario.

def nombreFuncion (parametros):
    #Bloque / conjunto de instrucciones

#Para ejecutar
nombreFuncion (mi_parametro)


"""
"""
#Ejemplo 1

print("##### Ejemplo 1 #####")

#Definir funcion
def muestraNombre():
    print("Victor")
    print("Paco")
    print("Juan")
    print("Francisco")
    print("Aitor")
    print("Nestor")
    print("\n")

# Invocar funcion
muestraNombre()
muestraNombre()
muestraNombre()


#ejemplo 2
print("##### Ejemplo 2 #####")


def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")

    if edad >= 18:
        print("Y eres mayor de edad")
    
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))


mostrarTuNombre (nombre, edad)


#ejemplo 3
print("##### Ejemplo 3 #####")

def tabla (numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range (11):
        operacion = numero * contador
        print(f"{numero} x {contador} = {operacion}")


tabla(3)


#ejemplo 3.1
print("##### Ejemplo 3.1 #####")

for numero_tabla in range (1, 11):
    tabla(numero_tabla)

"""
#ejemplo 4
print("\n##### Ejemplo 4 #####")
#Parametros opcionales

def getEmpleado(nombre, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Abel Rosales",42434385)

#ejemplo 5
print("\n##### Ejemplo 5 #####")
#Parametros opcionales y return o devolver datos

def saludame (nombre):
    saludo = f"Hola saludos {nombre}"

    return saludo

print (saludame ("Abel Rosales"))

#ejemplo 6
print("\n##### Ejemplo 6 #####")

def calculadora (numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas!= False:
        cadena +="Suma: " + str(suma)
        cadena += "\n"
        cadena +="Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena +="Multiplicacion: " + str(multiplicacion)
        cadena += "\n"
        cadena +="Division: " + str(division)
        cadena += "\n"

    return cadena

print (calculadora(5, 5, True))

#ejemplo 7
print("\n##### Ejemplo 7 #####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo (nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Abel", "Rosales"))
#print(getNombre("Abel"), getApellidos("Rosales"))

#ejemplo 8 Funciones lambda
print("\n##### Ejemplo 8 #####")

dime_el_year = lambda year: f"El año es {year * 50}"

print(dime_el_year(2034))
