from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, sexo, matricula, curso):
        super().__init__(nome, idade, sexo)
        self.__matricula = matricula
        self.__curso = curso
    
    def pagarMensalidade(self):
        print(f'Aluno(a) {self.nome} pagou a mensalidade')
    
    @property
    def matricula(self):
        return self.__matricula

    @property
    def curso(self):
        return self.__curso
        