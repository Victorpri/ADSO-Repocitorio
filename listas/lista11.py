#Este codigo es de IVAN

'''Escribir un programa que visualice la siguiente figura,
utilizando ciclos. El usuario decide cuantas líneas quiere
imprimir
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * *'''
lineas=int(input("Cuantas lineas quieres?: "))
figura="*"
for i in range(lineas):
    print(figura)
    figura+="*"