
#15 Escribe un algoritmo que genere una lista de números primos menores a 20.

primos=[]

for j in range(2, 20):
    es_primo = True
    if j <= 1:
        es_primo = False
    for i in range(2, j):
        if j % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(j)
 
print("Lista de números primos menores a 20:", primos)