def edad():
#esta es una funcion comun y corriente, no hay mucho que explicar en esta linea
    try:
#el try es para evaluar los errores del codigo
        tuedad=int(input("introduce tu edad"))
#esta es una variable que tendra el valor que el usuario quiera dar
        print(f'tu edad es  {tuedad}')
#no me acuerdo la funcion
    except ValueError as e:    
#cada que el codigo genere el error dado por el except 
        print(e)
#cuando el except se genere mostrara e que sera el error como tal
        print("La edad debe ser un valor numerico...")
#el mensaje que mostrar en vez del error
        edad()
#aca volvera a pedir la edad
    else:
        print('Viene por el else')
#no me acuerdo como se utilizaba el else en excepciones

edad()
# invoca la funcion