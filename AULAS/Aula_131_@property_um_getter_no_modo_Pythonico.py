'''
@property - um getter no modo Pythonico
getter - um metodo para obter um atributo

cor -> get_cor()

modo pythonico - modo do python de fazer coisas
@property e uma propriedade do objeto, ela 
e um metodo que se comporta como um 
atributo. 

Geralmente e usada nas seguintes situacoes:

-> como getter
-> p/ evitar quebra de codigo cliente
-> p/ evitar habilitar setter
-> p/ executar acoes ao obter um atributo.'''

'''Exemplo 1'''

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('Get cor')
#         return self.cor_tinta

# Caneta = Caneta('Azul')
# print(Caneta.get_cor())
# print(Caneta.get_cor())
# print(Caneta.get_cor())
# print(Caneta.get_cor())
# print(Caneta.get_cor())

'''Exemplo 2'''

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('Property')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123456

Caneta = Caneta('Azul')
print(Caneta.cor)
print(Caneta.cor)
print(Caneta.cor)
print(Caneta.cor)
print(Caneta.cor_tampa)