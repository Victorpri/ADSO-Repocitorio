#Este codigo es de IVAN

'''Calcular el máximo de números positivos introducidos por
teclado, sabiendo que metemos números hasta que
introduzcamos uno negativo. El negativo no cuenta.'''
def positivo(num=int(input("introduzca un numero: "))):
    contador=0
    while num>-1:
            num=num=int(input("introduzca un numero: "))
            contador+=1
    print("El total de numeros positivos es: ",contador)
positivo()