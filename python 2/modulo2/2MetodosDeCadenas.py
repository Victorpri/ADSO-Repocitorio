#EL METODO capitalize()

'''Este metodo se utiliza para cambiarde cierta 
forma una cadena, al hacer esto suceden dos cosas:

- El primer caracter de la cadena se cambiara por una 
mayuscula
- todas las letras restantes se volveran minusculas'''

'''print('hola MUNDO'.capitalize())'''

#EL METODO center()

'''este metodo se utiliza mucho para centrar
cadenas en un espacio determinado utilisando
el center(numero x), aunque tambien se utiliza 
el  center(numero x,'cualquier caracter' )'''

'''print('[' + 'alpha'.center(100) + ']')
print('[' + 'gamma'.center(20, '*') + ']')'''

#EL METODO endswith()

'''este metodo sirve para comprovar si la cadena
termina con el parametro especificado y para cada caso
devuenve un TRUE o un FALSE dependiendo del resultado'''

'''t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))'''

#EL METODO find()

'''en este metodo lo que se hace es buscar una sub cadena 
 para despues  devolver el indice de la primera 
 aparicion de esta sub cadena'''

'''si solo deseas verificar un solo caracter, lo mejor
es utilizar el operador in qu sera mas rapido'''

'''t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))'''

'''si se quiere hacer la busqueda desde otra parte de ña cadena
se utiliza una variante de dos perimetros'''

'''print('kappa'.find('a', 2))'''

'''se puede  emplear este metodo para buscar 
todas las ocurencias de la sub cadena '''

'''the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)'''

#EL METODO isalnum()

'''este metodo se utiliza para  comprobar si la cadena 
tiene solo digitos o caracteres alfabeticos y 
devuelve True o False segun coresponda'''

'''print('Hola soy Victor5543'.isalnum())
print('Hola Victor@_'.isalnum())'''

#EL METODO isalpha()

'''este es lo midmo que el anterior pero 
se especializa en letas'''

'''print("Moooo".isalpha())
print('Mu40'.isalpha())'''

#EL METODO isalpha()

'''este solo busca digitos'''

'''print('2018'.isdigit())
print("Year2019".isdigit())'''

#EL METODO islower()

'''se usa para identificar si hay letras minusculas
en una cadena'''

'''print('escribo sin manos'.islower)'''

#EL METODO isspace()

'''se usa para identificar espacios en blanco
y no debe contener ningun otro caracter'''

'''print('escribo sin manos'.isspace)
print(' '.isspace)'''

#EL METODO isupper()

'''se usa para identificar si hay letras mayusculas
en una cadena'''

'''print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())'''

#EL METODO join()

'''este metodo se utiliza para relizar una union de
varias cadenas separas por algun caracter en especifico
y todas las cadenas estan en una misma cadena y la
invocacion de el metodo es el separador que esta entre 
ellas'''

'''print(','.join(['escribo', 'sin', 'manos']))'''

#EL METODO lower()

'''este metodo se utiliza para remplazar las letras mayusculas 
con letras minusculas, la cadena original no sufre 
cambios, este metodo no necesita de  ningun parametro'''

'''print('ESCRIBO sin MANOS'.lower)'''

#EL METODO lstrip()

'''este metodo elimina los espacios en blanco y 
devuelve una cadena nueva, tambien se puede 
utilizndo parametros, haciendo que elimine no solo los
espacios en blanco si no tambien los caracteres incluidos
en el argumento '''

'''print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip("institute."))'''

#EL METODO replace()

'''este metodo da una copia de la cadena original
pero remplaza las apariciones del primer argumento 
con las del segundo argumento
tanbien existe una variante de tres argimentos el
cual el tercero es numerico y se usa para limitar el
numero de remplazos '''

'''print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))


print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 7))'''

#EL METODO rfind()

'''este metodo hace lo mismo que el metodo find
con la diferencia que empieza desde el final de
la cadena no desde el principio como find'''

'''print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))'''

#EL METODO split()

'''este metodo divide la cadena y crea una lista con
las sub cadenas encontradas, las subcadenas estan
delimitadas por espacios en blancos'''

'''print("phi       chi\npsi".split())'''

#EL METODO starwith()

'''este metodo comprueba si una cadena comienza con la 
sub cadena especificada'''

'''print("omega".startswith("meg"))
print("omega".startswith("om"))'''

#EL METODO swapcase()

'''este metodo crea una nueva cadena cambiando 
las letras mayusculas por minusculas y visaversa
los demas caracteres permanecen intactos'''

'''print("Yo sé que no sé nada.".swapcase())'''

#EL METODO title()

'''este metodod cambia la primera letra de cada
palabra por mayuscula y las demas a minuscula'''

'''print("Yo sé que no sé nadA. Part 1.".title())'''

#EL METODO upper()

'''este metodo devuelve una copia de la cadena pero
cambia todas las minusculas a mayusculas'''

'''print("Yo sé que no sé nada. Part 2.".upper())'''


#RESUMEN:

'''1. Algunos de los métodos que ofrecen las cadenas son:'''

#capitalize(): cambia todas las letras de la cadena a mayúsculas.
#center(): centra la cadena dentro de una longitud conocida.
#count(): cuenta las ocurrencias de un carácter dado.
#join(): une todos los elementos de una tupla/lista en una cadena.
#lower(): convierte todas las letras de la cadena en minúsculas.
#lstrip(): elimina los caracteres en blanco al principio de la cadena.
#replace(): reemplaza una subcadena dada con otra.
#rfind(): encuentra una subcadena comenzando por el final de la cadena.
#rstrip(): elimina los caracteres en blanco al final de la cadena.
#split(): divide la cadena en una subcadena usando un delimitador dado.
#strip(): elimina los espacios en blanco iniciales y finales.
#swapcase(): intercambia las mayúsculas y minúsculas de las letras.
#title(): hace que la primera letra de cada palabra sea mayúscula.
#upper(): convierte todas las letras de la cadena en letras mayúsculas.

'''El contenido de las cadenas se puede determinar mediante los siguientes métodos (todos devuelven valores booleanos):'''

#endswith(): ¿La cadena termina con una subcadena determinada?
#isalnum(): ¿La cadena consta solo de letras y dígitos?
#isalpha(): ¿La cadena consta solo de letras?
#islower(): ¿La cadena consta solo de letras minúsculas?
#isspace(): ¿La cadena consta solo de espacios en blanco?
#isupper(): ¿La cadena consta solo de letras mayúsculas?
#startswith(): ¿La cadena consta solo de letras mayúsculas?