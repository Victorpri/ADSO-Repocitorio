#4. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Ordenar el arreglo, de mayor a menor y de menor a mayor (algoritmo de la burbuja)
import random

vector = [round(random.random()*100) for i in range(10, 25)]
print(vector)



