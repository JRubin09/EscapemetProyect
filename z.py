def game_memory():
    
    memory_table=[]
    temp_table = []
    dataset = [
        ['😀', '🙄', '🐧', '🥵'],                                                   
        ['🐧', '😨', '🤓', '😷'],                                                 
        ['😨', '🤓', '🥵', '😷'],                                                  
        ['🤑', '🤑', '🙄', '😀'], 
    ]

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


    while True:

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
        
        first_emoji = get_emoji(option)
        set_emoji(temp_table,option,first_emoji)
        print_table(temp_table)
        print('')

        # Se le pide al usuario voltear el el segundo emoji
        print('')
        while True:
            try: 
                option = int(input('Ingrese la casilla a voltear: '))
                break
            except:
                print("Ingreso Invalido.")
        second_emoji = get_emoji(option)
        set_emoji(temp_table,option,second_emoji)
        print_table(temp_table)
        print('')

        # Si los dos emojis coinciden te actualiza la tabla
        if(first_emoji == second_emoji):
            print('Los emojis iguales')
            memory_table = [list(row) for row in temp_table]
        else:
            print('Los emojis no son iguales')
            # partida.quito_vida(1/4)
            print('Perdiste un cuarto de vida :/')

        # Verifica cuando se han encontrados todas las parejas de emoji y termina el juego
        if(memory_table == dataset):
            print('Juego completado')
            break

game_memory()