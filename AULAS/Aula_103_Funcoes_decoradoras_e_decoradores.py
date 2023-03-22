# Funcoes decoradoras e decoradores

'''Decorar = adicionar / remover / restringir / alterar
    Funcoes decoradoras sao funcoes que decoram outras funcoes
    Decoradores sao usadas para fazer o Python
    usar as funcoes decoradoras em outras funcoes.'''

def criar_funcao(func):                     # Funcao decoradora 
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('ok, agora voce foi decorada')
        return resultado
    return interna                          # Funcao decoradora 


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('Param deve ser uma string')


inverte_string_checando_parametro= criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)

