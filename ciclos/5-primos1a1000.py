"""5.	¿Cuáles y cuántos son los números primos comprendidos entre 1 y 1000?."""
cont=0
for j in range (1,1000,1):
    suma= 0
    for i in range (2,j,1):
        if j%i==0:
            suma+=1
    if suma==0:
        cont+=1
        print ("El número ",j," es primo")
print("Hay ",cont," números primos entre 1 y 1000")