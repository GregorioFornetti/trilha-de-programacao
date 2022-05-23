from Animal import Animal

class Reptil(Animal):
    def __init__(self, peso, idade, membros, corEscama):
        super().__init__(peso, idade, membros)
        self.__corEscama = corEscama
    
    @property
    def corEscama(self):
        return self.__corEscama
    
    def locomover(self):
        print('Rasteja')
    
    def alimentar(self):
        print('Come insetos')
    
    def emitirSom(self):
        print('Barulho de reptil')