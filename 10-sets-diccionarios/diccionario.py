"""
Diccionario:
Es un tipo de dato que almacena un conjunto de datos:
En formato clave > valor.
Es parecido a un array asociativo o un ojbeto json.
"""

persona={
    "nombre": "Victor",
    "apellidos": "Robles",
    "web": "victorrobles.web"
}

print(persona)
print(persona["apellidos"])


#lista de diccionarios

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@web.com'
    },
    {
        'nombre': 'Luis',
        'email': 'luis@luis.com'
    },
    {
        'nombre': 'Salvador',
        'email': 'salvador@salva.com'
    }
]

contactos[0]['nombre']="Antoñito"

print(contactos[0]['nombre'])

print("\n Listado de contactos: ")
print("-----------------------")

for contacto in contactos:
    print(f"Nombre de contacto: {contacto['nombre']}")
    print(f"Email de contacto: {contacto['email']}")
    print("-----------------------")