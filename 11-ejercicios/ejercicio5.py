"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla
ACCION  AVENTURA            DEPORTES
GTA     ASSASINS            FIFA 21
COD     CRASH               Pro 21
PUGB    Prince of persia    MOTO GP 21

Mostrar esta informacion ordenada
"""

tabla = [
    {
        "categoria": "ACCION",
        "juegos": ["GTA", "Call Of Duty", "PUGB"]
    },
    {
        "categoria": "AVENTURA",
        "juegos": ["ASSASINS", "CRASH", "Prince of persia"]      
    },
    {
        "categoria": "DEPORTES",
        "juegos": ["FIFA 21", "Pro 21", "MOTO GP 21"]    
    }
]

for categoria in tabla:
    print(f"-------------{categoria['categoria']} ----------")
    for juego in categoria['juegos']:
        print(juego)