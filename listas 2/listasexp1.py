#1. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.
import random

vector =[round(random.random()*100) for i in range(10, 25)]
print(vector)
suma = 0
prom = 0
for i in vector:
    suma += i
    prom = suma / len(vector)
encimaprom = [ x for x in vector if x > prom]
print("Los numeros que estan encima del promedio son: ", encimaprom)

debajoprom = [ x for x in vector if x < prom]
print("Los numeros que estan debajo del promedio son: ", debajoprom)