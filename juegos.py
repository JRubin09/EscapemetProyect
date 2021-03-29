
class Juegos:
    '''
    En la api nos trae varios juegos con mensaje luego se los agregare a esos
    name: str
    requirement: booleano que tengo que validar si es True verificar su inventario 
    award: str (objeto que debo agregar mediante un metodo al inventario o vidas)
    rules: float (dependiendo de lo que diga las reglas le quitare estas vidas)
    '''

    def __init__(self,name_game):
        
        self.name_game = name_game
    
    def mostrar(self):

        return((f'{self.name_game}').title())