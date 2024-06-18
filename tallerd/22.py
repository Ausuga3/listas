#Ejercicio 22: Crear una lista que contenga una mezcla de números y cadenas de texto y mostrar solo los elementos que sean cadenas de texto.
mixta = [1, 'hola', 2, 'mundo', 3, '']
soloTexto=[s for s in mixta if isinstance(s,str)]
print(soloTexto)