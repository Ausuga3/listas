


m=True
while m:

    opc=int(input("Eliga una opcion del 1 al 21, 21 para salir: "))
    if opc ==1:
        lista1=[1,2,3,4,5]
        sumLista1=sum(lista1)
        print("suma de la lista: ",sumLista1)

    elif opc ==2:
        producto=1
        for i in lista1:
            producto = producto*i
            
        print ("producto de la lista: ",producto)   

    elif opc ==3:
        lista2=[1, 2, 3, 4, 5, 3, 3]
        numRep=lista2.count(3)
        print("el numero 3 aparece: ",numRep)

    elif opc ==4:
        min= min(lista1)
        max= max(lista1)

        print(f"el numero menor es: {min} y el mayor es {max}")

    elif opc ==5:
        x=list(set(lista2))
        print("lista 2 sin duplicados: ",x)

    elif opc ==6:
        lista1[0],lista1[-1] = lista1[-1], lista1[0]
        print("lista 1 y ultimo numero invertido: ",lista1)


    elif opc ==7:
        sublista = lista1[1:4]
        sublista.reverse()
        lista1[1:4] = sublista

        print("sublista: ",sublista)


    elif opc ==8:
        pares=len([num for num in lista1 if num%2==0])
        impares=len([num for num in lista1 if num%2!=0])

        print(f"Numeros pares: {pares}, Numeros impares: {impares}")


    elif opc ==9:

        frutas = ["manzana", "banana", "cereza", "dátil", "fresa"]
        print("".join(frutas))

    elif opc ==10:
        mayores3=0
        for i in lista1:
            if i>3:
                print(f"{i} es mayor que 3")
                mayores3 = mayores3+1
            
    elif opc ==11:
            
        sumSub= sum(lista1[1:4])       
        print(f"la suma de la sublista es {sumSub}")

    elif opc ==12:

        promedioLista1= sum(lista1)/len(lista1)
        print(f"El promedio de la lista 1 es: {promedioLista1}")

    elif opc ==13:

        for i in lista1:
            if i%2==0:
                print(f"{i} es numero par")

    elif opc ==14:
        lista3=[1,2,3,4,5]        
        for i in lista3:
            print(f"{i} al cuadrado es: {i**2}")


    elif opc ==15:

        buscar= 3 in lista1
        print("3 Existe en lista 1 ?: ",buscar)
        

    elif opc ==16:
        i=0
        while i >=-10:
            print(i)
            i=i-1

    elif opc ==17:

        list3=[1,2,3]
        list4=[4,5,6]
        list3.extend(list4)
        print("el resultado de concatenar [1,2,3] y [4,5,6] es: ",list3)
        
    elif opc ==18:

        lista3=[1,2,3]
        lista4=["a","b","c"]

        a=list(zip(lista3,lista4))
        print("Pares ordenados: ",a)

    elif opc ==19:

        naturales=list(range(1,6))
        print("numeros naturales del 1 al 5",naturales )


    elif opc ==20:

        palabras=["HoLa", "MUNDO", "pYThon"]
        ee=[palabra.upper() for palabra in palabras]
        print(ee)

    elif opc ==21:
        print("Hasta pronto")
        m=False    

     