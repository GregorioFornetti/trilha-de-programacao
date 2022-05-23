from Aluno import Aluno

class Tecnico(Aluno):
    def __init__(self, nome, idade, sexo, matricula, curso, registroProfissional):
        super().__init__(nome, idade, sexo, matricula, curso)
        self.__registroProfissional = registroProfissional
    
    def praticar(self):
        print('Tecnico praticou')
    
    @property
    def registroProfissional(self):
        return self.__registroProfissional