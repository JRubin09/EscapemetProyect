from api import *
import random
from frases import *


api = api_call()
room_2 = api[4]
objetos = room_2.get('objects')
obj_right = objetos[2]

obj_right_game = obj_right.get('game')
# print(obj_right_game.get('name'))
lista_preguntas = obj_right_game.get('questions')
juego = lista_preguntas[0]
print(juego.get('question'))

correcto = random.randint(1,15)
continuar = 1
while continuar == 1:
    while True:
        try: 
            respuesta = int(input("Ingrese un numero: "))
            break
        except:
            print("Ingreso Invalido.")

    if respuesta == correcto:
        print('win')
        continuar = 0
    else:    
        print('Equivocado, siga intentando\n')
        continuar = 1

        