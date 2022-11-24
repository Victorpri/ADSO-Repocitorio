"""4. Determinar cuales y cuantos números perfectos hay entre 1 y 1000?."""

from math import trunc

for j in range (1,1000,1):
    suma= 0
    for i in range (2,j+1,1):
        if j%i==0:
            suma=suma+(trunc(j/i))
    if suma==j:
        print ("El número ",j," es perfecto")