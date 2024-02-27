from tabulate import tabulate
import os 
def registroJugador(novato:dict,intermedio:dict,avanzado:dict):
    
        print('SELECCIONE UNA CATEGORIA:')
        categoria=int(input('1.Novato\n 2.Intermedio\n 3.Avanzado\n'))
        if categoria==1:
            if len(novato)<5:
                edad=int(input('Ingrese la edad: '))
                if 15<=edad<=16:
                    id=int(input('Ingrese el ID: '))
                    nombre=input('Ingrese el nombre: ')
                    jugador={
                        'id':id,
                        'nombre':nombre,
                        'PJ':0,
                        'PG':0,
                        'PP':0,
                        'PA':0,
                        'TP':0

                }
                    novato[id]=jugador
                    print(jugador)
                    
                else:
                    print('Su edad no corresponde a la categoria')
                    registroJugador(novato,intermedio,avanzado)
            else:
                 print('Categoria Novatos se encuentra llena')
                 novatos=True
        if categoria==2:
            if len(intermedio)<5:
                edad=int(input('Ingrese la edad: '))
                if 17<=edad<=20:
                    id=int(input('Ingrese el ID: '))
                    nombre=input('Ingrese el nombre: ')
                    jugador={
                        'id':id,
                        'nombre':nombre,
                        'PJ':0,
                        'PG':0,
                        'PP':0,
                        'PA':0,
                        'TP':0

                }
                    intermedio[id]=jugador
                    
                else:
                    print('La edad no corresponde a la categoria(entre17 y 20 años)')
                    registroJugador(novato,intermedio,avanzado)
            else:
                 print('Categoria Novatos se encuentra llena')
                 intermedios=True
        if categoria==3:

            if len(avanzado)<5:
                edad=int(input('Ingrese la edad: '))
                if edad>20:
                    id=int(input('Ingrese el ID: '))
                    nombre=input('Ingrese el nombre: ')
                    jugador={
                        'id':id,
                        'nombre':nombre,
                        'PJ':0,
                        'PG':0,
                        'PP':0,
                        'PA':0,
                        'TP':0

                }
                    avanzado[id]=jugador
                    
                else:
                    print('La edad no corresponde a la categoria(mayor de 20 años')
                    registroJugador(novato,intermedio,avanzado)
            else:
                 print('Categoria Novatos se encuentra llena')
                 avanzados=True

