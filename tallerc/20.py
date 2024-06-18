#Escribe un algoritmo que elimine las palabras de menos de 4 caracteres de una lista de strings.
palabras = ["python", "es", "genial", "muy", "bueno"]

newList =[ p.capitalize() for p in palabras if len(p) >=4]   
print(newList)   
    
    