#Este codigo es de IVAN

'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
del promedio o es igual al promedio de todos los números de la lista.'''
import random
from statistics import mode

def promedio():
    vec=[]
    a=0
    suma=0
    for i in range(random.randint(10,25)):
        vec.insert(i,round(random.random()*100))
        suma+=vec[i]
        a+=1
        promedio=suma//a
        
        if i < promedio:
            print("El numero esta por debajo del promedio",vec[i])
        elif i == promedio:
            print("El numero es igual al promedio",vec[i])
        else:
            print("El numero esta por encima del promedio",vec[i])
    return vec
            
print(promedio())