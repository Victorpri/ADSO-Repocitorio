
class Persona1:#creo clase persona osea clase padre la principal 
    
    def __init__(self,nombre,tipo,cedu):#consturtor con tres argumentos o datos basicos como nombre tipo de documento y numero de documento 
        self.__nombre1=nombre
        self.__tipo1=tipo
        self.__cedu1=cedu
        

        #print('Constructor Activado')        
    def getNombre(self):#este metodo o funcion es para ver la informacion 
        t=self.__tipo1                                                   #guardo tipo1 en t
        c=self.__cedu1                                                   #guardo cedu1 en c
        n=self.__nombre1                                                 #guardo nombre1 en n
        print("nombre :",n,"\ntipo de documento :",t,"\nnumero de indentificacion :",c)
        
        

    def setNombre(self,nunombre):#este metodo es para cambiar el nombre 
        an=self.__nombre1                                              #guardo el nomre antiguo en an         
        self.__nombre1=nunombre                                        #ramplaso en nombre antiguo con el nuevo 

        n=self.__nombre1                                               #solo guador el nombre nuevo para no inprimir el nombre1

        print("la persona:",an,"cambio su nombre a :",n)
    
    def setipo(self,nuvotipo):# este metodo es para cambiar el tipo de documento 
        at=self.__tipo1                                                         #aca guardo en at el tipo de documeto antiguo 
        self.__tipo1=nuvotipo                                                   #aca remplaso el nuevo tipo 
        nuevot=self.__tipo1                                                     #aca guardo tipo1 en nuevot para no imprimir el tipo uno 
        
        n=self.__nombre1

        print("la persona:",n,"cambio su tipo de documento :",at, "a siguelte :",nuevot)
        
        
print()
ob=Persona1('Maria',"ti",123)
print()
ob.setNombre("mariam")
print()
ob.setipo("cc")


print()

class Aprendiz(Persona1):#aca creo otra calse llamada aprendiz con eredacion de la calse padre que estoy asignando llamada persona1
    def __init__(self,ficha,nombre_a,tipo_a,cedu_a):# pido 4 argumentos 
        super().__init__(nombre_a,tipo_a,cedu_a)    #este super() le dice a clase aprendiz que los argumetos que puse desde la pocicon 3
                                                    # vallan al __init__ de la calse padre que es persona1  
        self.__ficha=ficha                          # aca solo guardo la ficha 
        
    
        
    def setficha(self,ficha,nombre):# este metodo es para cambiar la ficha pido dos argumentos 
        ficha2=self.__ficha         #aca guardo la ficha enterior
        self.__nombre1=nombre       #aca guardo el nombre en nombre1
        self.__ficha=ficha          # guardo la nueva ficha 
        
        nombre1=self.__nombre1      #guarsdo el __nombre1 en nombre1 para asi no imprimir __nombre1
        
        print(nombre1,"cambio de numero de ficha que era :", ficha2,"a la siguente :",self.__ficha)
        sena1="gracias por estar en el sena "
        print(sena1)
        #print("2")
    
    
class profesor(Aprendiz,Persona1,):
    pass
      

app=Aprendiz("12345A","Ana","ti",133)
app.getNombre()
print()
app.setficha("12b","Ana")

ob2=Aprendiz("445677a",'Maria',"ti",123)
print()
ob2.getNombre()

print(isinstance(app,Aprendiz))


