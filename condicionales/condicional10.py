
hh = float(input("Escriba la hora: "))
mm = float(input("Escriba los minutos: "))
ss = float(input("Escriba los segundos: "))

if(ss < 59 ):
    print(hh, mm, ss + 1, sep=":")

elif(ss > 58 ):
    print(hh, mm + 1, ss - ss, sep=":")

elif(mm == 59, ss == 58):
    print(hh + 1, mm - mm, ss - ss, sep=":")

elif(hh > 23, mm == 60, ss == 59):
    print(hh - hh, mm - mm, ss - ss, sep=":")




