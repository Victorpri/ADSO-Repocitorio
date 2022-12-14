#Este codigo es de IVAN

'''Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta.'''
num=int(input("introduzca un numero"))
contador=0
while num>-1:
    num=int(input("introduzca un numero"))
    contador+=1
print("menciono",contador,"numeros positivos")