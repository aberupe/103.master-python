"""
Ejercicio 3. Programa que compruebe si una variable esta vacia
y si esta vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas
"""

texto = ""
if len(texto.strip()) <= 0:
   
   texto = "hola soy un texto en minusculas"
   print(texto.upper())

else:
    print("La variable tiene contenido {texto}")
