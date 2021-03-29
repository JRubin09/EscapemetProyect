from api import *
import random
from frases import *


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


api = api_call()
room_1 = api[0]
objetos = room_1.get('objects')
pizarra = objetos[0]
pc1 = objetos[1]
pc2 = objetos[2]

pc1_juego = pc1.get('game')
print(pc1_juego.get('name'))
lista_preguntas = pc1_juego.get('questions')
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
            else:
                print(lose)
        if codigo == 'frase[::-1]' or codigo == '[::-1]':

            print(win)
            continuar = 0

        elif codigo == 'salir':
            continuar = 0

        else:

            print(lose)
            print('Perdiste media vida')
            continuar = 1

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