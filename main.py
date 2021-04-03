from api import *
from closeup_dibujos import *
from cuartos import Cuartos
from dibujos_cuartos import *
from frases import *
from instrucciones import *
from jugador import Jugador
from objetos import Objetos
from partida import Partida
from games_all import *
import time

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
        vidas = float(5)
        pistas = 5
        tiempo = '15 minutos'
        
    elif opcion == '2':

        print(medio)
        vidas = float(3)
        pistas = 3
        tiempo = '10 minutos'
        
    elif opcion == '3':

        print(hard)
        vidas = float(1)
        pistas = 1
        tiempo = '5 minutos'
       
    elif opcion == '4':

        print('Adios')
        menu_juego()
    else:
        return 0

    nueva_partida = Partida(vidas, pistas, tiempo)
    # registro_jugador()
    print(nueva_partida.mostrar())
    return nueva_partida

def registro_jugador():

    while True:

        try:
            username = input('Username: ')
            contrasena = input('Contrasena: ')
            edad = int(input('Edad: '))
            break

        except:
            print('Ingresaste un dato invalido')

    avatar = input('''Elige el Avatar de tu jugador: 
    1. ''')
    #hacer un if y darle nombre a nuevos avatares que el jugador pueda elegir
    tiempo_partidas = []
    #agrego al inventario objetos que no tengo hecho los juegos de una vez para probar el juego
    inventario = '.'

    nuevo_jugador = Jugador(username, contrasena, edad, avatar, tiempo_partidas, inventario)
    # print(nuevo_jugador.mostrar())
    return nuevo_jugador
    
