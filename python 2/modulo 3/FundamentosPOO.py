#CONCEPTOS BASICOS DE POO

'''Hemos estado trabajando con progrmacion procedimental

el POO es muy joven y es muy util en proyectos grandes
que son desarrollados por equipos grandesde desarrolladores

el POO facilita tareas simples como dividir el proyecto en partes pequeñas 

el POO es relativamente simple

las funciones pueden usar datos pero no al revez
pero no es completamente cierto si hay datos y se llamas
metodos y se invocan dentro de los datos no junto a ellos

Los datos y el codigo estan encapsulados juntod en el mismo mundo
divididos por clases cada clase es como una receta que se puede
usar cuando quieras crear un objeto util, se puede
crear tanto objetos como necesites

Cada objeto tiene un conjunto de rasgos(atributos) y es capaz
de realizar un conjunto de actividades(metodos)

Las recetas pueden modificarse y se pueden crear nuevas
clases que heredan propiedades y metodos de los originalees
y agrgan nuevos, creando nuevas herramientas

Los objetos interactuan entre si, intercambian datos o activan sus
metodos, una clase bien construida puede proteger  los datos
y ocultarlos de modificaciones no autorizadas
'''

# JARARQUIA DE CLASE

'''La definicion de clse que usaremos es como una 
categoria, como resultado de similitudes definidas 
con precision

para entender las clases veamos este ejemplo:

Veamos por un momento los vehículos. Todos los 
vehículos existentes (y los que aún no existen) están 
relacionados por una sola característica importante: 
la capacidad de moverse. Puedes argumentar que un perro 
también se mueve; ¿Es un perro un vehículo? No lo es. 
Tenemos que mejorar la definición, es decir, enriquecerla con
otros criterios, distinguir los vehículos de otros 
seres y crear una conexión más fuerte. Consideremos las 
siguientes circunstancias: los vehículos son entidades 
creadas artificialmente que se utilizan para el 
transporte, movidos por fuerzas de la naturaleza y 
dirigidos (conducidos) por humanos.

ahora La clase Veiculos es muy amplia, debemos de definir
clases especializadas que seran llamadas subclases, y la
clase Veiculos sera una superclase para las subclases.

las jerarquias crece de arriba hacia abajo 

Ya podemos sacar algunas 
'''
#QUE CONTIENE UN OBJETO

'''

Un objeto tiene tres atributos:

- el nombre que lo identifica (sustantivo)
- un conjunto de propiedades individuales que lo hace 
unico (adjetivo)
- un conjunto de habilidades para relaizar actividadees 
espeificas (verbo)

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

3. Los objetos están equipados con:

Un nombre que los identifica y nos permite distinguirlos.
Un conjunto de propiedades (el conjunto puede estar vacío).
Un conjunto de métodos (también puede estar vacío).

4. Para definir una clase de Python,se necesita usar la 
palabra clave reservada class. Por ejemplo:

class This_Is_A_Class:
     pass


5. Para crear un objeto de la clase previamente definida, se 
necesita usar la clase como si fuera una función. Por 
ejemplo:

this_is_an_object = This_Is_A_Class()

'''









