class Caneta:
    def __init__(self, modelo, cor, ponta, carga):
        self.__modelo = modelo
        self.__cor = cor
        self.__ponta = ponta
        self.__carga = carga
        self.__tampada = False

    def status(self):
        print(f'Modelo: {self.__modelo}')
        print(f'Cor: {self.__cor}')
        print(f'Ponta: {self.__ponta}')
        print(f'Carga: {self.__carga}')
        print(f'Tampada ? {self.__tampada}')

    def rabiscar(self):
        if self.__tampada:
            print('Não posso rabiscar ! Estou tampada')
        else:
            print('Rabisquei')
    
    def tampar(self):
        self.__tampada = True
    
    def destampar(self):
        self.__tampada = False
    
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self, modelo):
        self.__modelo = modelo
    
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor






caneta1 = Caneta('Bic', 'Azul', 0.5, 90)
print(caneta1.cor)
caneta1.status()
caneta1.tampar()
caneta1.rabiscar()

