# Operadores logicos
# and (e) or (ou) not (nao)
# and - todas as condicoes precisa, ser 
# verdadeiras
# Se qualquer valor for considerado falso,
# a expressao inteira sera avaliada naquele valor
# Sao considerados falsy (que vc ja viu)
# 0 0,0 '' False
# Tambem existe o tique None que e usado para representar um nao valor
# if True:

# Avaliacao curto circuito
# print (True and False and True)


# entrada = input ('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')


# senha_permitida = '123456'

# if entrada == 'E' or entrada == senha_permitida:
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print ('Entrar')
# else:
#         print ('Sair')

senha = input('Senha: ') or 'Sem senha'
print (senha)