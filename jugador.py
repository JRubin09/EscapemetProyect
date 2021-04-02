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
        
        return(f"Username: {self.username}\nEdad: {self.edad}\nAvatar: {self.avatar}\nInventario: {self.inventario}")
    
    def agrego_objeto(self, item):

        self.inventario.append(item)
        

    def check_inventario(self,item):

        
        valor_bool = False

        for x in range(len(self.inventario)):

            if item == self.inventario[x]:

                valor_bool = True
                break

        return valor_bool    




        
   
