
class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
    
    def fazerAniversario(self):
        self.__idade += 1
        print(f'O(A) {self.__nome} fez aniversário ! Parabéns !')
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def sexo(self):
        return self.__sexo