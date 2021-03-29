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

