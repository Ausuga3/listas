#16 Escribe un algoritmo que genere una lista de los primeros 10 números de Fibonacci

fibonnaci=[0,1]

for i in range(2,10):
    result=fibonnaci[-1]+fibonnaci[-2]
    fibonnaci.append(result)
    
print(fibonnaci)    