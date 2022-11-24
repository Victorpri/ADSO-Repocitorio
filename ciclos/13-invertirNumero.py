"""13. Solicitar al usuario un número de hasta 9 dígitos e imprimirlo en orden contrario.
Ej. digito 6754 imprimo 4576."""

num = int(input("Ingresar un número de hasta 9 dígitos:  "))
if num>0 and num<1000000000:
    invertido=0
    while num!=0:
        invertido = 10 * invertido+num % 10
        num = num // 10
print(invertido)