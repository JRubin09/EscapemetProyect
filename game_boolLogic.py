from api import *
import random
from frases import *


api = api_call()
room_2 = api[3]
objetos = room_2.get('objects')
obj_mid = objetos[0]

obj_mid_game = obj_mid.get('game')
print(obj_mid_game.get('name'))
lista_preguntas = obj_mid_game.get('questions')
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