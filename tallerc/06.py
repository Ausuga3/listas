#6 Escribe un algoritmo que ordene una lista de palabras por su longitud.

palabras = ["python", "es", "un", "lenguaje", "de", "programación"]
ordenAlfabetico=sorted(palabras)

ordenTotal=sorted(ordenAlfabetico,key=len)
print(ordenTotal)
