hh = int(input("Escriba la hora: "))
mm = int(input("Escriba los minutos: "))
ss = int(input("Escriba los segundos: "))

ss = ss + 1
if(ss > 59 ):
    mm = mm + 1
    ss = 0

if(mm > 59):
    hh = hh + 1
    mm = 0
    
if(hh > 23):
    hh = 0


print(hh, mm, ss, sep=":")
