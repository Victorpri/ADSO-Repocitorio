minutos = float(input("Escriba cuanto duro la llamada: "))

if(minutos <= 3):
    print("La llamada costo",minutos * 200)
elif(minutos >=4):
    print("La llamada costo",450 + minutos * 50)