import os
import shutil

# crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("Ya existe el directorio")
"""
# copiar
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

shutil.copytree(ruta_original, ruta_nueva)
"""

# eliminar carpeta
# os.rmdir('./mi_carpeta_copiada')
# os.rmdir('./mi_carpeta')

# listar contenido
print("contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")

for fichero in contenido:
    print("Fichero: " + fichero)
