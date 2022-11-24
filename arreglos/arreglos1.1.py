#Escribe un programa que pida tres números y que escriba si son los tres
#iguales, si hay dos iguales o si son los tres distintos
n1 = float(input("introduzca un numero: "))
n2 = float(input("introduzca un numero: "))
n3 = float(input("introduzca un numero: "))


def tresNumeros(x,y,z):
    if (x == y == z):
        return"los 3 numeros son iguales"
    elif (x == y != z):
         return "dos numeros son iguales"
    elif (x == y != z):
          return "dos numeros son iguales"
    elif (x == y != z):
         return "dos numeros son iguales"
    else:
         return"ningun numero es igual"

print(tresNumeros(n1,n2,n3))