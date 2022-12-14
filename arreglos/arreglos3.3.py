#Este codigo es de IVAN

'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Sume los pares y saque el promedio de los impares'''
import random
from statistics import mode
def par_impar():
    vec=[]
    a=0
    suma1=0
    suma=0
    cont1=1
    prome1=0
    for i in range(random.randint(10,25)):
        vec.insert(i,round(random.random()*100))
        suma+=vec[i]
        a+=1    
        if i%2==0:
            print("El numero es par",vec[i])
        else:
            print("El numero es inpar",vec[i])
            suma1+=vec[i]
            cont1=1
            prome1=suma1/cont1
    print(vec)
    return "El promedio de los impares es: ",prome1


print(par_impar())