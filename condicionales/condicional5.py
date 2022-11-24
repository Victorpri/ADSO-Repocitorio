p1 = input("¿Colon descubrió América?: ")
r1 = "si"

if(p1 == r1):
    print("pregunta 1 contestada correctamente")
else:
    print("pregunta 1 contestada incorrectamente" )
    exit("perdiste")

p2 = input("¿La independencia de Colombia fue en el año 1815?: ")
r2 = "no"

if(p2 == r2):
    print("pregunta 2 contestada correctamente")
else:
    print("pregunta 2 contestada incorrectamente")
    exit("perdiste")

p3 = input("¿The Doors fue un grupo de rock Americano?: ")
r3 = "si"

if(p3 == r3):
    print("pregunta 3 contestada correctamente")
    exit("ganaste")
else:
    print("pregunta 3 contestada incorrectamente")
    exit("perdiste")