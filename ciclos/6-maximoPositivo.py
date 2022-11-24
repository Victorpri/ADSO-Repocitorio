"""6. Calcular el máximo de números positivos introducidos por teclado,
    sabiendo que metemos números hasta que introduzcamos uno negativo.
    El negativo no cuenta."""

num=0
maximo=0
cont=0
while num>=0:
    num =int(input("Ingrese un número      "))
    if num>=0:
        cont +=1
    if num>maximo:
        maximo=num
if cont>0:
    print("De los",cont,"números positivos que usted digito, el número mas grande es:",maximo)
else:
    print("No digito un número positivo, fin del programa")
