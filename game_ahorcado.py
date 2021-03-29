from api import *
import random
from frases import *


api = api_call()
room_2 = api[1]
objetos = room_2.get('objects')
obj_mid = objetos[0]
obj_left = objetos[1]
obj_right = objetos[2]

obj_mid_game = obj_mid.get('game')
print(obj_mid_game.get('name'))
lista_preguntas = obj_mid_game.get('questions')
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