def comienza_partida(partida,player):

    player.agrego_objeto(["Titulo Universitario","Mensaje"])
    
    primer_discurso(partida)
    print(ready)
    buen_continue()
    
    x = 1
    api = api_call()
    
    continuar = 1

    while continuar == 1:

        dic = api[x]
        name = dic.get('name')
        cosas = dic.get('objects')
        room = Cuartos(name)
        
        print(dibujos_rooms[x])
        print(f'''
            <-------   (S)   Te devuelves de cuarto      <-------
            -------> (SPACE) Avanzas al siguiente cuarto ------->
                       (P)    Para poner PAUSA ''')
        print(room.mostrar())
        
                # ('Movimiento invalido controlate vale es 2D y en la terminal de window') 

        movimiento = input('Hacia donde te diriges?\n>> ')      

        if movimiento.lower() == 'w':

            center_obj = cosas[0]
            name = center_obj.get('name')
            position = center_obj.get('position')    
            objeto_center = Objetos(name,position)

            center_game = center_obj.get('game')
            name_game = center_game.get('name')
            # juego = Juegos(name_game)
            # print(juego.mostrar())
            print(objeto_center.mostrar())

            if x == 2:

                print('NOOOOO, pisaste el saman perdiste una vida cuidado!!')
                partida.quito_vida(1)
                if partida.game_over() == True:
    
                    print (gg)
                    menu_juego()

            print(f'Bienvenido a ',center_game.get('name'),center_game.get('message_requirement'))
            
            print('Puedes intentar entrar si quieres, pero si no tienes lo requerido no pasaras')
            comprobando = input('Deseas pasar? (Y) ==> si (N) ==> no\n >>')

            if comprobando.lower() == 'y':

                valido_premio = player.check_inventario(center_game.get('award'))
                valido_requirement = player.check_inventario(center_game.get('requirement'))
                # print(valido_requirement)

                if valido_premio == True:

                    print(dibujos_closeup[x][0])
                    print('Ya pasaste por aqui y ganaste, tienes en tu INVENTARIO -->',center_game.get('award'))
                    buen_continue()
                    pass

                elif valido_requirement == True or center_game.get('requirement') == False:
                        
                    print(dibujos_closeup[x][0])

                    if x == 0:
                        #SOUP HARD
                        #sopa_letras(name_game,center_game,player, partida)
                        pass

                    elif x == 1:

                        #AHORCADO HARD
                        ahorcado(name_game, center_game,player, partida)
                        pass

                    elif x == 2:
                        #Solve logic

                        solve_logic(name_game,center_game,player, partida)
                        pass

                    elif x == 3:
                        #LOGICA BOOLEANA ESTA HECHO REVISAR

                        logic_bool(name_game,center_game,player, partida)
                        valido_obj_ganado = player.check_inventario(center_game.get('award'))

                        if valido_obj_ganado == True:

                            print('Felicidades por desbloquear un nuevo cuarto atento con lo que obtienes aqui!')
                            buen_continue()
                            x = x + 1

                        elif valido_obj_ganado == False:

                            print('Lo siento tienes que completar el juego para pasar')
                            buen_continue()
                            pass

                    elif x == 4:
                        #SI COMPLETA ESTE JUEGO GANA OJOOOOOOOOOOOOOO! LE PONGO UN BREAK? IDK
                        #AQUI NO HAY JUEGO O LO INVENTO O ABRE ESA PUERTA Y GGWP
                        pass

                    else:

                        pass  

                else:

                    print(f'Lo siento no puedes pasar, necesitas -->', center_game.get('requirement'))
                    buen_continue()

            elif comprobando.lower() == 'n':
                
                pass            
            
            elif comprobando != 'n' and comprobando != 'y':

                print('Ingreso invalido, vuelve al cuarto donde estabas!')
                buen_continue()        
                
        elif movimiento.lower() == 'a':

            left_obj = cosas[1]
            name = left_obj.get('name')
            position = left_obj.get('position')
            objeto_izq = Objetos(name,position)

            left_game = left_obj.get('game')
            name_game = left_game.get('name')
            # print(objeto_izq.mostrar())

            print(f'Bienvenido a ',left_game.get('name'),left_game.get('message_requirement'))
            
            print('Puedes intentar entrar si quieres, pero si no tienes lo requerido no pasaras')
            comprobando = input('Deseas pasar? (Y) ==> si (N) ==> no\n >>')

            if comprobando.lower() == 'y':
    
                valido_requirement = player.check_inventario(left_game.get('requirement'))
                valido_premio = player.check_inventario(left_game.get('award'))

                if valido_premio == True:

                    print(dibujos_closeup[x][1])
                    print('Ya pasaste por aqui y ganaste, tienes en tu INVENTARIO -->',left_game.get('award'))
                    buen_continue()
                    pass

                elif valido_requirement == True or left_game.get('requirement') == False:

                    print(dibujos_closeup[x][1])
                    if x == 0:

                        python_game(name_game,left_game,player, partida)
                        pass

                    elif x == 1:

                        #preguntas matematica
                        preguntas_mate(name_game,left_game,player,partida)

                        pass
                    
                    elif x == 2:

                        #QUIZZIS
                        millonario(name_game,left_game,player, partida)
                        pass

                    elif x == 4:

                        #Palabras mezcladas
                        p_mezcladas(name_game,left_game,player, partida)
                        pass

                else:

                    print(f'Lo siento no puedes pasar, necesitas -->', left_game.get('requirement'))
                    buen_continue()

            elif comprobando.lower() == 'n':
            
                pass            
            
            elif comprobando.lower() != 'n' and comprobando.lower() != 'y':

                print('Ingreso invalido, vuelve al cuarto donde estabas!!\n')
                buen_continue()

        elif movimiento.lower() == 'd':

            right_obj = cosas[2]
            name = right_obj.get('name')
            position = right_obj.get('position')
            objeto_right = Objetos(name,position)
            right_game = right_obj.get('game')
            name_game = right_game.get('name')

            print(objeto_right.mostrar())
            print(f'Bienvenido a ',right_game.get('name'),right_game.get('message_requirement'))
            
            print('Puedes intentar entrar si quieres, pero si no tienes lo requerido no pasaras')
            comprobando = input('Deseas pasar? (Y) ==> si (N) ==> no\n >>')

            if comprobando.lower() == 'y':
                valido_requirement = player.check_inventario(right_game.get('requirement'))
                valido_premio = player.check_inventario(right_game.get('award'))

                if valido_premio == True:

                    print(dibujos_closeup[x][2])
                    print('Ya pasaste por aqui y ganaste, tienes en tu INVENTARIO-->',right_game.get('award'))
                    buen_continue()
                    pass
                    
                
                elif valido_requirement == True or right_game.get('requirement') == False:

                    print(dibujos_closeup[x][2])

                    if x == 0:

                        
                        adivinanzas(name_game,right_game,player, partida)
                        pass

                    elif x == 1:

                        
                        #Criptograma 
                        criptograma(name_game, right_game,player, partida)
                        pass

                    elif x == 2:

                        #MEmoria con EMOJIS should be easy
                        memoria(name_game, right_game,player, partida)
                        pass

                    elif x == 4:

                        #RAndom number generator
                        random_number(name_game, right_game,player, partida)
                        pass

                else:

                    print(f'Lo siento no puedes pasar, necesitas -->', right_game.get('requirement'))
                    buen_continue()  

            elif comprobando.lower() == 'n':
                
                pass            
            
            elif comprobando != 'n' and comprobando != 'y':

                print('Ingreso invalido, vuelve al cuarto donde estabas!')
                buen_continue()                    
        
        elif movimiento == ' ':

            if x == 0:

                x = 4
            
            elif x == 1:

                x = 3

            elif x == 2:
                
                x = 1
            
            elif x == 3:
                # requirement para pasar 
                # logic_bool(name_game,center_game,player, partida)
                valido_obj_ganado = player.check_inventario(center_game.get('award'))

                if valido_obj_ganado == True:

                    print('Felicidades por desbloquear un nuevo cuarto atento con lo que obtienes aqui!')
                    buen_continue()
                    x = 0

                elif valido_obj_ganado == False:

                    print('Lo siento tienes que completar el juego para pasar')
                    buen_continue()
                    x = 3

            elif x == 4:

                print('Pa onde vas tu? ')
                buen_continue()
                x = 4
    
        elif movimiento.lower() == 's':

            if x == 0:
    
                x = 3
            

            elif x == 1:

                x = 2

            elif x == 2:

                print('Pa onde vas tu? ')
                buen_continue()
                x = 2
            
            elif x == 3:

                x = 1

            elif x == 4:

                x = 0
                
        elif movimiento.lower() == 'p':

            print(partida.mostrar())
            sigue_partida = input('''
                        Desea continuar la partida: 
                        
                        (Y) --> si o (N) --> no\n
                                >>''').lower()
            
            while not ("".join(movimiento.split(" "))).isalpha():   
                movimiento = input("Ingreso invalido, ingrese el movimiento :\n >> ")
                    
            if sigue_partida == 'y':
                pass

            elif sigue_partida == 'n':
                menu_juego()
                break

        
        
        else:

            continuar = 1

def menu_juego():

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

def main():

    print(bienvenido)
    menu_juego()


if __name__ == '__main__':
    main()

