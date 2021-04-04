import requests
import time
import datetime
from frases import gg, gratz

def api_call():

    url = "https://api-escapamet.vercel.app/"

    response = requests.request("GET", url)

    return response.json()
    

def try_again():
    continuar = 1
    while continuar == 1:
        opcion = input('Deseas volver a intentarlo. Escribe (si) o (no):\n>>').lower()
        while not ("".join(opcion.split(" "))).isalpha():
            opcion = input("Ingreso invalido, ingrese si o no: \n>>").lower()

        if opcion == 'si':
            return 1
        
        elif opcion == 'no':
            return 0
        
        else:
            print('Ingrese una opcion valida')
            continuar = 1

def to_be_continue():

    print('Se agregara a tu inventario!')
    time.sleep(3)

def buen_continue():
    sigue_partida = input('''
                Para continuar la partida: 
                        presione (C)

                            >> ''').lower()
    while sigue_partida != 'c':
        sigue_partida = input('''
                    Coloque la letra (C):>> ''').lower()
    
    if sigue_partida == 'c':
        pass

def primer_discurso(partida):
      
  show_time = partida.mostrar_tiempo()
  primera_narra = (f'''
  Hoy 5 de marzo de 2021, la Universidad sigue en cuarentena(esto no es novedad), lo que sí es   
  novedad es que se robaron un Disco Duro de la Universidad del cuarto de redes que tiene toda 
  la información de SAP de estudiantes, pagos y  asignaturas. Necesitamos que nos ayudes a 
  recuperar el disco, para eso tienes: {show_time} antes de que el servidor se caiga 
                      y no se pueda hacer más nada.''') 
  
  print(primera_narra)


def segundo_discurso(player):

    show_avatar = player.mostrar_avatar()
    segunda_narra = (f'''
    Bienvenido {show_avatar}, gracias por tu disposición a ayudarnos a resolver 
    este inconveniente, te encuentras actualmente ubicado en la biblioteca, revisa 
    el menú de opciones para ver qué acciones puedes realizar. Recuerda que el tiempo 
                    corre más rápido que un trimestre en este reto.''')

    print(segunda_narra)

def end_game(player,partida):

    show_avatar = player.mostrar_avatar()
    show_time = player.mostrar_tiempo()
    
    ultima_narra = (f'''
    ¡Felicidades! Has logrado evitar una catástrofe en la Unimet, entonces lograste 
    todos los objetivos {show_avatar} tenias {show_time} y lo lograste en tal tiempo increible tu record
    quedara para la historia vuelve a jugar en otra dificultad para mejorarlo!''')
    
    print(ultima_narra)


def se_acabo(player,instanteInicial):

    print(gg)
    instanteFinal = datetime.datetime.now().minute
    tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
    # segundos = tiempo.seconds
    # minutos = tiempo
    print(tiempo)
    # print(segundos)
    # print(minutos)
    player.agrego_tiempo(minutos)
    print("Estos son tus records en minutos: ")
    print(player.mostrar_terminado())
    time.sleep(3)

def ganador(player, instanteInicial):

    instanteFinal = datetime.datetime.now().minute
    tiempo = instanteFinal - instanteInicial # Devuelve un objeto timedelta
    # segundos = tiempo.seconds
    minutos = tiempo
    print(tiempo)
    # print(segundos)
    # print(minutos)
    player.agrego_tiempo(minutos)
    print(gratz)
    print("Estos son tus records en minutos: ")
    print(player.mostrar_terminado())
    time.sleep(10)

