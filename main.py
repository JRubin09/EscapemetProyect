from cuartos import Cuartos
from juegos import Juegos
from jugador import Jugador
from dibujos_cuartos import *
from partida import Partida
from objetos import Objetos
from api import api_call,buen_continue
from frases import *
from instrucciones import *
from left_games import *
from right_games import *
from center_games import *
from closeup_dibujos import *

def records():
    print(record)

def partida_nueva():

    print(nueva)
    opcion = input('''
    Eliga la dificultad de su partida: 
    1. Facil
    2. Media
    3. Dificil
    4. Menu\n >> ''')
    while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        opcion = input("Ingreso invalido, ingrese una opcion valida: ")        

    if opcion == '1':

        print(easy)
        vidas = '5'
        pistas = '5'
        tiempo = '15 minutos'
        
    elif opcion == '2':

        print(medio)
        vidas = '3'
        pistas = '3'
        tiempo = '10 minutos'
        
    elif opcion == '3':

        print(hard)
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
    # print(nueva_partida.mostrar())
    return nueva_partida

def registro_jugador():
    username = input('Username: ')
    contrasena = input('Contrasena: ')
    edad = input('Edad: ')
    avatar = input('Elige el Avatar de tu jugador: ')
    #hacer un if y darle nombre a nuevos avatares que el jugador pueda elegir
    tiempo_partidas = []
    #agrego al inventario objetos que no tengo hecho los juegos de una vez para probar el juego
    inventario = '.'

    nuevo_jugador = Jugador(username, contrasena, edad, avatar, tiempo_partidas, inventario)
    # print(nuevo_jugador.mostrar())
    return nuevo_jugador
    
def comienza_partida(partida,player):

    player.agrego_objeto('carnet')
    player.agrego_objeto('cable HDMI')
    player.agrego_objeto('Mensaje: Si estas gradudado puedes pisar el Samán')
    player.agrego_objeto("libro de Matemáticas")
    player.agrego_objeto("martillo")
    player.agrego_objeto(["Titulo Universitario","Mensaje"])
    player.agrego_objeto('llave')
    
    print(primera_narra)
    print(ready)
    buen_continue()
    
    x = 1
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
            # print(juego.mostrar())
            print(dibujos_closeup[x-1][0])
            valido_requirement = player.check_inventario(center_game.get('requirement'))
            # print(valido_requirement)
            if valido_requirement == True or center_game.get('requirement') == False:
                    
                if (x-1) == 0:
                    #SOUP HARD
                    #sopa_letras(name_game,center_game,player)
                    pass
                elif (x-1) == 1:
                    #AHORCADO HARD
                    # ahorcado(name_game, center_game,player)
                    pass

                elif (x-1) == 2:
                    #Solve logic
                    solve_logic(name_game,center_game,player)
                    pass

                elif (x-1) == 3:
                    #LOGICA BOOLEANA ESTA HECHO REVISAR
                    logic_bool(name_game,center_game,player)
                    pass

                elif (x-1) == 4:
                    #SI COMPLETA ESTE JUEGO GANA OJOOOOOOOOOOOOOO! LE PONGO UN BREAK? IDK
                    #AQUI NO HAY JUEGO O LO INVENTO O ABRE ESA PUERTA Y GGWP
                    pass

                else:
                    pass  

            else:
                print(f'Lo siento no puedes pasar, necesitas -->', center_game.get('requirement'))
                buen_continue()            
                

        elif movimiento == 'a':

            left_obj = cosas[1]
            name = left_obj.get('name')
            position = left_obj.get('position')
            objeto_izq = Objetos(name,position)
            print(objeto_izq.mostrar())
            left_game = left_obj.get('game')
            name_game = left_game.get('name')
            juego = Juegos(name_game)
            # print(juego.mostrar())
            print(dibujos_closeup[x-1][1])
            valido_requirement = player.check_inventario(left_game.get('requirement'))
            # print(player.mostrar())
            # print(valido_requirement)
            # print(left_game.get('requirement'))
            if valido_requirement == True or left_game.get('requirement') == False:

                if (x-1) == 0:

                    #preguntas sobre python
                    python_game(name_game,left_game,player)
                    pass

                elif (x-1) == 1:
                    #preguntas matematica NO LO HE HECHO
                    pass
                
                elif (x-1) == 2:
                    #QUIZZIS
                    millonario(name_game,left_game,player)
                    #checkear award??? EN TODOSSS ALO
                    pass

                elif (x-1) == 4:
                    #Palabras mezcladas
                    p_mezcladas(name_game,left_game,player)
                    pass

            else:
                print(f'Lo siento no puedes pasar, necesitas -->', left_game.get('requirement'))
                buen_continue()            

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
            valido_requirement = player.check_inventario(right_game.get('requirement'))
            # print(valido_requirement)
            # print(juego.mostrar())
            if valido_requirement == True or right_game.get('requirement') == False:

                if (x-1) == 0:
                    #Adivininanzas CASI HECHO CICLOS F
                    adivinanzas(name_game,right_game,player)
                    pass

                elif (x-1) == 1:

                    #Criptograma HARD
                    # def criptograma(name_game, right_game,player)

                    pass
                elif (x-1) == 2:

                    #MEmoria con EMOJIS should be easy
                    pass
                elif (x-1) == 4:
                    #RAndom number generator
                    random_number(name_game, right_game,player)
                    pass
            else:
                print(f'Lo siento no puedes pasar, necesitas -->', right_game.get('requirement'))
                buen_continue()                    
        
        elif movimiento == ' ':

            x = x + 1
            if x > 5:
                x = x - 1
                print('No puedes avanzar mas, termina el juego tu puedes!')
                buen_continue() 

        elif movimiento == 's':

            x = x - 1
            if x < 0:
                x = x + 1
                print('Para donde vas? No vas a ayudarnos ')
                buen_continue()
                

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

