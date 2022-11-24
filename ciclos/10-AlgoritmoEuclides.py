# Algoritmo para hallar el m.c.d de dos números m y n por el algoritmo de Euclides.

num1=int(input("Ingrese el número 1:   "))
num2=int(input("Ingrese el número 2:   "))
resto=1
while resto!=0:
    resto = num1 % num2
    if resto ==0:
        print ("El M.C.D de los 2 números es: ", num2)
    else:
        num1=num2
        num2 = resto
