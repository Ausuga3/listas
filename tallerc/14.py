#Escribe un algoritmo que alterne mayúsculas y minúsculas en una lista de strings.
palabras = ["python", "es", "genial"]
palabrasAlternadas = [palabra.upper() if i % 2 == 0 else palabra.lower() for i, palabra in enumerate(palabras)]
print(palabrasAlternadas)