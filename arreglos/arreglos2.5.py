#Este codigo es de IVAN

'''Calcular la operación x n sin utilizar la función pow'''
def potencia(num1=int(input("Ingrese una base: ")),
          num2=int(input("Ingrese un exponente: "))):
    resultado=1
    for i in range(num2):
        resultado*=num1
    return resultado
print(potencia())