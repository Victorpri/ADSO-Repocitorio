import random

#vec = []

#tam=round(random.randint(5,15))

#vec=[(i+1)**0.5 for i in range(tam)]
#print(vec)

vector =[round(random.random()*100) for i in range(10)]
print(vector)

pares = [x for x in vector if x%2==0]
impares = [x for x in vector if x%2!=0]
print(impares)
print(pares)

pares2=[x if x%2==0 else 0 for x in vector]
print(pares2)
