from Lutador import Lutador
from Luta import Luta

lutador1 = Lutador('Putscript', 80)
lutador2 = Lutador('Deadcode', 82.3)

luta1 = Luta()
luta1.marcarLuta(lutador1, lutador1)
luta1.lutar()

lutador1.apresentar()
lutador2.apresentar()