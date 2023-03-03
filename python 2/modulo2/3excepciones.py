
#EXEPCIONES

'''Cuando pasa un error python hace dos cosas:

- detener el programa 
- crear un dato llamado exepcion

cuando se genera una exepcion se espera a que alguien la resuelva

despues si no es resuelta el programa se terminara y saldra 
un error por consola

pero si la exepcion es manejada el programa continuara

'''

# OTRAS EXEPCIONES 

#ZeroDivisionError

''' Otra exepcion es el ZeroDivisionError que se utiliza 
cuando se intenta dividir en cero'''

'''value = 1
value /= 0'''

#IndexError

'''pasa cuando se trata de acceder a datos imposibles en una 
lista como puede ser los inexistentes'''

'''my_list = []
x = my_list[0]'''

#EXEPVIONES (CONTINUACION)

'''el metodo que nosotros utilizaremos va a ser el TRY(try)
y se debe utilizar asi:

- intentar (try) hacer algo 
- despues ver si todo salio bien
'''

'''Para el primer paso debemos saber que utilizaremos 
el try y el except una vez tengamos el codigo Python
intentara realizar las instrucciones dadas, si no hay ningun
problema entonces Python salta desoues de la ultima 
linea de except y la ejecucion sera completada. Pero
si algo sale mal entonces entra a la primera instruccion del
except y las instrucciones pueden ser omitidas'''

'''first_number = int(input("Ingresa el primer numero: "))
second_number = int(input("Ingresa el segundo numero: "))

try:
    print(first_number / second_number)
except:
    print("Esta operación no puede ser realizada.")

print("FIN.")'''

'''Si en el codigo hay mas de una manera que suceda un aerror
hay dos formas de resolver el prib lema :

- construir dos bloques de try-except

y la otra la cual es mucho mas favorable y elegante

- emplear una variable mas avanzada de la instruccion

try:
    :
except exc1:
    :
except exc2:
    :
except:
    :
    
funciona asi:

si el try genera la excepcion exc1 sera manejada por el
bloque  except exc1, y de la misma manera co la exc2
y si el try gemra otra exepcion sera manejado por el
except'''

'''try:
    x= int(input('Ingrsa un numero: '))
    y = 1/ x
    print(y)
except ZeroDivisionError:
    print('No puedes dividir entre cero, lo siento.')
except ValueError:
    print('Deves ingresar un valor entero.')
except:
    print('Oh cielos, algo salio mal...')

print('FIN.')'''

'''
-si se ingresa un valor entero valido distinto a cero:
0.2
FIN.

-si se ingrsa 0:
No puedes dividir entre cero, lo siento.
FIN.

-si se ingrea cualquier cadena no entera :
Debes ingresar un valor entero.
FIN.

-Si se interrumpe el proceso provocara un:KeyboardInterrupt
el programa dira:
Oh cielos, algo salió mal...
FIN.
'''

'''Recuerda:

-¡El orden de las excepciones importa!

-No pongas excepciones más generales antes que 
otras más concretas.

-Esto hará que el último sea inalcanzable e inútil.

-Además, hará que el código sea desordenado e 
inconsistente.

-Python no generará ningún mensaje de error con respecto
a este problema.'''

'''Si se desea manejar dos o mas excepciones de la misma
manera se utiliza la siguiente sintexis:

try:
    :
except (exc1, exc2):
    :
'''

'''Tambion se pueden generar excepciones dentro de funciones 
y se pueden utizar dentro o fuera de la funcion

eje:'''

'''def bad_fun(n):
    try:
        return 1/n
    except ArithmeticError:
        print('Problema Aritmetico')
    return None

bad_fun(0)

print('FIN.')'''

'''Es bastante facil de entender la excepcion ZeroDivisionError
es un caso concreto de la clase ArithmeticError y es generada
dentro de la funcion bad_fun() y la funcion se encarga de ella
La salida del programa es:

¡Problema Aritmético!
FIN.'''

'''Tambien al dejar la excepcion afuera de la funcion 
el problema tiene que ser resuelto por el invocador

eje:'''

'''def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se generó una excepción!")

print("FIN.")'''

#RAISE

'''la instruccion raise genera la excepcion especificada
como si se hubiece generado de forma natural

raise exc

esta instruccion perimite simular excepciones reales
y sirve para probar el manejo de excepciones 

eje:'''

'''def bad_fun(n):
    raise ZeroDivisionError

try:
    bad_fun(0)
except ArithmeticError:
    print('Sucedio un error.')

print('FIN.')'''

'''Tambien se puede utilizar la instruccion raise sola
unque tiene una gran resticcion y es que no se puede 
utilizar en otro lugar que no sea except

eje:'''

'''def bad_fun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")'''

#INSTRUCCION ASSERT(AFIRMAR)

'''En la instruccion assert se evalua la expresion ,
si la expresion es True no se hara nada mas, pero si se
evalua como False inmediatamente se generara una excepcion
llamada AssertionError'''

'''Esta instruccion se utiliza en la parte del codigo 
donde quieras estar a salvo de datos incorrectos 
esto sirve como una bolsa de aire para tu codigo

eje:'''

'''import math

x = float(input("Ingresa un número: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)'''

'''Si se ingresa un valor no valido emite el siguiente mensaje:'''

'''Ingresa un número: -5
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    assert x >= 0.0
AssertionError'''










