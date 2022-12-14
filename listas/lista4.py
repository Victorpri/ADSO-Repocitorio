#Este codigo es de IVAN

'''Determinar cuales y cuantos números perfectos hay entre 1 y
1000?'''
numero=1
i=1
divisores=0
contador=0
for a in range(1000):
    divisores=0
    for i in range(1,numero):
        if (numero % i) == 0 :
            divisores=divisores+i
    if divisores==numero:
        print(numero,"es numero perfecto")
        contador+=1
    numero+=1
print("hay",contador,"numeros perfectos del 1 al 1000")