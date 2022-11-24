"""1. Determinar los divisores de un número introducido por teclado."""

num = int(input("Ingrese un número   "))
if num>0:
    print ("SUS DIVISORES SON: ")
    for i in range (1,num+1,1):
        if num%i==0:
            print (i)
elif num<0:
    print ("SUS DIVISORES SON: ")
    for i in range (-1,num-1,-1):
        if num%i==0:
            print (i)
else:
    print ("NINGÚN NÚMERO ES DIVISIBLE POR 0")