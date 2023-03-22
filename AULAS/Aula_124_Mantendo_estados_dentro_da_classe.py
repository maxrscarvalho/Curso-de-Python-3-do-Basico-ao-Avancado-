# Mantendo estados dentro da classe.

class camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} esta filmando...')
            return
        
        print(f'{self.nome} esta filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} nao pode fotografar filmando.')

        print(f'{self.nome} esta fotografando...')
        self.filmando = True 

    def parar_filmar(self):
        if self.filmando:
            print(f'{self.nome} nao esta filmando...')
            return
        
        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False

c1 = camera('Cannon')
c2 = camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.fotografar()

# print(c1.filmando)
# print(c2.filmando)    