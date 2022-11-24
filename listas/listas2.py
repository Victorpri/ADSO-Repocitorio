#2. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Muestre cuales y cuantos son primo
import random

tam = round(random.randint(10, 25))

vec = []
suma = 0
prom = 0
primos = []

for x in range (tam):
    vec.append(round(random.random()*100))
      
print(vec)




 
    

   
