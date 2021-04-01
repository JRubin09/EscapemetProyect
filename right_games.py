from api import to_be_continue,try_again
import random
from frases import win, lose



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
    while continuar == 1:
        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
            respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")
        
        
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

        elif respuesta != correcto:
            print('Equivocado, sigue intentando\n')
            attempts = attempts + 1
            continuar = 1

        if attempts >= 3:
            print(lose)
            partida.quito_vida(1/4)
            print('         Perdiste -____-')
            #quitarle cuantas vidas sean 
            continuar = try_again()
            

