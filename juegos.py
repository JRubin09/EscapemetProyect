
class Juegos:
    '''
    En la api nos trae varios juegos con mensaje luego se los agregare a esos
    name: str
    requirement: booleano que tengo que validar si es True verificar su inventario 
    award: str (objeto que debo agregar mediante un metodo al inventario o vidas)
    rules: float (dependiendo de lo que diga las reglas le quitare estas vidas)
    '''

    def __init__(self,name,requirement,award,rules):
        
        self.name = name
    
    def mostrar(self):

        return((f'{self.name}').title())