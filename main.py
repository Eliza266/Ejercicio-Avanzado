import json
import modulos.menu as mp
import modulos.registro as re
if __name__ == '__main__':
    # Los jugadores ya queados son para pruebas 
    novato={
        '123':{       
            'id':123,
            'nombre':'juan',
            'PJ':0,
            'PG':10,
            'PP':0,
            'PA':0,
            'TP':0
            },
        '456':{       
            'id':456,
            'nombre':'jelias',
            'PJ':0,
            'PG':2,
            'PP':0,
            'PA':0,
            'TP':0
            }
            
    }
    intermedio={
        '852':{       
            'id':123,
            'nombre':'Eliza',
            'PJ':0,
            'PG':1,
            'PP':0,
            'PA':0,
            'TP':0
            },
        '632':{       
            'id':456,
            'nombre':'Pedro',
            'PJ':0,
            'PG':3,
            'PP':0,
            'PA':0,
            'TP':0
            }
    }
    avanzado={
        '147':{       
            'id':147,
            'nombre':'mateo',
            'PJ':0,
            'PG':10,
            'PP':0,
            'PA':0,
            'TP':0
            },
        '357':{       
            'id':357,
            'nombre':'lucas',
            'PJ':0,
            'PG':2,
            'PP':0,
            'PA':0,
            'TP':0
            }
    }
    principal=True
    while principal:
        op=mp.crearMenu()
        if (op==1):
             rJugador=True
             while rJugador:
                re.registroJugador(novato,intermedio,avanzado)
                rJugador=bool(input('Ingrese S(si) si desea agregar otro Jugador o enter(No)'))
                 
        elif (op==2):
            re.registrarEncuentro(novato,intermedio,avanzado)
            print(len(novato))
        elif (op==3):
            re.informeJugadores(novato,intermedio,avanzado)
        elif (op==4):
            re.ganadoresCategoria(novato,intermedio,avanzado)
        elif (op==5):
            principal=False

    print(json.dumps(novato, indent=4))
