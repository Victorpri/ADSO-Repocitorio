#5. Llenar una lista de tamaño aleatorio entre 10 y 25 elementos. Llene la lista con números
#aleatorios. Solicite al usuario un número para buscar en la lista. Diga cuantas veces está y en que
#posiciones esta. Si no está agréguelo al final de la lista.
import random

vector =[round(random.random()*100) for i in range(10, 25)]
print(vector)

num = int(input("Escruba un numero: "))

rep = [num for num in vector ]