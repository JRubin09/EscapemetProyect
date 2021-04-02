from api import *
import random
from frases import *
import sympy as sy
import math
from jugador import Jugador
from main import menu_juego



def adivinanzas(name_game, right_game,player, partida):
    
    print(right_game.get('name'))
    print(right_game.get('rules'))
    lista_preguntas = right_game.get('questions')
    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    correcto = juego.get('answers')
    # print(correcto)

    continuar = 1
    pistas = 1
    while continuar == 1:

        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")
        
        if respuesta == 'pista':
                
            if partida.quito_pistas(1) == True and pistas < 3:
    
                if pistas == 1:
    
                    print(juego.get('clue_1'))
                    buen_continue()

                if pistas == 2:
    
                    print(juego.get('clue_2'))
                    buen_continue()

                if pistas == 3:

                    print(juego.get('clue_3'))
                    buen_continue()

                pistas = pistas + 1
            
            elif partida.quito_pistas(1) == False or pistas > 3:
    
                print('No + pistas en este juego')
                buen_continue()
                
            
        else:

            for x in range(len(correcto)):
            
                if respuesta == correcto[x]:
                        
                    print(win)
                    print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
                    continuar = 0
                    player.agrego_objeto(right_game.get('award'))
                    to_be_continue()
                    break

                elif x == (len(correcto)-1):
                    
                    print(lose)
                    partida.quito_vida(1/2)
                    if partida.game_over() == True:
        
                        print (gg)
                        menu_juego()

                    continuar = try_again()                

# def criptograma(name_game, right_game,player, partida):
#     print(right_game.get('name'))
#     lista_preguntas = right_game.get('questions')
#     player.agrego_objeto(right_game.get('award'))

def memoria(name_game, right_game, player, partida):
    
    print(right_game.get('name'))
    print(right_game.get('rules'))
    # lista_preguntas = right_game.get('questions')
    # juego = lista_preguntas[0]

    memory_table=[]
    temp_table = []
    dataset = [
        ['😀', '🙄', '🐧', '🥵'],                                                   
        ['🐧', '😨', '🤓', '😷'],                                                 
        ['😨', '🤓', '🥵', '😷'],                                                  
        ['🤑', '🤑', '🙄', '😀'], 
    ]

    # print('Juego de memoria bla bla bla instrucciones')

    #Contruccion de la tabla de referencia
    cont = 0
    for row in dataset:
        aux_row = []
        for column in row:
            cont = cont + 1
            aux_row.append(cont)
        memory_table.append(aux_row)

    # Funcion encargada de buscar el emoji correspondiente en el dataset
    def get_emoji(num):
        cont = 0
        for row in dataset:
            for column in row:
                cont = cont + 1
                if(cont == option):
                    return column

    # Funcion encargada de imprimir la tabla de juego
    def print_table(table):
        for row in table:

            print('')
            print('|', end='')

            for column in row:

                print(' ', column, end='')

                if(isinstance(column, int) and column < 10):
                    print(' ', end='')
                    
                print(' |', end='')

            print('')

    # Funcion encargada de asignar un emoji a la tabla de juego
    def set_emoji(table,option,emoji):
        cont = 0
        for x in range(len(table)):
            for y in range(len(table[x])):
                cont = cont + 1
                if(cont == option):
                    table[x][y] = emoji
    continuar = 1
    while continuar == 1:

        # Se copia la tabla en cada iteracion para mostrar los nuevo emojis volteados
        temp_table = [list(row) for row in memory_table]

        print_table(memory_table)

        # Se le pide al usuario voltear el primer emoji
        print('')
        while True:
            try: 
                option = int(input('Ingrese la casilla a voltear: '))
                break
            except:
                print("Ingreso Invalido.")
                
        if option == 123456789:
            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            continuar = 0
            player.agrego_objeto(right_game.get('award'))
            to_be_continue()
            break

        firts_emoji = get_emoji(option)
        set_emoji(temp_table,option,firts_emoji)
        print_table(temp_table)
        print('')

        # Se le pide al usuario voltear el el segundo emoji
        print('')

        option = int(input('Ingrese la casilla segunda casilla a voltear: '))
        second_emoji = get_emoji(option)
        set_emoji(temp_table,option,second_emoji)
        print_table(temp_table)

        print('')


        # Si los dos emojis coinciden te actualiza la tabla
        if(firts_emoji == second_emoji):
            print('Los emojis iguales')
            memory_table = [list(row) for row in temp_table]
        else:
            partida.quito_vida(1/4)
            print('Los emojis no son iguales')

        # Verifica cuando se han encontrados todas las parejas de emoji y termina el juego
        if(memory_table == dataset):
            
            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            continuar = 0
            player.agrego_objeto(right_game.get('award'))
            to_be_continue()
            break
                                              

