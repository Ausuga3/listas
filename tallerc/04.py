#4 Escribe un algoritmo que elimine los primeros N elementos de una lista.
lista = [1, 2, 3, 4, 5, 6, 7, 8]

N=int(input("Cuantos numeros iniciales desea borrar?\n: "))
listaA= lista[N:]
lsitaB=lista[:N]
print(f"la lista eliminando los primeros {N} queda {listaA}, la lsita eliminando los ultimos {N} queda {lsitaB}")
