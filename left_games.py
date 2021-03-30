from api import *
import random
from frases import *


def python_game(name_game,left_game):
    

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
                print('Perdiste media vida')
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


# def preguntas_mate(name_game, right_game):


def millonario(name_game,left_game):

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

        if opcion == correcto:
            print(win)
            print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
            to_be_continue()
            #meterlo en el inventario?
            break
        else:
            print(lose)
            continuar = try_again()
    

def p_mezcladas(name_game,left_game):
    

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    print('Categoria:',juego.get('category'))
    palabras = juego.get('words')
    print(palabras)
    buena = random.randint(0,4)
    correcta = palabras[buena]
    print(correcta)

    respuesta = input('\nIndique la respuesta:\n>>')
    continuar = 1
    while continuar == 1:

        for x in range(len(palabras)):
            
            if respuesta == palabras[x]:
                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                to_be_continue()
                continuar = 0

            elif x == (len(palabras)-1):
                print(lose)
                continuar = try_again()   

