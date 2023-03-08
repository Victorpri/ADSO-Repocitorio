

class Persona:
    def __init__(self,Id,name,edad,contact,user_name,password,accion):
        self.id=Id
        self.name=name
        self.edad=edad
        self.contact=contact
        self.__user_name=user_name
        self.__password=password
        self.accion=accion

    def set_Id(self,id):
        self.id=id

    def set_nombre(self,new_nombre):
        self.nombre=new_nombre

    def set_edad(self,new_edad):
        self.edad=new_edad

    def set_contact(self,new_contact):
        self.contact=new_contact

    def set_user_name(self,new_user_name):
        self.__user_name=new_user_name

    def set_password(self,new_password):
        self.__password=new_password
        
    def set_accion(self,new_accion):
        self.accion=new_accion
        
    def inicio_secion(self):
        n=str(input('escriba su nombre de usuario: '))
        if n == self.__user_name:
            p =str(input('Escriba su contraseña: '))
            if p == self.__password:
                print('Bienvenido!!!')
                que_hacer=str(input('Que desea hacer en nuestro sistema: \n 1. agregar una materia \n 2. ver las materias \n 3. agragar materias al instructor \n 4. Cambiar de curso \n 5. cambiar de unstructor una materia \n'))
                if que_hacer =='1':
                    materia_nueva=str(input('que materia nueva desea colocar: '))
                    codigo_nueva=str(input('que codigo le desea cologar a la nueva materia: '))
                    print(ob3.agregar(materia_nueva,codigo_nueva))
            else:
                    print('La contraseña es incorrecta por favor intente de nuevo')
        else:
                print('El nombre de usuario es incorrecto')






        
        
    
    






















class Instuctores(Persona):
    def __init__(self,Id,name,edad,contact,user_name,password,accion,materia):
     
        self.id=Id
        self.name=name
        self.edad=edad
        self.contact=contact
        self.__user_name=user_name
        self.__password=password
        self.accion=accion
        self.materia=materia
        
        

    def set_materias(self,new_materias):
        self.materia=new_materias

    def info_credneciales(self):
        cre=self.id
        invertir=cre[::-1]
        return 'su credencial es: ',invertir,'y dicta la materia(s) de: ',self.materia, 
        
    
    
    
class Estuediantes(Persona):
    def __init__(self, Id, name, edad, contact, user_name, password,curso,accion):
        self.id=Id
        self.name=name
        self.edad=edad
        self.contact=contact
        self.__user_name=user_name
        self.__password=password
        self.accion=accion
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

    def agregar(self,new1,new2):
        self.new_materia.append(new1)
        self.new_codigo.append(new2)

    def info_materias(self,name):
        if name == self.materia:
            print('la materia que buscas es:',self.materia,'y tiene el id de: ',self.id)

class cursos:
    def __init__(self,Id,descripcion,nivel_año):
        self.id=Id
        self.descripcion=descripcion
        self.nivel_año=nivel_año





ob1=Persona('123456789','Victor',18,3137647669,'Vicpro','sus',1)
ob2=Instuctores('123456789','Victor',18,3137647669,'Vicpro','sus','programacion',1)
ob3=Materias(12,'Mate','muy buena','jose','todos los dias')


print(ob1.inicio_secion())


'''print(ob2.info_credneciales())
print(ob2.set_materias('a'))
print(ob2.__dict__)'''












