from Controlador import Controlador

class Controle(Controlador):

    def __init__(self):
        self.__desligada = True
        self.__volume = 50
    
    def status(self):
        print(f'Volume: {self.__volume}')
        print(f'Desligada: {self.__desligada}')
    
    def ligar(self):
        self.__desligada = False
    
    def desligar(self):
        self.__desligada = True
    
    def maisVolume(self):
        self.__volume += 5
    
    def menosVolume(self):
        self.__volume -= 5
    
    @property
    def volume(self):
        return self.__volume
    
    @property
    def desligada(self):
        return self.__desligada


controle = Controle()
controle.status()
controle.ligar()
controle.maisVolume()
controle.status()
print(controle.volume)
print(controle.desligada)