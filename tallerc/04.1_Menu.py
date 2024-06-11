

i=True

while i:

    opc=int(input("eliga opcion 1, 2, 3 o 4 para salir\n: "))


    if opc == 1:    
        lista = [1, 2, 3, 4, 5, 6]
        acum=1
        acumulador =0
        for i in lista:
            if i %2 ==0:
                acumulador=acumulador +i
            else:
                acum=acum *i     
        print(f"la suma de los numero pares es {acumulador} y el producto de  los impares es {acum}")   

    elif opc == 2:

        lista = [1, 2, 3, 4, 5, 6]

        acum=1
        for i in lista:
            if i%2 != 0:
                acum=acum*i

        print(f"el producto de los numeros impares es {acum}")    

    elif opc ==3:
        lista1 = [1, 2, 3, 4, 5]
        lista2 = [4, 5, 6, 7, 8]

        comunes = list(set(lista1) & set(lista2))
        print(f"los comunes son {comunes}")    

    elif opc ==4:
        print("Adios")
        i=False 

