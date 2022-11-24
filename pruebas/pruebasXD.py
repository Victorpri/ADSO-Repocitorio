import random
tam = int(input("Ingrese un numero: "))
vec = []
for i in range(tam):
    vec.insert(i,round(random.random()*100))
print(vec)

cont = 0
cont2 = 0

suma = 0
suma2 = 0


for i in range(len(vec)):
    if vec [i]%2==0:
        print(vec[i]," par")
        cont+=1
        suma += vec[i]
        
    else:
        print(vec[i]," inpar")
        cont2 += 1
        suma2 += vec[i]
        
        
print("hay", cont,"numeros pares")
print("la suma de los numeros pares son: ", suma)
print("Hay", cont2, "numeros impares")
print("la suma de los numeros inpares son: ", suma2)

