#CONCEPTOS BASICOS DE POO

'''Hemos estado trabajando con programacion procedimental
el POO es muy joven y es muy util en proyectos grandes
que son desarrollados por equipos grandes de desarrolladores
el POO facilita tareas simples como dividir el proyecto en partes pequeñas
el POO es relativamente simple
las funciones pueden usar datos pero no al revez
pero no es completamente cierto si hay datos y se llamas
métodos y se invocan dentro de los datos no junto a ellos
Los datos y el codigo estan encapsulados junto con el mismo mundo
divides por clases cada clase es como una receta que se puede
usar cuando quieras crear un objeto util, se puede
crear tanto objetos como necesites
Cada objeto tiene un conjunto de rasgos(atributos) y es capaz
de realizar un conjunto de actividades(métodos)
Las recetas pueden modificarse y se pueden crear nuevas
clases que heredan propiedades y metodos de los originales
y agrgan nuevas, creando nuevas herramientas
Los objetos interactuan entre si, intercambian datos o activan sus
metodos, una clase bien construida puede proteger los datos
y ocultar las modificaciones no autorizadas
'''

#JARARQUIA DE CLASE

'''La definicion de clse que usaremos es como una
categoria, como resultado de similitudes definidas
con precisión
para entender las clases veamos este ejemplo:
Veamos por un momento los vehículos. Todos los
vehículos existentes (y los que aún no existen) están
relacionados por una sola caracteristica importante:
la capacidad de movimiento. Puedes argumentar que un perro
también se mueve; ¿Es un perro un vehículo? No lo es.
Tenemos que mejorar la definición, es decir, enriquecerla con
otros criterios, distinguir los vehiculos de otros
seres y crear una conexión más fuerte. Consideramos las
siguientes circunstancias: los vehículos son entidades
creadas artificialmente que se utilizan para el
transporte, movidos por fuerzas de la naturaleza y
dirigidos (conducidos) por humanos.
ahora La clase Veiculos es muy amplia, debemos de definir
clases especializadas que seran llamadas subclases, y la
clase Veiculos sera una superclase para las subclases.
las jerarquias crecen de arriba hacia abajo
Ya podemos sacar algunas
'''
#QUE CONTIENE UN OBJETO

'''
Un objeto tiene tres atributos:
- el nombre que lo identifica (sustantivo)
- un conjunto de propiedades individuales que lo hace
único (adjetivo)
- un conjunto de habilidades para relaizar actividadees
especifica (verbo)
'''

#RESUMEN

'''
1. Una clase es una idea (más o menos abstracta) que
se puede utilizar para crear varias encarnaciones;
una encarnación de este tipo se denomina objeto.
2. Cuando una clase se deriva de otra clase, su relación
se denomina herencia. La clase que deriva de la otra
clase se denomina subclase. El segundo lado de esta
relación se denomina superclase. Una forma de presentar
dicha relación es en un diagrama de herencia, donde:
Las superclases siempre se presentan encima de sus subclases.
Las relaciones entre clases se muestran como flechas dirigidas
desde la subclase hacia su superclase.
3. Los objetos estan equipados con:
Un nombre que los identifica y nos permite distinguirlos.
Un conjunto de propiedades (el conjunto puede estar vacío).
Un conjunto de métodos (también puede estar vacío).
4. Para definir una clase de Python, se necesita usar la
clase de palabra clave reservada. Por ejemplo:
clase Esta_es_una_clase:
     aprobar
5. Para crear un objeto de la clase previamente definida, se
necesita usar la clase como si fuera una función. por
ejemplo:
this_is_an_object = This_Is_A_Class()
'''







'''
existen dos tipos de variables:

diferencias:

Pues bien, siguiendo este símil, cualquier propiedad o información atribuible al concepto de ser humano se recoge en variables de clase y son comunes a todos los individuos.

Por otro lado, cualquier propiedad o información atribuible a cada uno de los individuos y particular a cada uno de ellos se recoge en variables de instancia.

____________________________________________________________________________________________________________________________________________________________________________________________________
variables de instancia:

representan la información particular de cada una de las instancias de una clase, como por ejemplo, el nombre de cada ser humano, el color de una silla o el importe total 
de una factura.

ejemplo:

Vamos a verlo con un ejemplo. Crearemos una clase para representar un semáforo de tráfico. La información que nos interesa almacenar es su estado actual, que es su color, 
es decir, si su luz está en rojo, en amarillo o en verde. Con esto creamos la clase Semaforo inicializando su variable luz a rojo (por defecto cualquier semáforo recién 
creado tendrá su luz en rojo). Proporcionaremos además un método cambiar para poder cambiar su luz cuando lo necesitemos

Desde el momento en que la variable está creada e inicializada podemos acceder a ella a través del nombre del objeto o de la instancia. Por supuesto, previamente hay que crear 
dicha instancia. Además, podremos invocar a la función de cambio de estado para alterar el valor de dicha variable. A continuación creamos dos instancias diferentes, cambiamos 
la luz a una de ellas y mostramos por pantalla el color de la luz de cada instancia

Es importante notar que, en el ejemplo anterior, existen dos instancias diferentes de la misma clase, es decir, dos semáforos diferentes, donde cada uno mantiene su luz de manera individual.
Modificar una variable de instancia no implica en ningún caso un cambio en las variables de otras instancias.


class Semaforo:

	def __init__(self):
		self.luz = 'Rojo' #creamos e inicializamos la variable de instancia

	def cambiar(self, nuevo_estado):
		self.luz = nuevo_estado #cambiamos el valor de la variable de instancia



 ____________________________________________________________________________________________________________________________________________________________________________________________________
 variables de clase:

 Las variables de clase representan información que es común para todas las instancias de una clase.

 La manera más sencilla de definir una variable de clase es hacerlo dentro de la clase pero fuera de las funciones. Para ver esto vamos a definir una clase 
 para representar perros. Cada perro tendrá su nombre, que como ya sabes, podrá ser representado por una variable de instancia, pero además queremos guardar el tipo de animal 
 que es, en este caso, mamífero. Como todos los perros son mamíferos indiscutiblemente, esta valor lo guardaremos en una variable de clase

 
 class Perro:

	tipo_de_animal = 'Mamífero' #se define la variable de clase

	def __init__(self, nombre):
		self.nombre = nombre #se define la variable de instancia


 ____________________________________________________________________________________________________________________________________________________________________________________________________

__dict__:

Los objetos de Python, cuando se crean, están dotados de un pequeño conjunto de propiedades y métodos predefinidos. Cada objeto los tiene, los quieras o no. Uno de ellos es una 
variable llamada __dict__ (es un diccionario).

La variable contiene los nombres y valores de todas las propiedades (variables) que el objeto contiene actualmente.

Se puede acceder al valor de una variable de clase partiendo de la propia clase o de una instancia de dicha clase, como veremos a continuación:
'''

