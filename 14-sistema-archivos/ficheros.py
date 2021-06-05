from io import open
import pathlib
import shutil

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+")

# escribir
archivo.write("**** Texto escrito desde python*****\n")

# cerrar archivo
archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# leer contenido
#contenido = archivo_lectura.read()
# for elemento in contenido:
# print(contenido)

# leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()


# for frase in lista:
#     print("- " + frase.upper())

# for frase in lista:
#     if frase.isnumeric():
#         print("- " + frase.upper())

# for frase in lista:
#     if frase.split():
#         print("- " + frase.capitalize())

for frase in lista:
    lista_frase = frase.split()
    # print(lista_frase)
    print(" "+frase.center(100))

# copiar fichero
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + \
    "/07-ejercicios/fichero_copiado77.txt"

shutil.copyfile(ruta_original, ruta_nueva)

# mover
