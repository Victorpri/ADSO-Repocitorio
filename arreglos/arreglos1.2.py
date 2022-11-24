#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el
#valor del medio es 11. No use operadores lógicos

n1 = int(input("introduzca un numero: "))
n2 = int(input("introduzca un numero: "))
n3 = int(input("introduzca un numero: "))

def numDelMedio(x,y,z):
    if x < y < z:
        return n2,' es el valor del medio'
    elif z < y < x:
        return n2,' es el valor del medio'
    elif y < x < z:
        return n1,'es el valor del medio'
    elif z < x < y:
        return n1,'es el valor del medio'
    elif x < z < y:
        return n3, 'es el valor del medio'
    elif y < z < x:
        return n3, 'es el valor del medio'

print(numDelMedio(n1, n2, n3))
