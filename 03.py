#15 crear lista de listas
superLista=[[1,2,3],[4,5,6],[7,8,9]]
print(superLista)

#16 acceder a elementos de sub listas
print("el primer elemento de la primera lista es: ",superLista[0][0])

#17 añdir sub lista
superLista.append([10,11,12])
print(superLista)

#18 fusionar dos listas en una 

lista1=[1,2,3]
lista2=[4,5,6]

lista1.extend(lista2)
print(lista1)