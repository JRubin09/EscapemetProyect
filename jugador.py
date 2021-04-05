from api import buen_continue
from partida import Partida

class Jugador(Partida):
    
    def __init__(self, vidas, pistas, tiempo, username, contrasena, edad, avatar, tiempo_partidas, inventario):
        super().__init__(vidas,pistas,tiempo)
        self.username = username
        self.contrasena = contrasena
        self.edad = edad
        self.avatar = avatar 
        self.tiempo_partidas = []
        self.inventario = []
        
 
    def mostrar(self):
        
        return(f"Vidas: {self.vidas}\nPistas: {self.pistas}\nTiempo: {self.tiempo}\nUsername: {self.username}\nEdad: {self.edad}\nAvatar: {self.avatar}\n")

    def mostrar_terminado(self):

        # for x in range(len(self.tiempo_partidas)):
        return(f'{self.tiempo_partidas}')

    def mostrar_avatar(self):

        return(f'{self.avatar}')
    
    def agrego_objeto(self, item):

        self.inventario.append(item)
        
    def check_inventario(self,item):

        valor_bool = False

        for x in range(len(self.inventario)):

            if item == self.inventario[x]:

                valor_bool = True
                break

        return valor_bool    
    
    def agrego_tiempo(self,time):

        self.tiempo_partidas.append(time)

    def veo_inventario(self):
        print('Inventario:')
        for x in range(len(self.inventario)):
            
            items = self.inventario[x]
            
            print(items)
            buen_continue()
    

        
   
