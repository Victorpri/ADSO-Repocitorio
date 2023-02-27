values = (1, 0)
#aca se declara una varible con una valor de una tupla

try:
# el try se coloca para poder evaluar y analizar los errores en el codigo

    q, r = divmod(*values)
# en esta parte se utilizan dos variables separadas por comas las cuales valen el divmod(se utiliza para conseguir el cosiente y el residuo)
    
    print(f'q={q}')
#no me acuerdo

    print(f'r={r}')
#no me acuerdo

except (ZeroDivisionError, TypeError) as e:
#este se usa parte se crea un except con dos errors, es decir que si hay alguno de los dos errores dara el mismo mensaje

    print(type(e), e)
#este es el resultado de el except pero no me acuerdo como funciona
