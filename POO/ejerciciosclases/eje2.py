#Crea una clase llamada Cuenta con atributos titular y saldo. 
#Crea métodos para depositar y retirar dinero, y otro método para 
#mostrar el saldo actual de la cuenta.

d = str(input("Desea depocitar o retirar dinero? "))


class Cuenta:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def get_depositar(self):

        cantidadDepocito = float(input("Que cantidad de dinero desea depocitar: "))
        return 'En su cuenta ahora existen: ',self.saldo + cantidadDepocito
    
    def get_retirar(self):

        cantidadRetiro = float(input("Que cantidad de dinero desea depocitar: "))
        return 'acaba de retitar: ',cantidadRetiro,'actualmente su cuanta cunta con:',self.saldo - cantidadRetiro
    
    def get_saldo(self):
        return 'su saldo actual es de: ',self.saldo

ob = Cuenta('Victor Prieto',10000000)

if d == 'retirar':
    print(ob.get_retirar())
elif d == 'depocitar':
    print(ob.get_depositar())
elif d == 'ver saldo':
    print(ob.get_saldo())
else:
    print('el valor que nos ha dicho no es valido, los valores validos son: ver saldo, retirar, depocitar')






