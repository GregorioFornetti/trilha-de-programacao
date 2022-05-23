import abc


class Animal(abc.ABC):
    def __init__(self, peso, idade, membros):
        self.__peso = peso
        self.__idade = idade
        self.__membros = membros
    
    @property
    def peso(self):
        return self.__peso
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def membros(self):
        return self.__membros

    @abc.abstractclassmethod
    def locomover(self):
        pass

    @abc.abstractclassmethod
    def alimentar(self):
        pass

    @abc.abstractclassmethod
    def emitirSom(self):
        pass

