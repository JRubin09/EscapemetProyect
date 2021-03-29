class Partida:
    '''
    vidas: float numero que con un metodo le quitare o agregare vidas
    pistas: int que le quitare a medida que usa las pistas
    tiempo: str
    '''
    def __init__(self, vidas, pistas, tiempo):
        self.vidas = vidas
        self.pistas = pistas
        self.tiempo = tiempo

    
    def mostrar(self):
        
        return(f"Vidas: {self.vidas}\nPistas: {self.pistas}\nTiempo: {self.tiempo}\n")

    def mostrar_tiempo (self):
        return(f'{self.tiempo}')

    