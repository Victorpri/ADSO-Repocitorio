#numeros iguales o diferentes

n1 = float(input("introduzca un numero: "))
n2 = float(input("introduzca un numero: "))
n3 = float(input("introduzca un numero: "))

if (n1 == n2 == n3):
    print("los 3 numeros son iguales")
elif (n1 == n2 != n3):
    print("dos numeros son iguales")
elif (n3 == n2 != n1):
    print("dos numeros son iguales")
elif (n3 == n1 != n2):
    print("dos numeros son iguales")
else:
    print("ningun numero es igual")

