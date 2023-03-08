'''class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getDocumento(self):
        return self.__documento
    
    def setDocumento(self,documento):
        self.__documento=documento

ob=Persona('Ivan',1030533045)
print(ob.getNombre(),ob.getDocumento())
ob.setNombre('Goku')
ob.setDocumento(1045534768)
print(ob.getNombre(),ob.getDocumento())'''



'''escritor = '4554151'
cadenaInvertida = escritor[::-1]
print(cadenaInvertida)'''



class materias:
    def __init__(self,id,nombre,descripcion,instructor,horario):
        self.id=id
        self.nombre=nombre
        self.descripcion=descripcion
        self.instructor=instructor
        self.horario=horario
        self.nombre1=[]
    def nombre12(self,n):
        self.nombre1.append(n)
    def getNombre(self,nombre):
        if nombre == self.nombre:
            print('El id del curso es',self.id,'y el nombre del curso es', nombre)
        for i in self.nombre1 :
            if i in nombre:
                print('El id del curso es',self.id,'y el nombre del curso es', nombre)
            else:
                print('El nombre no coincide con ninguna materia del curso')


ob=materias(12341234,'mate','jsdfkajsdhfula','jose','10 a 11')
print(ob.nombre12('jajajaj'))
print(ob.nombre12('safdgasdf'))
print(ob.getNombre('mate'))
print(ob.__dict__)

