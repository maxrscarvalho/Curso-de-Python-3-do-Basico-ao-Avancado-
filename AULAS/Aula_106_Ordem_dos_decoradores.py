def parametros_decorador(nome):                 # parametros do decorador
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'             # Concaternacao 
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='4')         # Parametros
@parametros_decorador(nome='3')         # Parametros
@parametros_decorador(nome='2')         # Parametros
@parametros_decorador(nome='1')        # parametros
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)