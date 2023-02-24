try:
#se utiliza la palabra try para poder analizar y evaluar los errores de lo que sigue de codigo 

    raise SyntaxError
#el raise se utiliza para simular un error que tenga como indise  (raise(error x))

except SyntaxError:
#en esta linea lo que se hace es que se utiliza un except para poder interactuar con el error, cada vez que la consola suelte ese error estara en el except co intercambia por el print

    print('Cierra el parentesis')
#este es el valor por el cual el error sera intercambiado en este caso una cadena