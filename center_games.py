from api import *
import random
from frases import *

def sopa_letras(name_game, center_game, player, partida):

    print(center_game.get('name'))
    print(center_game.get('rules'))
    # partida.agrego_vida(1)
    # partida.quito_vida(1/2)

# soupppppppppp

def ahorcado(name_game, center_game,player,partida):
    
    # # print(name_game.get('name'))
    # lista_preguntas = center_game.get('questions')
    # pregunta = random.randint(0,2)
    # juego = lista_preguntas[pregunta]
    # print(juego.get('question'))

    # palabra = list(juego.get('answer'))
    # print(palabra)

    # letra = input('Diga una letra: ')
    # while not ("".join(letra.split(" "))).isalpha():
    #         letra = input("Ingreso invalido, ingrese una letra : ")
    # partida.agrego_vida(1)

    # for x in range(len(palabra))
    #     if letra == palabra[x]:
    # partida.quito_vida(1/4)

    pass
    pass


def solve_logic(name_game,center_game,player, partida):
    
    print(center_game.get('name'))
    print(center_game.get('rules'))
    # partida.quito_vida(1)
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego)
    
    continuar = 1
    while continuar == 1:    

        if pregunta == 1:

            correcto = 26

            while True:

                try: 
                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:
                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                player.agrego_objeto(center_game.get('award'))
                to_be_continue()
                break

            else:

                print(lose)
                partida.quito_vida(1)
                continuar = try_again()
        
        else:

            correcto = 67
            
            while True:
                try: 
                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:
                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                player.agrego_objeto(center_game.get('award'))
                to_be_continue()
                break

            else:

                print(lose)
                partida.quito_vida(1)
                continuar = try_again()

        #print(juego.get('questions'))

        
def logic_bool(name_game,center_game, player, partida):

    print(center_game.get('name'))
    print(center_game.get('rules'))
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))

    respuesta = input('Indique la respuesta:\n>>')

    continuar = 1
    while continuar == 1:

        if respuesta.title() == juego.get('answer'):

            print(win)
            print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
            player.agrego_objeto(center_game.get('award'))
            to_be_continue()
            continuar = 0
            
        else:

            print(lose)
            partida.quito_vida(1/2)
            continuar = try_again()

