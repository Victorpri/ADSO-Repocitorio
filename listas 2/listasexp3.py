#3. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Sume los pares y saque el promedio de los impares
import random

vector =[round(random.random()*100) for i in range(10, 25)]
print(vector)
suma = 0
suma1 = 0
prom  = 0
pares = [x for x in range (len(vector)) if vector[x]%2==0]
print("Los numeros pares son: ", pares)
for i in range (len(pares)):
    suma += pares[i]
print("La suma de los pares son: ",suma)

impares = [x for x in vector if x%2==0]
print("Los numeros impares son: ", impares)
for i in range (len(impares)):
    suma1 += impares[i]

print("La suma de los impares son: ", suma1)
print("El promedio de los impares son: ", suma1 / len(impares))