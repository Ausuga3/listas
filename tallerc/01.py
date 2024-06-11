#1 Escribe un algoritmo que sume todos los elementos pares de una lista de números enteros.

lista = [1, 2, 3, 4, 5, 6]
acum=1
acumulador =0
for i in lista:
    if i %2 ==0:
        acumulador=acumulador +i
    else:
        acum=acum *i     
print(f"la suma de los numero pares es {acumulador} y el producto de  los impares es {acum}")        


