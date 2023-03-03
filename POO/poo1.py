class Empleado:
    def __init__(self,nombre,cargo,salario,horasExtras):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        self.horasExtras = horasExtras
    



    def get_nombre(self):
        return self.nombre
    def get_cargo(self):
        return self.cargo
    def get_slario(self):
        return self.salario
    def get_horasExtras(self):
        return self.horasExtras
    def set_nombre(self,nombre):
        self.nombre = nombre
    def set_cargo(self,cargo):
        self.cargo = cargo
    def set_slario(self,salario):
        self.salario = salario
    def set_horasExtras(self,horasExtras):
        self.horasExtras = horasExtras


    def plata(self):
        resultado=(self.salario/20/8)
        return 'el empleado gana', resultado,'pesos por hora'

    def IPC(self):
        if self.salario == 1160000:
            salfin=(self.salario*0.16)
            return 'el aumento del salario es de: ',salfin
        elif self.salario > 1160000:
            salfin=(self.salario*0.13)
            return 'el aumento del salario es de: ',salfin
        elif self.salario < 1160000:
            return 'no se puede agegar un valor que sea mas pqueño que el minimo el cual es 1.160.000'

    def extras(self):
        if self.horasExtras > 40 or self.horasExtras < 0:
            return 'un trabajador no puede trabajar mas de 40 horas extras al mes'
        elif self.horasExtras < 40 and self.horasExtras > 0:
            pagoxhora=(self.salario/20/8)
            pagoextras=(self.horasExtras*pagoxhora)
            pagofinal=(self.salario+pagoextras)
            return 'el empleado tiene: ',pagoextras,'para conletar un salario de: ',pagofinal




ob=Empleado('victor','programador', 5000000,10)

print(ob.plata())
print(ob.IPC())
print(ob.extras())
