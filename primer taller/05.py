print("Bienvenido al Sistema de inventario")
producto =[]
cantidad =[]

precio   =[]

i = True
while i == True:

    opcion=int(input("Ingresar\n1--Crear Producto\n2--Buscar Producto\n3--Actualizar Producto\n4--Eliminar Producto\n5--Salir\n: "))

    if opcion >= 0 and opcion <=5:
        if opcion==1:
            nombreP = input("Ingresa el nombre del producto: ").capitalize()
            cantidadP = int(input("Ingrese cantidad del producto: "))
            precioP = float(input("Ingrese el precio del producto: "))

            producto.append(nombreP)
            cantidad.append(cantidadP)
            precio.append(precioP)

            print("----- Producto almacenado correctamente -----")

        elif opcion ==2:
            buscarProducto = input("Ingresa producto a buscar: ").capitalize()
            resultado = buscarProducto in producto
            if resultado == True:
                print("----- Producto encontrado -----")
                elemento = producto.index(buscarProducto)

                print("Nombre del producto ",producto[elemento])
                print("Cantidad del producto ",cantidad[elemento])
                print("Precio del producto ",precio[elemento])
            else:
                print("----- Producto No encontrado -----")      

        elif opcion == 3:
            buscarProducto = input("Ingresa producto a Actualizar: ").capitalize()
            resultado = buscarProducto in producto
            if resultado == True:
                print("----- Producto encontrado -----")

                nuevoNombreP = input("Ingresa el nombre nuevo del producto: ").capitalize()
                nuevaCantidadP = int(input("Ingrese la cantidad nueva del producto: "))
                nuevoPrecioP = float(input("Ingrese el precio nuevo del producto: "))
                
                elemento = producto.index(buscarProducto)

                producto[elemento] = nuevoNombreP
                cantidad[elemento] = nuevaCantidadP
                precio[elemento] = nuevoPrecioP

                print("----- Producto actualizado correctamente -----")
            else:
                print("----- Producto No encontrado -----")    
        elif opcion == 4:

            buscarProducto = input("Ingresa producto a eliminar: ").capitalize()
            resultado = buscarProducto in producto

            if resultado == True:
                print("----- Producto encontrado -----")
                elemento = producto.index(buscarProducto)

                del producto[elemento]
                del cantidad[elemento]
                del precio[elemento]

                print("----- Producto Eliminado correctamente -----")
            else:
                print("----- Producto No encontrado -----")  
        elif opcion == 5:
            print("Hasta pronto")
            i= False        
    else:
        print("Esta opcion no existe")        
