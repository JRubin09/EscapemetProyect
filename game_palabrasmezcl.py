from api import *
import random
from frases import *


api = api_call()
room_2 = api[4]
objetos = room_2.get('objects')
obj_left = objetos[1]

obj_left_game = obj_left.get('game')
print(obj_left_game.get('name'))
lista_preguntas = obj_left_game.get('questions')
pregunta = random.randint(0,2)
juego = lista_preguntas[pregunta]
print(juego.get('question'))
print('Categoria:',juego.get('category'))

respuesta = input('\nIndique la respuesta:\n>>')
palabras = juego.get('words')

for x in range(len(palabras)):
    
    if respuesta == palabras[x]:
        print('win')

    else:
        print('lose')