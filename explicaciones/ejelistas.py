import random

"""b = [5, 3, 2,7,2,1,53,5]
a=b
a.append(8)

print(b)

#[start(inclusive)-end(no inclusive)]

c = b [1:4]
print(c) """



vec = []

suma = 0

for i in range (30):
    vec.append(round(random.randint(5,28)))
    suma += 1

print(vec)

suma1 = 0
suma2 = 0
suma3 = 0

pm = vec[:15]
for i in pm:
    suma1 += i
print("La primera mitad es: ", pm )
print("El promedio de la primera mitad es: ", suma1/len(pm))
sm = vec[16:]
for i in sm:
    suma2 += i
print("La segunda mitad es: ", sm )
print("El promedio de la segunda mitad es: ", suma2/len(sm))
pt = vec[:10]
for i in pt:
    suma3 += i
print("el primer tercio es: ", pt )
print("El promedio del primer tercio es: ", suma3/len(pt))