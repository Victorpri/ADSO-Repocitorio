#PILA

'''

Una pila es una estructura de almacenamiento de datos

se utiliza como una cada le libros 'lo primero que entra es lo ultimo que sale'

ejemplo:
'''

'''
stack=[]

def push(val):
    stack.append(val)

def pop():
    val = stack[-1]
    del stack[-1]
    return val

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())
'''



