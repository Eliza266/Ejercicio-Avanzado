import os
def crearMenu():
    titulo= """
        +++++++++++++++++++++++++++++++++++++++++
        +     TORNEO DE TENIS DE MESA           +
        +++++++++++++++++++++++++++++++++++++++++
        """
    print(titulo)
    listMenu=[1,2,3,4,5]

    try:
        print(" 1.Registro de Jugadores\n 2.Registrar Encuentro\n 3.Informe de Jugadores\n 4.Ganadores por Categorias\n 5.Salir")
        op=int(input('--'))
        if (op not in listMenu):
            os.system('cls')
            crearMenu()

    except:
        os.system('pause')
        crearMenu()
        
    else:
        return op