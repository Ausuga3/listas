#11 Escribe un algoritmo que genere una lista de factoriales de los números del 1 al 5.

import math
factoriales = [math.factorial(i) for i in range(1, 6)]
print("Lista de factoriales:", factoriales)