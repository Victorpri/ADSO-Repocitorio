#Este codigo es de IVAN

'''¿Cuáles y cuántos son los números primos comprendidos
entre 1 y 1000?'''
numero= 1
contador1 = 0
for i in range(10,1001):
    for n in range(2,numero):
        if numero % n == 0:
            contador1 +=1
            print("divisor:", n)
    numero+=1
    if contador1 > 0 :
        print("El número no es primo" )
    else:
     print("El nÚmero es primo")