#pida un número al usuario (0 a 365) y diga a qué mes y dia corresponde del año.

numero = int(input("Digite un número de 1 a 365 para saber qué mes y día del año es"))

if numero < 0:
    print("número erroneo")
elif numero < 31:
    print("es",numero,"de enero")
elif numero < 60:
    print("es",numero - 31,"de febrero") # 31 + 28 = 59
elif numero < 91:
    print("es",numero - 59,"de marzo") # 59 + 31 = 90
elif numero < 121:
    print("es",numero - 90,"de abril") # 90 + 30 = 120
elif numero < 152:
    print("es",numero - 120,"de mayo") # 120 + 31 = 151
elif numero < 182:
    print("es",numero - 151,"de junio") # 151 + 30 = 181
elif numero < 213:
    print("es",numero - 181,"de julio") # 181 + 31 = 212
elif numero < 244:
    print("es",numero - 212,"de agosto") # 212 + 31 = 243
elif numero < 274:
    print("es",numero - 243,"de septiembre") # 243 + 30 = 273
elif numero < 305:
    print("es",numero - 273,"de octubre") # 273 + 31 = 304
elif numero < 335:
    print("es",numero - 304,"de noviembre") # 304 + 30 = 334
elif numero < 366:
    print("es",numero - 334,"de diciembre") # 334 + 31 = 365
elif numero > 365:
    print("El número excede los límites")
    

