#17 Escribe un algoritmo que elimine los elementos en posiciones impares de una lista.

lista = [1, 2, 3, 4, 5, 6, 7, 8]
# enumerate(lista) devuelde dos datos, almacena en i el indice del elemento y en valorDelIndex el valor del elemento
lista_pares = [valorDelIndex for i, valorDelIndex in enumerate(lista) if i % 2 == 0]
print("Lista sin elementos en posiciones impares:", lista_pares)