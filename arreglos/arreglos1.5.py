#Telefónica realiza los cálculos del costo de una llamada de teléfono siguiendo
#los cálculos así:
#Cuando se descuelga el teléfono los primeros 3 minutos (banderazo) cuestan
#200 pesos y cada minuto adicional cuesta 50 pesos. Escriba un programa que
#permita calcular el costo de una llamada dados los minutos de duración.

min = int(input("Cuanto duro la llamada: "))

def minutosDuracion(num):

    if min <= 3:
        return "La llamada costo",min * 200
    elif min >=4:
        return "La llamada costo",450 + min * 50

print(minutosDuracion(min))

