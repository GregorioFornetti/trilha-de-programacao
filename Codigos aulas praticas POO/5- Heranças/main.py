from Visitante import Visitante
from Aluno import Aluno
from Professor import Professor
from Bolsista import Bolsista
from Tecnico import Tecnico

visitante = Visitante('Greg', 20, 'M')
visitante.fazerAniversario()

aluno = Aluno('Ana', 22, 'F', 123, 'BCC')
aluno.pagarMensalidade()
aluno.fazerAniversario()

professor = Professor('Gustavo', 30, 'M', 'SO', 3000)
professor.receberAumento()
print(professor.salario)

bolsista = Bolsista('Greg', 20, 'M', 123, 'BCC', 100)
bolsista.renovarBolsa()