#1 crear una lista
lista = [1,2,3,4,5]
print(lista)

#2 acceder al tercer elemento

print(lista[3])

#3 modificar el segundo elemento de la lista

lista[1]=10
print(lista[1])

#4 usa append para agregar el unmero 6 al final de la lista

lista.append(6)
print(lista)


#5 elimina un elemento por valor

lista.remove(10)
print(lista)

#6 Eliminar un elemento por index
del lista[0]
print(lista)

#7 mostrar la longitud de la lista

print("longitud de la lista: ",len(lista))

#8 extender la lista

lista.extend([7,8,9])
print(lista)

#9 insertar un elemento

lista.insert(0,2)
print(lista) 

#10 limpiar la lista

lista.clear()
print(lista)