#Diseñar una lista tipo spotofy donde se pueda buscar y agregar artistas, buscar y agregar canciones con genro y duracion,
#eliminar artistas, ordenar alfabeticamente el que tiene mas canciones, la que tiene la duracion mas larga, el que tiene la duracion
#mas corta.


k=str(input('que desa hacer en spotify: '))


nuevoartista={
    'artista nuevo':{

    },
    'nueva cancion':{

    },
    'g y d':{

    }
}

chayanne={
    'dejaria todo':{
        'dejaria todo':{
            'genero':'romantico',
            'duracion':'3:30'
        }
    },
    'torero':{
        'torero':{
            'genero':'romantico',
            'duracion':'3:20'
        }
    },  
    'un siglo sin ti':{
        'un siglo sin ti':{
            'genero':'romantico',
            'duracion':'4:20'
        }
    },    
    'fiesta en america':{
        'fiesta en america':{
            'genero':'pop',
            'duracion':'5:15'
        }
    },   
    'humanos a marte':{
        'humanos a marte':{
            'genero':'romantico',
            'duracion':'3:58'
        }
    }   
}

badbunny={
    'me porto bonito':{
        'me porto bonito':{
            'genero':'regton',
            'duracion':'3:02'
        }
    },
    'efecto':{
        'efecto':{
            'genero':'regeton',
            'duracion':'4:10'
        }
    },
    'diles':{
        'diles':{
            'genero':'trap',
            'duracion':'5:30'
        }
    },
    'callaita':{
        'callaita':{
            'genero':'regeton',
            'duracion':'2:22'
        }
    },
    'te bote':{
        'te bote':{
            'genero':'regeton',
            'duracion':'6:46'
        }
    }
}

icecube={
    'It Was a Good Day':{
        'It Was a Good Day':{
            'genero':'rap',
            'duracion':'5:20'
        }
    },
    'You Know How We Do It':{
        'You Know How We Do It':{
            'genero':'rap',
            'duracion':'3:20'
        }
    },
    'Check Yo Self':{
        'Check Yo Self':{
            'genero':'rap',
            'duracion':'4:20'
        }
    },
    'Fuck Tha Police':{
        'Fuck Tha Police':{
            'genero':'rap',
            'duracion':'5:02'
        }
    },
    'Gangsta Nation':{
        'Gangsta Nation':{
            'genero':'rap',
            'duracion':'6:20'
        }
    }
}
busca='buscar un artista'
elima='eliminar un artista'
agrea='agregar un artista'
agrec='agregar una cancion'

if k=='buscar una cancion':
    buscarc=str(input('Escriba una cancion: '))
    def busqueda1(diccionario, elem):
         if elem in chayanne.keys():
             print(chayanne[elem])
    busqueda1(chayanne,buscarc)
    def busqueda2(diccionario, elem):
         if elem in badbunny.keys():
             print(badbunny[elem])
    busqueda2(badbunny,buscarc)
    def busqueda3(diccionario, elem):
         if elem in icecube.keys():
             print(icecube[elem])
    busqueda3(icecube,buscarc)



elif k==busca:
    buscara=str(input('Escribe un artista: '))
    if buscara=='chayanne':
        print('Canciones de chayanne: ')
        print(chayanne['dejaria todo'])
        print(chayanne['fiesta en america'])
        print(chayanne['humanos a marte'])
        print(chayanne['torero'])
        print(chayanne['un siglo sin ti'])
    elif buscara=='badbunny':
        print('Canciones de badbunny: ')
        print(badbunny['callaita'])
        print(badbunny['diles'])
        print(badbunny['efecto'])
        print(badbunny['me porto bonito'])
        print(badbunny['te bote'])
    elif buscara=='icecube':
        print('Canciones de ice cube')
        print(icecube['Check Yo Self'])
        print(icecube['Fuck Tha Police'])
        print(icecube['Gangsta Nation'])
        print(icecube['It Was a Good Day'])
        print(icecube['You Know How We Do It'])
        
elif k==elima:
    eliminara=str(input('Escribe el nombre del artista que desees eliminar: '))
    if eliminara=='chayanne':
        del chayanne ['dejaria todo']
        del chayanne['fiesta en america']
        del chayanne['humanos a marte']
        del chayanne['torero']
        del chayanne['un siglo sin ti']
        print('repertorio actual de chayanne es: ',chayanne)
    elif eliminara=='badbunny':
        del badbunny['callaita']
        del badbunny['diles']
        del badbunny['efecto']
        del badbunny['me porto bonito']
        del badbunny['te bote']
        print('el repertorio actual de badbunny es: ',badbunny)
    elif eliminara=='icecube':
        del icecube['Check Yo Self']
        del icecube['Fuck Tha Police']
        del icecube['Gangsta Nation']
        del icecube['It Was a Good Day']
        del icecube['You Know How We Do It']
        print('el repertorio actual de icecube es: ',icecube)

elif k==agrea:
    agregara=str(input('Que artista desea agregar:'))
    nuevoartista['artista nuevo'].update({'1':agregara})

    nuevo=str(input('desea agregarle mas cosas a su nuevo artista?: '))
    if nuevo=='si':
        agregarc2=str(input('Que cancion desea agregar: '))
        genero2=str(input('De que genero es la nueva cancion? '))
        tiempo2=str(input('Cuanto tiempo dura la nueva cancion? '))

        nuevoartista['nueva cancion'].update({'2':agregarc2})
        nuevoartista['g y d'].update({'genero':genero2, 'duracion':tiempo2})
    print(nuevoartista)

elif k==agrec:
    akart=str(input('A que artista lo desea agregar? '))
    agregarc=str(input('Que cancion desea agregar: '))
    genero=str(input('De que genero es la nueva cancion? '))
    tiempo=str(input('Cuanto tiempo dura la nueva cancion? '))
    print('- La nueva cancion: ',agregarc,'\n- Del artista: ',akart,'\n- Del genero: ',genero,'\n- La cancion dura: ',tiempo)

    if akart=='chayanne':
        chayanne.update({agregarc:{'genero':genero, 'duracion':tiempo}})
        print(chayanne)
    elif akart=='badbunny':
        badbunny.update({agregarc:{'genero':genero, 'duracion':tiempo}})
        print(badbunny)
    elif akart=='icecube':
        icecube.update({agregarc:{'genero':genero, 'duracion':tiempo}})
        print(icecube)

else:
    print('escriba una accion permitida como por ejemplo:  \n - buscar una cancion\n - buscar un artista\n - eliminar un artista\n - agregar un artista\n - agregar una cancion')

deseo=str(input('Desea ver la cancion con mayor y menor duracion de cada artista:? '))
if deseo=='si':
    if (chayanne['dejaria todo']['dejaria todo']['duracion'])>(chayanne['torero']['torero']['duracion']):
        print('dejaria todo con 3:30 de duracion es la cancion mas larga')
    else:
        print('jajajja')



