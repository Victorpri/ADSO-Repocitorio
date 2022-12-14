#Este codigo es de IVAN

'''Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
aleatorios. Muestre cuales y cuantos son primos'''

import random
def primos():
    cont=0
    cont1=0
    suma1=0
    tam=random.randint(10, 25)
    vec=[]
    for i in range(tam):
        vec.insert(i,round(random.randint(0, 100)))
    print(vec)

    for i in range(len(vec)):
        if vec[i]%2==0:
            cont=cont+1
        if cont > 2:
            continue
        else:
            print(vec[i],' el numero es primo')
            cont1=cont1+1
            suma1=suma1+vec[i]
    print("La cantidad de numeros primos es: ",cont1)
    print("La suma de los numeros primos es igual a: ",suma1)
print(primos())