def registrarEncuentro(novato:dict,intermedio:dict,avanzado:dict):
    opcion=int(input('Seleccione la categoria para registrar el encuentro:\n 1.Novato\n 2.Intermedio\n 3.Avanzado\n'))
    if opcion==1:
        if len(novato)==5:
            print('Selecione dos jugadores (Escriba el id): ')
            for key, value in novato.items():
                print(f" {key}:{value['nombre']}")
            A=input('A. ')
            B=input('B.')
            puntosFavorA = int(input(f'Ingrese los puntos anotados por {A}: {novato[A]["nombre"]}'))
            puntosFavorB=int(input(f'Ingrese los puntos anotados por {B}: {novato[B]["nombre"]}'))
            #PJ de A y B
            novato[A]['PJ']+=1
            novato[B]['PJ']+=1
            # PA,PG  A y B
            if puntosFavorA> puntosFavorB:
                novato[A]['PA']=(puntosFavorA-puntosFavorB)
                novato[A]['PG']+=1
                novato[A]['TP']+=2
                novato[B]['PP']+=1
            else:
                novato[B]['PA']=(puntosFavorB-puntosFavorA)
                novato[B]['PG']+=1
                novato[B]['TP']+=2
                novato[A]['PP']+=1
        else: 
            print('No se puede registrar el encuentro por falta de participantes')
    
    if opcion==2:
        if len(intermedio)==5:
            print('Selecione dos jugadores (Escriba el id): ')
            for key, value in intermedio.items():
                print(f" {key}:{value['nombre']}")
            A=input('A. ')
            B=input('B.')
            puntosFavorA = int(input(f'Ingrese los puntos anotados por {A}: {intermedio[A]["nombre"]}'))
            puntosFavorB=int(input(f'Ingrese los puntos anotados por {B}: {intermedio[B]["nombre"]}'))
            #PJ de A y B
            intermedio[A]['PJ']+=1
            intermedio[B]['PJ']+=1
            # PA,PG  A y B
            if puntosFavorA> puntosFavorB:
                intermedio[A]['PA']=(puntosFavorA-puntosFavorB)
                intermedio[A]['PG']+=1
                intermedio[A]['TP']+=2
                intermedio[B]['PP']+=1
            else:
                intermedio[B]['PA']=(puntosFavorB-puntosFavorA)
                intermedio[B]['PG']+=1
                intermedio[B]['TP']+=2
                intermedio[A]['PP']+=1
        else: 
            print('No se puede registrar el encuentro por falta de participantes')
    if opcion==3:
        if len(avanzado)==5:
            print('Selecione dos jugadores (Escriba el id): ')
            for key, value in avanzado.items():
                print(f" {key}:{value['nombre']}")
            A=input('A. ')
            B=input('B.')
            puntosFavorA = int(input(f'Ingrese los puntos anotados por {A}: {avanzado[A]["nombre"]}'))
            puntosFavorB=int(input(f'Ingrese los puntos anotados por {B}: {avanzado[B]["nombre"]}'))
            #PJ de A y B
            avanzado[A]['PJ']+=1
            avanzado[B]['PJ']+=1
            # PA,PG  A y B
            if puntosFavorA> puntosFavorB:
                avanzado[A]['PA']=(puntosFavorA-puntosFavorB)
                avanzado[A]['PG']+=1
                avanzado[A]['TP']+=2
                avanzado[B]['PP']+=1
            else:
                avanzado[B]['PA']=(puntosFavorB-puntosFavorA)
                avanzado[B]['PG']+=1
                avanzado[B]['TP']+=2
                avanzado[A]['PP']+=1
        else: 
            print('No se puede registrar el encuentro por falta de participantes')

def informeJugadores(novato:dict,intermedio:dict,avanzado:dict):
    print('********NOVATO*********\n')
    listaNovato = list(novato.values())
    print(tabulate(listaNovato, headers="keys", tablefmt="pretty"))
    print('********INTERMEDIO*********\n')
    listaIntermedio= list(intermedio.values())
    print(tabulate(listaIntermedio, headers='keys', tablefmt='pretty'))
    print('********AVANZADO*********\n')
    listaAvanzado= list(avanzado.values())
    print(tabulate(listaAvanzado, headers='keys', tablefmt='pretty'))

def ganadoresCategoria(novato:dict,intermedio:dict,avanzado:dict):

    print('Los Jugadores de la Categoria Novato: \n')
    mayorN=0
    for key, value in novato.items():
        print(f" {key}:{value['nombre']} {value['PG']}")
        if novato[key]['PG']>mayorN:
            mayorN=novato[key]['PG']
            nombreN=novato[key]['nombre']
        
    print('El Jugador con mas partidos ganados en la categoria NOVATO ES: ')
    print(f'{nombreN} con {mayorN} partidos Ganados\n')
    #--------------------------------------------------------------------------
    print('Los Jugadores de la Categoria Intermedio: \n')
    mayorI=0
    for key, value in intermedio.items():
        print(f" {key}:{value['nombre']} {value['PG']}")
        if intermedio[key]['PG']>mayorI:
            mayorI=intermedio[key]['PG']
            nombreI=intermedio[key]['nombre']
    print('El Jugador con mas partidos ganados en la categoria Intermedio ES: ')
    print(f'{nombreI} con {mayorI} partidos Ganados\n')
    #-------------------------------------------------------------------------
    print('Los Jugadores de la Categoria Avanzado: \n')
    mayorA=0
    nombre=''
    for key, value in avanzado.items():
        print(f" {key}:{value['nombre']} {value['PG']}")
        if avanzado[key]['PG']>mayorA:
            mayorA=avanzado[key]['PG']
            nombreA=avanzado[key]['nombre']
    print('El Jugador con mas partidos ganados en la categoria Avanzado ES: ')
    print(f'{nombreA} con {mayorA} partidos Ganados')
    os.system('pause')


