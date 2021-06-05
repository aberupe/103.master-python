cantantes = ['2pac','Drake','Bad bunny','Julio Iglesias']
numeros = [1,2,5,8,3,4]

#ordenar la lista de numeros
print(numeros)

numeros.sort()
print(numeros)

#añadir elementos
cantantes.append("natos y Waor")
cantantes.insert(1, "David Bisbal")
print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove('Bad bunny')
print(cantantes)

#Dar la vuelta
print(numeros)
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('Drake' in cantantes)

#contar elementos
print(cantantes)
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#conseguir indice
print(cantantes.index("Drake"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)