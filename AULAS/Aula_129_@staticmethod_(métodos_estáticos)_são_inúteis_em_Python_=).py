'''
@staticmethod (metodos estaticos) sao inuteis em python =)
Metodos estaticos sao metodos que estao dentro da classe, mas nao
tem acesso ao self nem ao cls.
Em resumo, sao funcoes que existem dentro da sua classe.'''


class classe:
    @staticmethod
    def funcao_que_esta_na_classe(*args, **kwargs):
        print('oi')

def funcao(*args, **kwargs):
    print('oi', args, kwargs)

c1 = classe()
funcao(1, 2, 3)
classe.funcao_que_esta_na_classe(nomeado=1)
funcao(nomeado=1)