# Ejercicio 21: Crear una lista de listas donde cada sublista contenga tres números consecutivos, luego sumar los elementos de cada sublista y mostrar tanto las sublistas como sus sumas.

listaListas=[[1,2,3],[4,5,6],[7,8,9]]
# s1,s2,s3 = sum(listaListas[0]), sum(listaListas[1]), sum(listaListas[2])
# print(f"La suma de {listaListas[0]} Es: {s1}, La suma de {listaListas[1]} Es: {s2}, La suma de {listaListas[2]} Es: {s3}")

listaSumas =[]
for sublista in listaListas:
    sumaSubLista=0
    for num in sublista:
        sumaSubLista=sumaSubLista+num
    listaSumas.append(sumaSubLista)      
    print(f"la Suma de {sublista} Es {sumaSubLista}")    
print("nueva lista ",listaSumas)    
