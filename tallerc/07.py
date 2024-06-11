#7 Escribe un algoritmo que elimine todos los elementos negativos de una lista de números.

lista = [1, -2, 3, -4, 5, -6]
lista = lista
for i in lista:
    if i <0:
       lista.remove(i)
print("lista sin negativos: ",lista)  
 