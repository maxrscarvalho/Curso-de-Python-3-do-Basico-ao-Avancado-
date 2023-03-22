'''Metodos em instancias de classes Python'''

# Hard coded - E algo que foi escrito diretamente no codigo

class carro:
    def __init__(self, nome):             # O self referece a classe de instancia 
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} esta acelerando...')

string = 'Max'
print(string.upper())

fusca = carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = carro(nome='Celta')
print(celta.nome)
celta.acelerar()