from api import *
import random
from frases import *

# def sopa_letras:

# soupppppppppp




def ahorcado(name_game, center_game):

     

    print(name_game.get('name'))
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))

    palabra = list(juego.get('answer'))
    print(palabra)

    # letra = input('Diga una letra: ')
    # while not ("".join(letra.split(" "))).isalpha():
    #         letra = input("Ingreso invalido, ingrese una letra : ")

    # for x in range(len(palabra))
    #     if letra == palabra[x]:


# def solve_logic(name_game,center_game):


def logic_bool(name_game,center_game):


    print(name_game.get('name'))
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))

    respuesta = input('\nIndique la respuesta:\n>>')

    continuar = 1
    while continuar == 1:
        if respuesta.title() == juego.get('answer'):
            print('win')
            continuar = 0
        else:
            print('lose')
            continuar = try_again()

