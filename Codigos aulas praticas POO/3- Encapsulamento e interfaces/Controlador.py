import abc

class Controlador(abc.ABC):

    @abc.abstractclassmethod
    def ligar(self):
        pass

    @abc.abstractclassmethod
    def desligar(self):
        pass


    @abc.abstractclassmethod
    def maisVolume(self):
        pass

    @abc.abstractclassmethod
    def menosVolume(self):
        pass
