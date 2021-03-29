from api import *
import random
from frases import *



api = api_call()
room_1 = api[0]
objetos = room_1.get('objects')
pizarra = objetos[0]
pc1 = objetos[1]
pc2 = objetos[2]


pc2_juego = pc2.get('game')
print(pc2_juego.get('name'))
lista_preguntas = pc2_juego.get('questions')
pregunta = random.randint(0,2)
juego = lista_preguntas[pregunta]
print(juego.get('question'))

correcto = juego.get('answers')
print(correcto)


continuar = 1
while continuar == 1:
        respuesta = input('\n >>')
        while not ("".join(respuesta.split(" "))).isalpha():
                respuesta = input("Ingreso invalido, ingrese solo letras:\n >>")
        
        
        for x in range(len(correcto)):
        
                if respuesta == correcto[x]:
                        
                        continuar = 0
                        print('win') 
                        break

                        
        
        print('lose')
        continuar = try_again()        
                

        


# attempts = 0

# while attempts < 5:
#     print("Guess a number between 1 and 20:")

#     guess = int(input())

#     attempts = attempts + 1

#     if guess == magic_number:
#         break

# print("You have guessed the magic number!")
                            
# #                 # meto el 'award' en el inventario con un metodo?
                

# #         # elif respuesta == juego.get('answer'): 

# #                 # print(lose)
# #                 # continuar = try_again()

# #         # else: 
# #         #         break
