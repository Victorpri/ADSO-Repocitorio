numero_1 = float(input("escriba la calificacion del estudiante: "))

if(numero_1<=10 and numero_1>=9):
    print("La nota es perfecta")
elif(numero_1<=8 and numero_1>=7):
    print("La nota es casi perfecta")
elif(numero_1<=6 and numero_1>=5):
    print("La nota es regular")
elif(numero_1<=4 and numero_1>=3):
    print("La nota es basica")
elif(numero_1<=2 and numero_1>=1):
    print("La nota es insuficiente")
else:
    print("La tota no es valida")
    