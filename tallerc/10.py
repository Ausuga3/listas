#Escribe un algoritmo que divida una lista en dos partes iguales. Si la lista tiene un número impar de elementos, la primera parte debe tener un elemento más que la segunda.

lista = [1, 2, 3, 4, 5]
mitad = len(lista) //2

if len(lista) %2 != 0:
    mitad += 1

lista1 = lista[:mitad]
lista2 = lista[mitad:]
print("Primera parte:", lista1)
print("Segunda parte:", lista2)
