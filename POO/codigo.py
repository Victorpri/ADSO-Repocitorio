import random

class Persona:
    def __init__(self,Id,name,edad,contact,user_name,password):
        self.id=Id
        self.name=name
        self.edad=edad
        self.contact=contact
        self.user_name=user_name
        self.password=password

    def set_Id(self,id):
        self.id=id

    def set_nombre(self,new_nombre):
        self.nombre=new_nombre

    def set_edad(self,new_edad):
        self.edad=new_edad

    def set_contact(self,new_contact):
        self.contact=new_contact

    def set_user_name(self,new_user_name):
        self.user_name=new_user_name

    def set_password(self,new_password):
        self.password=new_password

class Instuctores(Persona):
    def __init__(self, Id, name, edad, contact, user_name, password,materia):
        super().__init__(Id, name, edad, contact, user_name, password)

        self.materia=materia

    def set_materias(self,new_materias):
        self.materia=new_materias

    def info_credneciales(self):
        cre=self.id
        invertir=cre[::-1]
        return 'su credencial es: ',invertir,'y dicta la materia(s) de: ',self.materia
    
    
    
class Estuediantes(Persona):
    def __init__(self, Id, name, edad, contact, user_name, password,curso):
        super().__init__(Id, name, edad, contact, user_name, password)
        self.curso=curso

    def set_curso(self,new_curso):
        self.curso=new_curso

class Materias:
    def __init__(self,Id,materia,descripcion,instructor,cronograma):
        self.id=Id
        self.materia=materia
        self.descripcion=descripcion
        self.instructor=instructor
        self.cronograma=cronograma
        self.new_materia=[]
        self.new_codigo=[]

    def set_instructor(self,new_instructor):
        self.instructores=new_instructor

    def agregar(self,new):
        self.new_materia.append(new)
        self.new_codigo.append(new)

    def info_materias(self,name):
        if name == self.materia:
            print('la materia que buscas es:',self.materia,'y tiene el id de: ',self.id)

class cursos:
    def __init__(self,Id,descripcion,nivel_año):
        self.id=Id
        self.descripcion=descripcion
        self.nivel_año=nivel_año


        
        




ob1=Persona('123456789','Victor',18,3137647669,'Vicpro','sus')
ob2=Instuctores('123456789','Victor',18,3137647669,'Vicpro','sus','programacion')

print(ob2.info_credneciales())
print(ob2.set_materias('matematicas'))
print(ob2.__dict__)

        

        



