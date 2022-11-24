h = float(input("Escriba el numero de horas en total trabajadas: "))
he = float(input("Escriba cuantas horas extras realizo: "))

salario = (h * 2600)
salarioextra = (40 * 2600 + he * 5000)

if(h <= 40):
    print(salario)
elif(h >= 41):
    print(salarioextra)




