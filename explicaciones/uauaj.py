#cuales tienen un solo digito de los numeros
#los numeros que se guardan son edad o - 100 y en cada espacio en un vector nuevo si es mayor de edad o menor de edad
import random

vector =[round(random.random()*100) for i in range(10)]
print(vector)

digitouno = [x for x in vector if x < 10]

digitov = [x for x in vector if x > 9]

print("Los numeros con mas de dos digitos son: ", digitov)

print("Los numeros con un solo digito son: ", digitouno)


"""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""

vector =[round(random.random()*100) for i in range(10)]
print(vector)

menor = [x for x in vector if x < 18]
mayor = [x for x in vector if x > 17]
print("Los mayores de edad son: ", mayor)
print("Los menores de edad son: ", menor)

"""aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""

vector =[round(random.random()*100) for i in range(10)]
print(vector)

undigito = [x if x<10 else 0 for x in vector]
print(undigito)
edad = ['mayor' if x >= 18 else 'menor' for x in vector]
print(edad)


17