#Crea una clase llamada Persona con atributos nombre, edad y sexo. 
#Crea un método saludar() que muestre un mensaje de saludo con el 
#nombre de la persona.


class Persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def get_saludo(self,):
        return 'hola',self.nombre,'tienes',self.edad,'años y tu sexo es el:',self.sexo
     

ob = Persona('Victor',18,'Masculino')
print(ob.get_saludo())