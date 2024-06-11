#Escribe un algoritmo que filtre una lista de palabras y devuelva solo las palabras que contienen una subcadena específica.
palabras = ["hola", "mundo", "holanda", "python", "holístico"]

subCadena="hol"

palabrasFiltradas = [i for i in palabras if subCadena in i]
print("Palabras que contienen 'hol':", palabrasFiltradas)