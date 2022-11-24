#1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.
import random

tam = round(random.randint(10, 25))

vec = []
suma = 0
prom = 0

for i in range (tam):
    vec.append(round(random.random()*100))
    suma = suma + vec[i]
    prom = suma / len(vec)
    if vec[i] < prom:
        print("El numero esta por debajo del promedio", vec[i])
    elif vec[i] > prom:
        print("El numero esta por encima del promedio", vec[i])
    elif vec[i] == prom:
        print("El numero es igual al promedio", vec[i])

print("La lista es: ", vec)



