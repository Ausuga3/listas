#5 Escribe un algoritmo que genere una lista donde cada elemento sea el cubo de los números del 1 al 10.


lista=[]

for i in range(1,11):
    x=i**3
    lista.append(x)
print(lista)   