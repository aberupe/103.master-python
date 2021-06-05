"""
# Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instrucciones
SI NO:
    Se ejecutaran otro grupo de instrucciones

if condicion:
    instrucciones
else
    otras instrucciones

#Operadores de comparacion
== igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

#Operadores logicos
and Y
or O
! negacion
not NO

"""
"""
# Ejemplo 1
print("########## EJEMPLO 1 ############")

color="rojo"
#color = input("Adivina cual es mi color favorito: ")

if color=="rojo":
    print("Enhorabuena!!")
    print("El color es ROJO")
else:
    print("El color es incorrecto")


# Ejemplo 2
print("\n########## EJEMPLO 2 ############")

#year =2020
year = int(input("¿En que año estamos?: "))
if year < 2021:
    print("Estamos antes de 2021 !!")
else:
    print("Es un año posterior a 2021")

# Ejemplo 3
print("\n########## EJEMPLO 3 ############")

nombre = "Abel Rosales"
ciudad = "Lima"
continente = "Oceania"
edad = 24
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad !!")

    if continente != "America":
        print ("El usuario no es Americano")
    else:
        print(f"Es Americano y de {ciudad}")
else:
    print(f"{nombre} NO es mayor de edad")


# Ejemplo 4
print("\n########## EJEMPLO 4 ############")

#dia = 1
dia = int(input("Introduce el numero del dia de la semana: "))

if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de semana")


if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
else:
    print("Es fin de semana")

"""

# Ejemplo 5
print("Ejemplo 5")
edad_minima = 18
edad_maxima = 65
edad_oficial = 17

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")


    #Ejemplo 6
print("Ejemplo 6")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")

        #Ejemplo 7
print("Ejemplo 7")

pais = "España"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} NO es un pais de habla hispana")
else:
    print(f"{pais} SI es un pais de habla hispana")