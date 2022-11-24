#"""2.	Determinar si un numero es o no es primo."""

num = int(input("ingrese un número    "))
cont = 0
for i in range (2,num,1):
    if num%i==0:
        cont +=1
if cont>0:
    print ("el número no es primo")
else:
    print ("el número es primo")