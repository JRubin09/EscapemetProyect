from api import *
import random
from frases import *


def millonario(name_game,left_game):

    print(left_game.get('name'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    print(f'''Elige una opcion:
    A --> {juego.get('answer_2')}     B --> {juego.get('correct_answer')}

    C --> {juego.get('answer_3')}     D --> {juego.get('answer_4')}
    ''')

    opcion = input('Elige una opcion:\n>>')
    continuar = 1
    correcto = 'b'
    while continuar == 1:
        # while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        #     opcion = input("Ingreso invalido, ingrese una opcion:\n>>")

        if opcion == correcto:
            print(win)
            break
        else:
            print(lose)
            continuar = try_again()
