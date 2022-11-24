"""7. Encontrar un número natural n más pequeño tal que la suma de los n 
    primeros números naturales (1 + 2 + 3 + 4…..) exceda de una cantidad (máximo)
    introducida por el teclado.
    Es decir cuantos números  de la serie de los naturales debo sumar para superar el dato máximo."""

num = int(input("Ingrese el número máximo   "))
cont=0
while cont*(cont+1)<=2*num:
    cont+=1
print("El número natural mas pequeño que excede al dato es:",cont)