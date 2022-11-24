"""3. Determinar si un número es o no es perfecto.
Un numero es perfecto si la suma de sus divisores sin incluir el propio número es igual a este."""

from math import trunc

num = int(input("Ingrese un número   "))
suma= 1
if num>1:
    for i in range (2,num,1):
        if num%i==0:
            suma=suma+(trunc(num/i))
if suma>1:
    print ("El número ",num," es perfecto")
else:
    print ("El número ",num," no es perfecto")