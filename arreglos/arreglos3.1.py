#Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. De cada elemento de la lista diga si el elemento está por encima del promedio, debajo
#del promedio o es igual al promedio de todos los números de la lista.
import random

def llenarLissta (list):
    tam=round(random.randint(10,25))
    for i in range(tam):
        list.append(round(random.randrange(100)))
    return list
    
lista = []
lista=llenarLissta(lista)

def promedio (list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(lista)

print(lista)
print("El promedio de la lista es: ", promedio(lista))

def numerosEDI(list):
    for i in lista:
        if i < promedio(lista):
            return 'esta por debajo del promedio'
        elif i > promedio(lista):
            return 'esta por encima del promedio'
        



print(numerosEDI(lista))





