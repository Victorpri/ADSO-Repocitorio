#Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene. Cuando el número
#exceda los límites emita un mensaje y finalice el programa

n = int(input("Escriba un numero entre 0 y 9999: "))

def numero(num):
    if n <= 9:
        return 'solo tiene una cifra'
    elif n <= 99 and n >= 10:
        return 'tiene dos cifras'
    elif n <= 999 and n >= 100:
        return 'tiene tres cifras'
    elif n <= 9999 and n >= 1000:
        return 'tiene cuatro cifras'
    else:
        return 'este numero es mayor a 9999'

print(numero(n))

