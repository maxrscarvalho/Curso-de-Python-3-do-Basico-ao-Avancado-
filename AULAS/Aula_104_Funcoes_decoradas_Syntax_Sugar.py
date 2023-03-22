# Funcoes decoradoras e decoradores

'''Decorar = adicionar / remover / restringir / alterar
    Funcoes decoradoras sao funcoes que decoram outras funcoes
    Decoradores sao usadas para fazer o Python
    usar as funcoes decoradoras em outras funcoes.
    Decoradores sao "syntax sugar" (acucar sintatico)'''

def criar_funcao(func):                     # Funcao decoradora 
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += ' Quakl'
        print(f'O seu resultado foi {resultado}')
        print('ok, agora voce foi decorada')
        return resultado
    return interna                          # Funcao decoradora 

@criar_funcao                               # Funcao Syntax Sugar
def inverte_string(string):
    print(f'{inverte_string.__name__}')     # Declara o nome da funcao decorada
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


invertida = inverte_string("123")
print(invertida)