def random_number(name_game, right_game,player, partida):

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

                respuesta = int(input("Ingrese un  posicion: "))
                break

            except:

                print("Ingreso Invalido.")

        if respuesta == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',right_game.get('award'))
            player.agrego_objeto(right_game.get('award'))
            to_be_continue()
            continuar = 0
            break

        elif respuesta != correcto:

            print('Equivocado, sigue intentando\n')
            attempts = attempts + 1
            continuar = 1

        if attempts >= 3:

            print(lose)
            partida.quito_vida(1/4)
            print('         Perdiste -____-')

            if partida.game_over() == True:
    
                print (gg)
                menu_juego()

            #quitarle cuantas vidas sean 
            continuar = try_again()
            

def python_game(name_game, left_game,player, partida):
    
    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,1)

    juego = lista_preguntas[pregunta]

    frase = 'tengo en mi cuenta 50,00 $'

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))


    if pregunta == 1:

        continuar = 1
        pistas = 1
        while continuar == 1: 

            print("Invierte este string con python en un línea  para poder leerlo frase = \"oidutse ne al ortem aireinegni ed sametsis\"")
            codigo = input('\nCodigo: \n>>')
            frase = 'oidutse ne al ortem aireinegni ed sametsis'
            a = frase.split(' ')

            if codigo == 'frase[::-1]':

                for i in range(len(a)):
            
                    a[i] = a[i][::-1]

                print(" ".join(a))

                logrado = input('Cual era la frase: \n>>')
                while not ("".join(logrado.split(" "))).isalpha():
                    logrado = input("Ingreso invalido :\n >> ")

                if logrado == 'estudio en la metro ingenieria de sistemas':

                    print(win)
                    print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                    player.agrego_objeto(left_game.get('award'))
                    # print(player.mostrar())
                    continuar = 0
                    to_be_continue()
                    break

                else:

                    print(lose)
                    partida.quito_vida(1/2)

                    if partida.game_over() == True:

                        print (gg)
                        menu_juego()

                    continuar = try_again()
                
            elif codigo.lower() == 'pista':

                if partida.quito_pistas(1) == True and pistas <= 1:

                    pistas = pistas + 1
                    print(juego.get('clue_1'))
                    buen_continue()
                
                elif partida.quito_pistas(1) == False or pistas > 1:

                    print('No + pistas en este juego')
                    buen_continue()

            else:

                print(lose)
                partida.quito_vida(1/2)
                if partida.game_over() == True:
    
                    print(gg)
                    menu_juego()
                
                continuar = try_again()

    else:
          
        frase = 'tengo en mi cuenta 50,00 $'
        respuesta = '''[int(float(x)) for x in frase.replace(",",".").split(' ') if x.replace('.','',1).isdigit()][0]'''
        correcto = input('Indique su codigo en una sola linea:\n>>')
        pistas = 1
        continuar = 1

        while continuar == 1:

            if correcto == respuesta:

                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                player.agrego_objeto(left_game.get('award'))
                # print(player.mostrar())
                to_be_continue()
                continuar = 0
                break

            elif correcto == """int(float(x)) for x in frase.replace(",",".").split(' ') if x.replace('.','',1).isdigit()""":
                
                print(win)
                print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
                player.agrego_objeto(left_game.get('award'))
                # print(player.mostrar())
                continuar = 0
                to_be_continue()
                break

            elif correcto == 'pista':
                
                if partida.quito_pistas(1) == True and pistas < 3:

                    if pistas == 1:
        
                        print(juego.get('clue_1'))
                        buen_continue()

                    if pistas == 2:
        
                        print(juego.get('clue_2'))
                        buen_continue()

                    if pistas == 3:

                        print(juego.get('clue_3'))
                        buen_continue()

                    pistas = pistas + 1

                elif partida.quito_pistas(1) == False or pistas > 3:

                    print('No + pistas')
                    buen_continue()
                
               
                
                else:
        
                    print(lose)
                    partida.quito_vida(1/2)

                    if partida.game_over() == True:

                        print (gg)
                        menu_juego()

                    continuar = try_again()


