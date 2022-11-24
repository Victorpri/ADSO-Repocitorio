#8.	Determinar cuales son los múltiplos de 5 comprendidos entre 1 y N.

num=int(input("Ingrese la cantidad de multiplos de 5:   "))
for i in range (1,num+1,1):
    multiplo=5*i
    print (multiplo)