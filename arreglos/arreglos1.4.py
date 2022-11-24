#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
#etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores
nota = int(input("escriba la nota: "))

def notaEstudiante(num):
    if nota <= 10 and nota >= 9:
        return 'La nota es: exelente'
    elif nota <= 8 and nota >= 7:
        return 'La nota es: muy bien'
    elif nota <= 6 and nota >= 5:
        return ' La nota es: bien'
    elif nota <= 4 and nota >= 3:
        return 'La nota es: suficiente'
    elif nota <= 2 and nota >= 1:
        return 'La nota es insufuciente'
    else:
        return 'La nota es nula'
print(notaEstudiante(nota))