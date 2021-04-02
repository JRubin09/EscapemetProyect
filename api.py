import requests

def api_call():

    url = "https://api-escapamet.vercel.app/"

    response = requests.request("GET", url)

    return response.json()
    

def try_again():
    continuar = 1
    while continuar == 1:
        opcion = input('Deseas volver a intentarlo. Escribe (si) o (no):\n>>').lower()
        while not ("".join(opcion.split(" "))).isalpha():
            opcion = input("Ingreso invalido, ingrese si o no: \n>>")

        if opcion == 'si':
            return 1
        
        elif opcion == 'no':
            return 0
        
        else:
            print('Ingrese una opcion valida')
            continuar = 1

def to_be_continue():
    print('Se agregara a tu inventario!')
    sigue_partida = input('''
                Para continuar la partida: 
                        presione (C)

                            >> ''').lower()
    while sigue_partida != 'c':
        sigue_partida = input('''
                    Coloque la letra (C): >> ''').lower()
    
    if sigue_partida == 'c':
        pass

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

    
