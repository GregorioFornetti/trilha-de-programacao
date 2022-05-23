from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, sexo, especialidade, salario):
        super().__init__(nome, idade, sexo)
        self.__especialidade = especialidade
        self.__salario = salario
    
    def receberAumento(self):
        self.__salario += 50
    
    @property
    def especialidade(self):
        return self.__especialidade
    
    @property
    def salario(self):
        return self.__salario