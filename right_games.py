from api import *
import random
from frases import *

# def criptograma(name_game, right_game):
#     print(right_game.get('name'))
#     lista_preguntas = right_game.get('questions')

def adivinanzas(name_game, right_game):
    
    print(right_game.get('name'))
    lista_preguntas = right_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    correcto = juego.get('answers')
    # print(correcto)

    continuar = 1
    while continuar == 1:
        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")
        
        
        for x in range(len(correcto)):
        
            if respuesta == correcto[x]:
                    
                print(win)
                print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
                to_be_continue()
                break

            elif x == (len(correcto)-1):
                print(lose)
                continuar = try_again()                



def memoria(name_game, right_game):
    print(right_game.get('name'))
    print(right_game.get('rules'))
    lista_preguntas = right_game.get('questions')
    juego = lista_preguntas[0]
    print(juego.get('question'))
    # no entiendo 

def random_number(name_game, right_game):
    print(right_game.get('name'))
    print(right_game.get('rules'))
    lista_preguntas = right_game.get('questions')
    juego = lista_preguntas[0]
    print(juego.get('question'))

    correcto = random.randint(1,15)
    continuar = 1
    attempts = 0
    while continuar == 1:
        while True:
            try: 
                respuesta = int(input("Ingrese un numero: "))
                break
            except:
                print("Ingreso Invalido.")

        if respuesta == correcto:
            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            to_be_continue()
            continuar = 0

        elif respuesta != correcto:
            print('Equivocado, siga intentando\n')
            attempts = attempts + 1
            continuar = 1

        elif attempts > 3:
            

