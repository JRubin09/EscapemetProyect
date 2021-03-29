class Objetos:
    '''
    Nombre: str 
    gracias a esta clase sabremos a que objeto accede el jugador
    position: str
    '''

    def __init__(self,name,position):
        
        self.name = name
        self.position = position

    def mostrar(self):

        print(f'Name = {self.name}')