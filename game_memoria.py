from api import *
import random
from frases import *


api = api_call()
room_2 = api[2]
objetos = room_2.get('objects')
obj_mid = objetos[0]
obj_left = objetos[1]
obj_right = objetos[2]

obj_right_game = obj_right.get('game')
print(obj_right_game.get('name'))
lista_preguntas = obj_right_game.get('questions')
pregunta = random.randint(0,2)
juego = lista_preguntas[pregunta]
print(juego.get('question'))
