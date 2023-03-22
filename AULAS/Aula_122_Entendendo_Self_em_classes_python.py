'''Entendendo self em classes Python '''

# Hard coded - E algo que foi escrito diretamente no codigo
# Classe - Molde (geralmente sem dados)
# Instancia da class (objeto) - tem os dados 
# Uma classe pode gerar varias instancias 
# Na classe o self e a propria instancia.

class carro:
    def __init__(self, nome):             # O self referece a classe de instancia 
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')


fusca = carro('Fusca')
fusca.acelerar()
carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = carro(nome='Celta')
celta.acelerar()
carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()


# O self e uma convecao quando quero utilizar a propria instancia 