#FUCION hasattr

'''
Python proporciona una función que puede verificar con seguridad si algún objeto / clase contiene una propiedad específica. La función se llama hasattr, y espera que le pasen 
dos argumentos:

La clase o el objeto que se verifica.
El nombre de la propiedad cuya existencia se debe informar (Nota: debe ser una cadena que contenga el nombre del atributo).

La función retorna True o False

también puede operar en clases. Puedes usarla para averiguar si una variable de clase está disponible,

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))


La función devuelve True si la clase especificada contiene un atributo dado, y False de lo contrario.

Una función llamada hasattr() se puede utilizar para determinar si algún objeto o clase contiene cierta propiedad especificada.

____________________________________________________________________________________________________________________________________________________________________________________________________

'''

#metodos de poo:

'''
Como ya sabes, un método es una función que está dentro de una clase.

Existe un requisito fundamental: un método está obligado a tener al menos un parámetro (no existen métodos sin parámetros; un método puede invocarse sin un argumento, 
pero no puede declararse sin parámetros).

El primer (o único) parámetro generalmente se denomina self

La función Self ofrece un modo de cálculo para hacer referencia al contenido del objeto con el que está asociado sin tener que hacer referencia explícitamente al objeto. 
Con Self, puede crear una única fórmula de cálculo que se puede aplicar a los distintos objetos.





'''

'''

Como ya sabes, un método es una función que está dentro de una clase.

Si deseas que el método acepte parámetros distintos a self, debes:

Colocarlos después de self en la definición del método.
Pasarlos como argumentos durante la invocación sin especificar self.
Justo como aqui:

class Classy:
    def method(self, par):
        print("método:", par)


obj = Classy()
obj.method(1)
obj.method(2)
obj.method(3)

El parámetro self es usado para obtener acceso a la instancia del objeto y las variables de clase.

class Classy:
    varia = 2
    def method(self):
        print(self.varia, self.var)


obj = Classy()
obj.var = 3
obj.method()


El parámetro self también se usa para invocar otros métodos desde dentro de la clase.

Justo como aquí:

class Classy:
    def other(self):
        print("otro")

    def method(self):
        print("método")
        self.other()


obj = Classy()
obj.method()


Si se nombra un método de esta manera: __init__, no será un método regular, será un constructor.

Si una clase tiene un constructor, este se invoca automática e implícitamente cuando se instancia el objeto de la clase.

El constructor:

Esta obligado a tener el parámetro self (se configura automáticamente).
Pudiera (pero no necesariamente) tener mas parámetros que solo self; si esto sucede, la forma en que se usa el nombre de la clase para crear el objeto debe tener la definición
 __init__.
Se puede utilizar para configurar el objeto, es decir, inicializa adecuadamente su estado interno, crea variables de instancia, crea instancias de cualquier otro objeto si es 
necesario, etc.
____________________________________________________________________________________________________________________________________________________________________________________________________

'''
#SOBREESCRITURA

'''
 Para ello es requisito indispensable que ambos métodos compartan el mismo nombre. Así, Python llamará de acuerdo al flujo de ejecución, al método de la subclase o clase hija 
 en lugar de a su homónimo en la superclase o clase padre, cuando dicho flujo de ejecución alcance en su descenso a la clase hija.

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def mostrarNombre(self):
        print("El nombre de la PERSONA es",self.nombre)
class Encargado:
    def __init__(self,codigoEncargado,departamento):
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento

class EstudianteEncargado(Persona,Encargado):
    def __init__(self,nombre,edad,clave,calificacion,codigoEncargado,departamento):
        Persona.__init__(self,nombre,edad)
        Encargado.__init__(self,codigoEncargado,departamento)
        self.clave=clave
        self.calificacion=calificacion
        self.codigoEncargado=codigoEncargado
        self.departamento=departamento

class Estudiante(Persona):
    def __init__(self,nombre,edad,clave,calificacion):
        Persona.__init__(self,nombre,edad)
        self.clave=clave
        self.calificacion=calificacion
estudianteEncargado1=EstudianteEncargado("Juan",22,"0232",10,"0233","Sistemas")
estudianteEncargado1.mostrarNombre()

#print("Nombre",estudianteEncargado1.nombre,"Departamento",estudianteEncargado1.departamento)

juan=Persona("Juan",22)
print("juan.edad",juan.edad)
maria=Estudiante("Maria",23,"2222",10)
print("maria clave",maria.clave)



'''






#HERENCIA

'''



'''





'''
#polimorfismo



es basicamente que dos metodos con el mismo nombre hagan cosas distientas eje:
'''

class carro:
    def atri(self):



