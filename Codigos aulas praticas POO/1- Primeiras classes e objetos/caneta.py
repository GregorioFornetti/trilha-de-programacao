class Caneta:
    modelo = ''
    cor = ''
    ponta = 0
    carga = 0
    tampada = False

    def status(self):
        print(f'Modelo: {self.modelo}')
        print(f'Cor: {self.cor}')
        print(f'Ponta: {self.ponta}')
        print(f'Carga: {self.carga}')
        print(f'Tampada ? {self.tampada}')

    def rabiscar(self):
        if self.tampada:
            print('Não posso rabiscar ! Estou tampada')
        else:
            print('Rabisquei')
    
    def tampar(self):
        self.tampada = True
    
    def destampar(self):
        self.tampada = False




caneta1 = Caneta()
caneta1.modelo = 'Bic'
caneta1.cor = 'Azul'
caneta1.ponta = 0.5
caneta1.carga = 90
caneta1.status()
caneta1.tampar()
caneta1.rabiscar()

caneta2 = Caneta()
caneta2.status()
caneta2.destampar()
caneta2.rabiscar()