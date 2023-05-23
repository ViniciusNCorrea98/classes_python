class Carro:
    def __init__(self, marca, cor, ano):
        self.marca = marca
        self.cor = cor
        self.ano = ano

    def Partida(self):
        print('Dando partida no carro')
    def Desligar(self):
        print('Desligando o carro')
    def ExibirInfoCarro(self):
        print(self.marca, self.cor, self.ano)

carro1 = Carro('Fiat', 'Branco', 2021)
carro1.Partida()
carro1.Desligar()
carro1.ExibirInfoCarro()

carro2 = Carro('BMW', 'Preto', 2020)
carro2.Partida()
carro2.Desligar()
carro2.ExibirInfoCarro()


carro1 = Carro('Mercedes', 'Verde', 2013)
carro1.Partida()
carro1.Desligar()
carro1.ExibirInfoCarro()