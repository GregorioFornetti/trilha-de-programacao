from Animal import Animal

class Mamifero(Animal):
    def __init__(self, peso, idade, membros, corPelo):
        super().__init__(peso, idade, membros)
        self.__corPelo = corPelo
    
    @property
    def corPelo(self):
        return self.__corPelo
    
    def locomover(self):
        print('Caminhando')
    
    def alimentar(self):
        print('Comer comida de mamífero')
    
    def emitirSom(self):
        print('Fazer barulho de mamifero')
