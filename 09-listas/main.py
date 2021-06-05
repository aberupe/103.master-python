"""
Listas (arrays)
Son colecciones o conjuntos e datos / valores, bajo un unico nombre.
para acceder a esos valores podemos usar un indice numerico.

"""

pelicula = "Batman"
#definir lista
peliculas = ["Batman","Spiderman","El señor de los anillos"]
cantantes = list(('2pac','Drake','Jelop'))
years = list(range(2020,2050))
variada = ["victor", 30, 4.4, True, "texto"]

print(peliculas)
print (cantantes)
print(years)
print (variada)

#Indices
pelicula ="otra cosa"
peliculas[1]="Gran torino"
peliculas[2]="El Hobbit"


print (peliculas[1])
print(pelicula[-2])
print(cantantes[0:1])
print(peliculas[1:])

#Añadir elementos a la lista
cantantes.append("Kase O")
print(cantantes)

#Recorrer listas


#añadimos nueva pelicula a la lista
nueva_pelicula=""
while nueva_pelicula != "parar":
    nueva_pelicula=input("Introduce la nueva pelicula. ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

print("\n***************Listado de Peliculas***************")
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")

#Listas multidimendionales
print("\n ********Listado de Contactos **********")
contactos = [
    [
        'Antonio',
        'antonio@correo.com'
    ],
    [
        'Luis',
        'luis@luis.com'
    ],
    [
        'salvador',
        'salvador@salva.com'
    ]
]

#mostrar los nombres
for contacto in contactos:
    print(contacto[0])

#mostrar nombres y correo
for contacto in contactos:
    for elemento in contacto:
        print(elemento)

#mostrar nombres y correo
for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: "+ elemento)
        else:
            print("Email: "+ elemento)
    print("\n")

#mostrar correo de Luis
print(contactos[1][1])

