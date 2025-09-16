
class Carta:

    def __init__(self, nome:str, tipo:str, ataque:int, defesa:int, custo:int):
    
        self._nome = nome
        self._tipo = tipo
        self._ataque = ataque
        self._defesa = defesa
        self._custo = custo
        
    @property    
    def nome(self)-> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome:str)-> None:
        self._nome = nome
        
        