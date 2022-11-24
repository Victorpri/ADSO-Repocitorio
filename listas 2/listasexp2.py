#2. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Muestre cuales y cuantos son primo
import random

vector =[round(random.random()*100) for i in range(10, 25)]
print(vector)

for i in range(2, vector + 1):
    primos = True
    for j in range(2,i):
        if i == j:
           break
        elif i%j == 0:
           primos = False

