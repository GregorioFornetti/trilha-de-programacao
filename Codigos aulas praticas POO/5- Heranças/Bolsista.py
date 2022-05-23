from Aluno import Aluno

class Bolsista(Aluno):
    def __init__(self, nome, idade, sexo, matricula, curso, bolsa):
        super().__init__(nome, idade, sexo, matricula, curso)
        self.__bolsa = bolsa
    
    def renovarBolsa(self):
        print('Bolsa renovada')
    
    def pagarMensalidade(self):
        print('Pagar mensalidade')
    
    @property
    def bolsa(self):
        return self.__bolsa