#2 Escribe un algoritmo que calcule el producto de todos los elementos impares de una lista de números enteros.

lista = [1, 2, 3, 4, 5, 6]

acum=1
for i in lista:
    if i%2 != 0:
        acum=acum*i

print(f"el producto de los numeros impares es {acum}")        