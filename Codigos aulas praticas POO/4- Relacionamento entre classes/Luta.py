import random

class Luta:
    def __init__(self):
        self.__desafiante = None
        self.__desafiado = None
        self.__aprovado = False
    
    def marcarLuta(self, desafiante, desafiado):
        if desafiante != desafiado and desafiante.categoria == desafiado.categoria:
            self.__desafiante = desafiante
            self.__desafiado = desafiado
            self.__aprovado = True
        else:
            self.__desafiante = None
            self.__desafiado = None
            self.__aprovado = False
    
    def lutar(self):
        if self.__aprovado:
            print('Desafiante:')
            self.__desafiante.apresentar()
            print('Desafiado:')
            self.__desafiado.apresentar()

            numero_aleatorio = random.randint(0, 2)
            if numero_aleatorio == 0:
                self.__desafiante.ganharLuta()
                self.__desafiado.perderLuta()
                print('Desafiante ganhou do desafiado')
            elif numero_aleatorio == 1:
                self.__desafiante.perderLuta()
                self.__desafiado.ganharLuta()
                print('Desafiado ganhou do desafiante')
            else:
                self.__desafiante.empatarLuta()
                self.__desafiado.empatarLuta()
                print('Ocorreu um empate')