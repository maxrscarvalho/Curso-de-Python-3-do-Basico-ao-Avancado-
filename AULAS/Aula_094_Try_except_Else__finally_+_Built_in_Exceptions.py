
# try, except, else e finally

try:                            # O try pode ser usado com finally e except,  Nao pode ficar sozinho
    print('Abrir Arquivo')
    8/0

except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('Dividiu Zero')

except IndexError as error:
    print('IndexError')

except (NameError, ImportError):
    print('NameError, ImportError')

else: 
    print('Nao deu erro')

finally: 
    print('Fechar Arquivo')