from api import *
import random
from frases import *


api = api_call()
room_2 = api[2]
objetos = room_2.get('objects')
obj_mid = objetos[0]
obj_left = objetos[1]
obj_right = objetos[2]

obj_left_game = obj_left.get('game')
print(obj_left_game.get('name'))
lista_preguntas = obj_left_game.get('questions')
pregunta = random.randint(0,2)
juego = lista_preguntas[pregunta]
print(juego.get('question'))
print(f'''Elige una opcion:
1.{juego.get('answer_2')}     2.{juego.get('correct_answer')}

3.{juego.get('answer_3')}     4.{juego.get('answer_4')}
''')

opcion = input('Elige una opcion:\n>>')
continuar = 1
while continuar == 1:
    while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        opcion = input("Ingreso invalido, ingrese una opcion:\n>>")

    if opcion == juego.get('correct_answer'):
        print(win)

    else:
        print(lose)
        continuar = try_again()
