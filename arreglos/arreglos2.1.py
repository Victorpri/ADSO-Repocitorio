#Este codigo es de IVAN

'''Determinar si el numero es o no es par'''

def parimpar(num=int(input("Ingrese un numero: "))):
    while num>0:
        if num%2==0:
            return "El numero ingresado es par"
        else:
            return "El numero ingresado no es par"

print(parimpar())