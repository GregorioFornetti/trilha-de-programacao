class Lutador:
    def __init__(self, nome, peso):
        self.__nome = nome
        self.__peso = peso
        self.__vitorias = 0
        self.__derrotas = 0
        self.__empates = 0
        self.__setCategoria()
    
    def apresentar(self):
        print(f'Nome: {self.__nome}')
        print(f'Peso: {self.__peso}')
        print(f'Categoria: {self.__categoria}')
        print(f'Vitorias: {self.__vitorias}')
        print(f'Derrotas: {self.__derrotas}')
        print(f'Empates: {self.__empates}')
    
    def ganharLuta(self):
        self.__vitorias += 1
    
    def perderLuta(self):
        self.__derrotas += 1
    
    def empatarLuta(self):
        self.__empates += 1
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @property
    def peso(self):
        return self.__peso
    
    @peso.setter
    def peso(self, peso):
        self.__peso = peso
        self.__setCategoria()
    
    
    @property
    def categoria(self):
        return self.__categoria
    
    @property
    def vitorias(self):
        return self.__vitorias
    
    @property
    def derrotas(self):
        return self.__derrotas
    
    @property
    def empates(self):
        return self.__empates
    
    def __setCategoria(self):
        if self.__peso < 52.2:
            self.__categoria = 'inválida'
        elif self.__peso <= 70.3:
            self.__categoria = 'leve'
        elif self.__peso <= 83.9:
            self.__categoria = 'médio'
        elif self.__peso <= 120.2:
            self.__categoria = 'pesado'
        else:
            self.__categoria = 'inválida'