def preguntas_mate(name_game, left_game,player, partida):

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')

    pregunta = random.randint(0,2)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))
    # si gana  ensenarselo en pantalla etc. partida.agrego_vida(1)

    continuar = 1
    x = sy.symbols('x')

    while continuar == 1:

        if pregunta == 0:
            
            # correcto = sympy.Derivative(((math.sin(math.pi))/2))
            
            f_1 = (sy.sin(x))/2
            c_1 = sy.Derivative(f_1)
            a_1 = c_1.doit()
            d_1 = a_1.evalf(subs={x: math.pi})

            correcto = round(d_1,2)
            print(correcto)

            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:
                
                    print('Ingreso invalido')
            
            if correcto == respuesta:

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                partida.agrego_objeto(left_game.get('award'))
                partida.agrego_vida(1)
                continuar = 0
                to_be_continue()
                break

            else:

                print(lose)
                partida.quito_vida(1/4)

                if partida.game_over() == True:
                    
                    print (gg)
                    menu_juego()

                continuar = try_again()
        
        elif pregunta == 1:

            f_2 = (sy.cos(x/2)/2)
            c_2 = sy.Derivative(f_2)
            a_2 = c_2.doit()
            d_2 = a_2.evalf(subs={x: math.pi})

            correcto = round(d_2,2)
            print(correcto)

            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:

                    print('Ingreso invalido')
            
            if correcto == respuesta:

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                partida.agrego_objeto(left_game.get('award'))
                partida.agrego_vida(1)
                continuar = 0
                to_be_continue()
                break
            
            else:

                print(lose)
                partida.quito_vida(1/4)

                if partida.game_over() == True:
                    
                    print (gg)
                    menu_juego()

                continuar = try_again()
        
        elif pregunta == 2:

            f_3 = ((sy.sin(x))/5 -(sy.tan(x)))
            c_3 = sy.Derivative(f_3)
            a_3 = c_3.doit()
            d_3 = a_3.evalf(subs={x: math.pi})

            correcto = round(d_3,2)
            print(correcto)

            while True:

                try:

                    respuesta = float(input('Indique su respuesta:\n >>'))
                    break

                except:

                    print('Ingreso invalido')
            
            if correcto == respuesta:

                print(win)
                print(f'Felicidades obtuviste:',left_game.get('award'))
                partida.agrego_objeto(left_game.get('award'))
                partida.agrego_vida(1)
                continuar = 0
                to_be_continue()
                break

            else:

                print(lose)
                partida.quito_vida(1/4)
                if partida.game_over() == True:
                    
                    print (gg)
                    menu_juego()

                continuar = try_again()
                     

