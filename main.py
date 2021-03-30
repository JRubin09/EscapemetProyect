from cuartos import Cuartos
from juegos import Juegos
from jugador import Jugador
from dibujos_cuartos import *
from partida import Partida
from objetos import Objetos
from api import api_call
from frases import *
from instrucciones import *
from left_games import *
from right_games import *
from center_games import *
from narrativas import *
from closeup_dibujos import *

def records():
    print(record)

def partida_nueva():

    opcion = input('''
    Eliga la dificultad de su partida: 
    1. Facil
    2. Media
    3. Dificil
    4. Menu\n >> ''')
    while (not opcion.isnumeric()) or (int(opcion) < 1): 
        opcion = input("Ingreso invalido, ingrese una opcion valida: ")        

    if opcion == '1':
        vidas = '5'
        pistas = '5'
        tiempo = '15 minutos'
        
    elif opcion == '2':
        vidas = '3'
        pistas = '3'
        tiempo = '10 minutos'
        
    elif opcion == '3':
        vidas = '1'
        pistas = '1'
        tiempo = '5 minutos'
       
    elif opcion == '4':
        print('Adios')
        main()
    else:
        return 0

    nueva_partida = Partida(vidas, pistas, tiempo)
    # registro_jugador()
    print(nueva_partida.mostrar())
    return nueva_partida

def registro_jugador():
    username = input('Username: ')
    contrasena = input('Contrasena: ')
    edad = input('Edad: ')
    avatar = input('Elige el Avatar de tu jugador: ')
    #hacer un if y darle nombre a nuevos avatares que el jugador pueda elegir
    tiempo_partidas = []
    inventario = []

    nuevo_jugador = Jugador(username, contrasena, edad, avatar, tiempo_partidas, inventario)

    print(nuevo_jugador.mostrar())
    return nuevo_jugador
    
def comienza_partida(partida,player):
    
    print(primera_narra)
    print('Intenta Escapar')
    while True:
        try: 
            x = int(input('''En donde deseas comenzar:
    
    1 --> Laboratorio SL001               
    2 --> Biblioteca
    3 --> Plaza Rectorado\n>>'''))
            break
        except:
            print('Ingreso invalido')
    api = api_call()
    continuar = 1
    while continuar == 1:

    #Mientras este while se cumpla sigue en el juego hacer para
    #Game over y para Win! 
    #Crear condicion para que siga en el while 
    #Objetos? Vidas? 

        dic = api[x-1]
        name = dic.get('name')
        cosas = dic.get('objects')
        room = Cuartos(name)
        
        print(dibujos_rooms[x-1])
        print(f'''
            <-------   (S)   Te devuelves de cuarto      <-------
            -------> (SPACE) Avanzas al siguiente cuarto ------->
                       (P)    Para poner PAUSA ''')
        print(room.mostrar())
        movimiento = input('Hacia donde quieres ir:\n>> ').lower()

        if movimiento == 'w':
            #if award = 
            center_obj = cosas[0]
            name = center_obj.get('name')
            position = center_obj.get('position')    
            objeto_center = Objetos(name,position)
            print(objeto_center.mostrar())
            center_game = center_obj.get('game')
            name_game = center_game.get('name')
            juego = Juegos(name_game)
            print(juego.mostrar())
            print(dibujos_closeup[x-1][0])
            if (x-1) == 0:
                #SOUP HARD
                #sopa_letras(name_game,center_game)
                pass
            elif (x-1) == 1:
                #AHORCADO HARD
                # ahorcado(name_game, center_game)
                pass

            elif (x-1) == 2:
                #Solve logic
                solve_logic(name_game,center_game)
                pass

            elif (x-1) == 3:
                #LOGICA BOOLEANA ESTA HECHO REVISAR
                logic_bool(name_game,center_game)
                pass

            elif (x-1) == 4:
                #SI COMPLETA ESTE JUEGO GANA OJOOOOOOOOOOOOOO! LE PONGO UN BREAK? IDK
                #AQUI NO HAY JUEGO O LO INVENTO O ABRE ESA PUERTA Y GGWP
                pass

            else:
                pass  

        elif movimiento == 'a':
            
            left_obj = cosas[1]
            name = left_obj.get('name')
            position = left_obj.get('position')
            objeto_izq = Objetos(name,position)
            print(objeto_izq.mostrar())
            left_game = left_obj.get('game')
            name_game = left_game.get('name')
            juego = Juegos(name_game)
            print(juego.mostrar())
            print(dibujos_closeup[x-1][1])
            if (x-1) == 0:
                #preguntas sobre python
                python_game(name_game,left_game)
                pass
            elif (x-1) == 1:
                #preguntas matematica NO LO HE HECHO
                pass
            
            elif (x-1) == 2:
                #QUIZZIS
                millonario(name_game,left_game)
                #checkear award??? EN TODOSSS ALO
                pass
            elif (x-1) == 4:
                #Palabras mezcladas
                p_mezcladas(name_game,left_game)
                pass

        elif movimiento == 'd':

            right_obj = cosas[2]
            name = right_obj.get('name')
            position = right_obj.get('position')
            objeto_right = Objetos(name,position)
            print(objeto_right.mostrar())
            right_game = right_obj.get('game')
            name_game = right_game.get('name')
            juego = Juegos(name_game)
            print(dibujos_closeup[x-1][2])
            print(juego.mostrar())
            if (x-1) == 0:
                #Adivininanzas CASI HECHO CICLOS F
                adivinanzas(name_game,right_game)
                pass
            elif (x-1) == 1:
                #Criptograma HARD
                # def criptograma(name_game, right_game)

                pass
            elif (x-1) == 2:
                #MEmoria con EMOJIS should be easy
                pass
            elif (x-1) == 4:
                #RAndom number generator
                random_number(name_game, right_game)
                pass

        
        elif movimiento == ' ':

            x = x + 1
            if x > 5:
                x = x - 1
                print('No puedes avanzar mas, termina el juego tu puedes!')

        elif movimiento == 's':

            x = x - 1

        elif movimiento == 'p':

            print(partida.mostrar())
            sigue_partida = input('''
                        Desea continuar la partida: 
                        
                        (Y) --> si o (N) --> no\n
                                >>''').lower()
            if sigue_partida == 'y':
                pass
            elif sigue_partida == 'n':
                main()

        elif x > 4:
            print('No puedes avanzar mas')
            x = x - 1


def main():
    print(bienvenido)
    while True:
        opcion = input("""
        Elige una opcion: 
        1. Nueva Partida
        2. Instrucciones
        3. Records
        4. Para salir \n >> """)

        while (not opcion.isnumeric()) or (int(opcion) < 1): 
          opcion = input("Ingreso invalido, ingrese una opcion valida: ") 

        if opcion == '1':

            partida = partida_nueva()
            player = registro_jugador()
            comienza_partida(partida,player)

        elif opcion == '2':

            instrucciones()

        elif opcion == '3':

            records()

        elif opcion == '4':

            break

        else:

            print('Opcion invalida')




if __name__ == '__main__':
    main()

