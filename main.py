from cuartos import Cuartos
from juegos import Juegos
from jugador import Jugador
from dibujos_cuartos import *
from partida import Partida
from objetos import Objetos
from api import *
from frases import *
from instrucciones import *


def records():
    print(record)

def partida_nueva():

    opcion = input('''
    Eliga la dificultad de su partida: 
    1. Facil
    2. Media
    3. Dificil
    4. Menu\n >> ''')
    while (not opcion.isnumeric()) or (int(opcion) < 1): 
        opcion = input("Ingreso invalido, ingrese una opcion valida: ")        

    if opcion == '1':
        vidas = '5'
        pistas = '5'
        tiempo = '15 minutos'
        
    elif opcion == '2':
        vidas = '3'
        pistas = '3'
        tiempo = '10 minutos'
        
    elif opcion == '3':
        vidas = '1'
        pistas = '1'
        tiempo = '5 minutos'
       
    elif opcion == '4':
        print('Adios')
        main()
    else:
        return 0

    nueva_partida = Partida(vidas, pistas, tiempo)
    # registro_jugador()
    print(nueva_partida.mostrar())

def registro_jugador():
    username = input('Username: ')
    contrasena = input('Contrasena: ')
    edad = input('Edad: ')
    avatar = input('Elige el Avatar de tu jugador: ')
    #hacer un if y darle nombre a nuevos avatares que el jugador pueda elegir
    tiempo_partidas = []
    inventario = []

    nuevo_jugador = Jugador(username, contrasena, edad, avatar, tiempo_partidas, inventario)

    print(nuevo_jugador.mostrar())
    
def comienza_partida():
    print('Intenta Escapar')
    while True:
        try: 
            x = int(input('''En donde deseas comenzar:
    
    1 --> Laboratorio SL001               
    2 --> Biblioteca
    3 --> Plaza Rectorado\n>>'''))
            break
        except:
            print('Ingreso invalido')
    api = api_call()

    while True:

    #Mientras este while se cumpla sigue en el juego hacer para
    #Game over y para Win! 
    #Crear condicion para que siga en el while 
    #Objetos? Vidas? 
    #  
        dic = api[x-1]
        name = dic.get('name')
        cosas = dic.get('objects')
        room = Cuartos(name)
        print(dibujos_rooms[x-1])
        print('''
        (S) te devuelves de cuarto    <-----
        (SPACE) avanzas al siguiente cuarto ----->''')
        print(room.mostrar())
        movimiento = input('Hacia donde quieres ir:\n >> ')

        if movimiento == 'w':

            position = 'center'

        elif movimiento == 'a':

            name = cosas.get('name')
            position = 'left'    
            objeto_izq = Objetos(name,position)
            print('dibujo')
            


        elif movimiento == 'd':
            pass

        elif movimiento == ' ':
            x = x + 1

        elif movimiento == 's':
            x = x - 1
        else:
            break

def main():
    print(bienvenido)
    while True:
        opcion = input("""
        Elige una opcion: 
        1. Nueva Partida
        2. Instrucciones
        3. Records
        4. Para salir \n >> """)

        while (not opcion.isnumeric()) or (int(opcion) < 1): 
          opcion = input("Ingreso invalido, ingrese una opcion valida: ") 

        if opcion == '1':

            partida_nueva()
            registro_jugador()
            comienza_partida()

        elif opcion == '2':

            instrucciones()

        elif opcion == '3':

            records()

        elif opcion == '4':

            break

        else:

            print('Opcion invalida')




if __name__ == '__main__':
    main()

