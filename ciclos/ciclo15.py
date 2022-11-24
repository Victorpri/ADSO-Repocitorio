"""Diseñar e implementar un programa que solicite a su
usuario un valor no negativo n y visualice la siguiente salida:
1 2 3 ........ n-1 n
1 2 3 ........ n-1
.........
1 2 3
1 2
1"""

x = int(input("Digite un numero positivo: "))

for i in range(x):
    for j in range(1,x+1):
        print(j," ",end="")
    x = x-1
    print("")