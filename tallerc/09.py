# Escribe un algoritmo que intercale los elementos de dos listas de igual longitud.
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]

listaIntercalada = [None]*(len(lista1) + len(lista2))
listaIntercalada[::2] = lista1
listaIntercalada[1::2] = lista2
print("Lista intercalada:", listaIntercalada)

