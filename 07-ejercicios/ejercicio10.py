"""
Ejercicio 10: Hacer un programa que pida la nota de 15 alumnos
y mostrar en pantalla cuantos aprobados y cuantos suspendidos

"""

contador = 1
aprobados = 0
suspendidos = 0

numero_alumnos = int(input("¿Cuantos alumnos tienes?: "))

while contador <= numero_alumnos:
    nota = int(input(f"¿Que nota quieres ponerle al \"alumno {contador}\"?: "))
    
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

    contador += 1
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos suspendidos: {suspendidos}")