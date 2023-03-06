#Crea una clase llamada Rectángulo con atributos base y altura. 
#Crea métodos para calcular el área y el perímetro del rectángulo.


class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura

    def get_area(self):
        area = self.base * self.altura
        return 'el area del rectangulo es: ',area
    
    def get_perimetro(self):
        perimetro = self.base * self.altura
        return 'el perimetro del rectangulo es: ',perimetro * 2
    
ob = Rectangulo(5,10)

print(ob.get_area())
print(ob.get_perimetro())