def millonario(name_game,left_game,player, partida):

    print(left_game.get('name'))
    print(left_game.get('rules'))
    lista_preguntas = left_game.get('questions')
    pregunta = random.randint(0,2)

    juego = lista_preguntas[pregunta]
    continuar = 1
    correcto = 'b'
    while continuar == 1:

        print(juego.get('question'))
        print(f'''
            A --> {juego.get('answer_2')}      B --> {juego.get('correct_answer')}

            C --> {juego.get('answer_3')}      D --> {juego.get('answer_4')}
        ''')

        opcion = input('Elige una opcion:\n>>').lower()
            # while (not opcion.isnumeric()) or (int(opcion) < 1) or (int(opcion) > 4): 
        #     opcion = input("Ingreso invalido, ingrese una opcion:\n>>")
        pistas = 0
        if opcion.lower() == correcto:

            print(win)
            print(f'Felicidades obtuviste el objeto:',left_game.get('award'))
            player.agrego_objeto(left_game.get('award'))
            # print(player.mostrar())
            continuar = 0
            to_be_continue()

            break

        elif opcion.lower() == 'pista':
            
            if partida.quito_pistas(1) == True and pistas == 0:

                pistas = pistas + 1
                print(juego.get('clue_1'))
                buen_continue()
            
            elif partida.quito_pistas(1) == False:

                buen_continue()

        else:

            print(lose)
            partida.quito_vida(1/2)

            if partida.game_over() == True:

                print (gg)
                menu_juego()

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
        print(list_str)

        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")

        for x in range(len(palabras)):
            
            if respuesta == palabras[x]:

                print(win)
                print(f'Felicidades obtuviste una contraseña: escapandoando')
                player.agrego_objeto(left_game.get('award'))
                continuar = 0
                to_be_continue()
                break

            elif x == (len(palabras)-1):

                print(lose)
                partida.quito_vida(1/2)

                if partida.game_over() == True:
    
                    print (gg)
                    menu_juego()

                continuar = try_again() 

            elif x == 'pista':

                print('Aqui no hay pistas')
                pass


def sopa_letras(name_game, center_game, player, partida):
    
    print(center_game.get('name'))
    print(center_game.get('rules'))
    # partida.agrego_vida(1)
    # partida.quito_vida(1/2)

# soupppppppppp

def ahorcado(name_game, center_game,player,partida):
    
    # # print(name_game.get('name'))
    # lista_preguntas = center_game.get('questions')
    # pregunta = random.randint(0,2)
    # juego = lista_preguntas[pregunta]
    # print(juego.get('question'))

    # palabra = list(juego.get('answer'))
    # print(palabra)

    # letra = input('Diga una letra: ')
    # while not ("".join(letra.split(" "))).isalpha():
    #         letra = input("Ingreso invalido, ingrese una letra : ")
    # partida.agrego_vida(1)

    # for x in range(len(palabra))
    #     if letra == palabra[x]:
    # partida.quito_vida(1/4)

    pass


def solve_logic(name_game,center_game,player, partida):
    
    print(center_game.get('name'))
    print(center_game.get('rules'))
    print('NOOOOO, pisaste el saman perdiste una vida cuidado!!')
    partida.quito_vida(1)
    # poner el game over aqui 
    lista_preguntas = center_game.get('questions')
    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego)
    
    continuar = 1
    while continuar == 1:    

        if pregunta == 1:

            correcto = 26

            while True:

                try: 

                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:

                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                player.agrego_objeto(center_game.get('award'))
                to_be_continue()
                continuar = 0
                break

            else:

                print(lose)
                partida.quito_vida(1)
                continuar = try_again()
        
        else:

            correcto = 67
            
            while True:

                try: 

                    respuesta = int(input('Indique la respuesta:\n>>'))
                    break

                except:

                    print("Ingreso Invalido.")

            if respuesta == correcto:

                print(win)
                print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
                player.agrego_objeto(center_game.get('award'))
                to_be_continue()
                continuar = 0
                break

            else:

                print(lose)
                partida.quito_vida(1)

                if partida.game_over() == True:
    
                    print(gg)
                    menu_juego()

                continuar = try_again()

        #print(juego.get('questions'))

        
def logic_bool(name_game,center_game, player, partida):

    print(center_game.get('name'))
    print(center_game.get('rules'))
    lista_preguntas = center_game.get('questions')

    pregunta = random.randint(0,1)
    juego = lista_preguntas[pregunta]
    print(juego.get('question'))

    respuesta = input('Indique la respuesta:\n>>')
    while not ("".join(respuesta.split(" "))).isalpha():
        respuesta = input("Ingreso invalido, ingrese una respuesta valida:\n >> ")

    continuar = 1
    while continuar == 1:

        if respuesta.title() == juego.get('answer'):

            print(win)
            print(f'Felicidades obtuviste el objeto:',center_game.get('award'))
            player.agrego_objeto(center_game.get('award'))
            to_be_continue()
            continuar = 0
            break
            
        else:

            print(lose)
            partida.quito_vida(1/2)

            if partida.game_over() == True:
    
                print (gg)
                menu_juego()

            continuar = try_again()

