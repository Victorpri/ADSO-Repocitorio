class Vehiculo:                                                                   # crea la clase vehiculo que en este caso en la super o el padre 
    def __init__(self,tipo):
        self.tipo=tipo                                                            # un metodo  para tener la descripcion del viculo en este caso solo el tipo 
    def descripcion(self):
        print('Soy generico no tengo descripcion',self.tipo)                      # imprime que tipo de vehiculo es 
#v=Vehiculo('Cualquier tipo')

    def getTipo(self):                                                            # un metodo para agregar o gaurdarel tipo 
        return self.tipo                                                          # retorna el tipo de veilocolo oposea lo que agrego 
        #return Vehiculo.tipo
    def __str__(self):                                                            # este metodo es un metodo que trae python pero se puede re escribir 
        return 'Soy objeto de la clase Vehiculo'                                  # esto es lo que hace lo re escribe osea re escribe el mensaje para asi tenaer un identificador 

class Herramienta:                                                                # crea la calse herramienta 
    def __init__(self,proposito):                                                 # el contructor 
        self.__proposito=proposito                                                # guarda su proposito
    
    def getProposito(self):                                                       # get para agregar el proposito 
        return self.__proposito                                                   # retorna el prposito que se guardo en el __init__
    
    def __str__(self):                                                            # este metodo es un metodo que trae python pero se puede re escribir 
        return 'Soy objeto de la clase Vehiculo'                                  # en este caso lo que hace es re escribir osea re escribe el mensaje para asi tenaer un identificador

class Terrestre(Vehiculo,Herramienta):                                            # se crea otra calse con herencia de veiculo y herramienta va a actuar jerarquica mente depediendo de 
                                                                                  # actuara depende de la posiicion
    def __init__(self,tipo,proposito):                                            # consturctor 
        Herramienta.__init__(self,proposito)                                      # declara el init de la calse herramienta 
        Vehiculo.__init__(self,tipo)                                              # declara el init de la clase veiculo 
    def datos(self):                                                              
        print('Tipo: ',super().getTipo())                                         # llama gettipo de la clase veiculo  
        print('Tipo: ',super().getProposito())                                    # llama getProposito de la clase herramienta 
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga")
t.datos()
print(t.__str__())

