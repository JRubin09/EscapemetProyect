from api import *
import random
from frases import *
# import sympy
import math
from jugador import Jugador

def python_game(name_game,left_game,player, partida):
    

    # "question": "Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\".
    # Escribe una línea de código como extraer de este string 
    #  50 en formato entero"
    # "answer": "Validar en python que de el siguiente resultado:
    #  50.00 en formato entero",

    # La respuesta es la validacion hacerla

    # print('Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\".')

    # frase = 'tengo en mi cuenta 50,00 $'

    # new_frase = frase.replace('tengo en mi cuenta $','')

    # print(new_frase)

    # "question": "Invierte este string con python en un línea  para 
    # poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\"",
    # "answer": "string invertido",
    # "clue_1": "utiliza slices"

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))

    if pregunta == 1:
        continuar = 1
        while continuar == 1: 
            codigo = input('\nCodigo: \n>>')
            frase = 'oidutse ne al ortem aireinegni ed sametsis'
            a = frase.split(' ')
            if codigo == 'frase[::-1]':
                for i in range(len(a)):
                    a[i] = a[i][::-1]
                print(" ".join(a))
                logrado = input('Cual era la frase: \n>>')
                if logrado == 'estudio en la metro ingenieria de sistemas':
                    player.agrego_objeto(left_game.get('award'))
                    print(win)
                # else:
                #     print(lose)
            # if codigo == 'frase[::-1]' or codigo == '[::-1]':

            #     print(win)
            #     continuar = 0

            # elif codigo == 'salir':
            #     continuar = 0

            else:

                print(lose)
                partida.quito_vida(1/2)
                continuar = try_again()
    else:
    #     "question": "Tengo el siguiente string: frase  = \"tengo en mi cuenta 50,00 $\".
    # Escribe una línea de código como extraer de este string 
    #  50 en formato entero"
    # "answer": "Validar en python que de el siguiente resultado:
    #  50.00 en formato entero",

    # La respuesta es la validacion hacerla   

        frase = 'tengo en mi cuenta 50,00 $'

        respuesta = [int(frase)for frase in frase.replace(',','.').split(' ') if frase.isdigit()]

            
        print(respuesta)


def preguntas_mate(name_game, left_game,player, partida):

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    # si gana  ensenarselo en pantalla etc. partida.agrego_vida(1)
    # continuar = 1
    # while continuar == 1:

    #     if pregunta == 0:
    #         correcto = Derivate((sen(pi))/2)
    #         while True:
    #             try:
    #                 respuesta = int(input('Indique su respuesta:\n >>'))
    #                 break
    #             except:
    #                 print('Ingreso invalido')
            
    #         if respuesta == correcto:
    #             print(win)
    #             print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
    #             continuar = 0
    #             to_be_continue()
    #             break
    #         else:
    #             print(lose)
    #             continuar = try_again()
        
    #     elif pregunta == 1:
    #         correcto = Derivate((cos(pi/2))/2 - (tan(pi/2)/5))
    #         while True:
    #             try:
    #                 respuesta = int(input('Indique su respuesta:\n >>'))
    #                 break
    #             except:
    #                 print('Ingreso invalido')
            
    #         if respuesta == correcto:
    #             print(win)
    #             print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
    #             continuar = 0
                #   player.agrego_objeto(left_game.get('award'))
    #             to_be_continue()
    #             break
    #         else:
    #             print(lose)
    #             continuar = try_again()
        
    #     elif pregunta == 2:
    #         correcto = Derivate((sen(pi/3))/5 - tan(pi/3))
    #         while True:
    #             try:
    #                 respuesta = int(input('Indique su respuesta:\n >>'))
    #                 break
    #             except:
    #                 print('Ingreso invalido')
            
    #         if respuesta == correcto:
    #             print(win)
    #             print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
    #             continuar = 0
    #             to_be_continue()
    #             break
    #         else:
    #             print(lose)
                # partida.quito_vida()
    #             continuar = try_again()
                     

def millonario(name_game,left_game,player, partida):

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    print(f'''
        A --> {juego.get('answer_2')}      B --> {juego.get('correct_answer')}

        C --> {juego.get('answer_3')}      D --> {juego.get('answer_4')}
    ''')

    opcion = input('Elige una opcion:\n>>').lower()
    continuar = 1
    correcto = 'b'
    while continuar == 1:
        # while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        #     opcion = input("Ingreso invalido, ingrese una opcion:\n>>")

        if opcion.lower() == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
            player.agrego_objeto(left_game.get('award'))
            # print(player.mostrar())
            to_be_continue()
            break

        elif opcion.lower() == 'pista':
            
            if partida.quito_pistas(1) == True:

                print(juego.get('clue_1'))
            
            elif partida.quito_pistas(1) == False:

                buen_continue()

        else:

            print(lose)
            partida.quito_vida(1/2)
            continuar = try_again()
    

def p_mezcladas(name_game,left_game,player, partida):
    
    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    palabras = juego.get('words')
    # print(palabras)
    buena = random.randint(0,4)
    one_word = palabras[buena]
    # print(one_word)
    correcta = list(one_word)
    random.shuffle(correcta)
    list_str = ' '.join([str(elem) for elem in correcta])
    
    continuar = 1
    while continuar == 1:
        print('Categoria:',juego.get('category'))
        print(list_str.join(" "))
        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")

        for x in range(len(palabras)):
            
            if respuesta == palabras[x]:

                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                player.agrego_objeto(left_game.get('award'))
                continuar = 0
                to_be_continue()
                break

            elif x == (len(palabras)-1):

                print(lose)
                partida.quito_vida(1/2)
                continuar = try_again() 

            elif x == 'pista':

                print('Aqui no hay pistas')
                pass
