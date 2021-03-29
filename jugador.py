from partida import Partida

class Jugador:
    def __init__(self, username, contrasena, edad, avatar, tiempo_partidas, inventario):

        self.username = username
        self.contrasena = contrasena
        self.edad = edad
        self.avatar = avatar 
        self.tiempo_partidas = [tiempo_partidas]
        self.inventario = [inventario]
        
    def mostrar(self):
        
        return(f"Username: {self.username}\nEdad: {self.edad}\nAvatar: {self.avatar}\n")
    
   
