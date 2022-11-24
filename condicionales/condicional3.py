numero_1 = float(input("escriba un numero entre el 0 y el 9999: "))

if(numero_1<=9999 and numero_1>=1000):
    print("este numero tiene cuatro cifras")
elif(numero_1<=999 and numero_1>=100):
    print("este numero tiene tres cifras")
elif(numero_1<=99 and numero_1>=10):
    print("este numero tiene dos cifras")
elif(numero_1<=9 and numero_1>=0):
    print("este numero tiene una ciffra")
else: 
    print("numero mayor a cuatro cifras")





