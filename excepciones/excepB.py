values = (1, 0)
#aca se declara una varible con una valor de una tupla

try:
# el try se coloca para poder evaluar y analizar los errores en el codigo

    q, r = divmod(*values)
# en esta parte se utilizan dos variables separadas por comas las cuales valen el divmod(se utiliza para conseguir el cosiente y el residuo)
    
    print(f'q={q}')
    print(f'r={r}')
except (ZeroDivisionError, TypeError) as e:
    print(type(e), e)