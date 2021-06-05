"""
Local: Definida dentro de la funcion y no
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return.

Globales: Definidas fuera de la funcion y estan disponibles
dentro y fuera de ella.

"""

frase = ("Hola Peru")

print (frase)

def holaMundo():
    frase = "Hola Mundo"
    print ("Dentro de la funcion")
    print (frase)

    year = 2021
    print (year)

    global website
    website="gemba.pe"
    print("DENTRO: ", website)

    return "dato devuelto: " + str(year)

print(holaMundo())
print("Fuera: ", website)
