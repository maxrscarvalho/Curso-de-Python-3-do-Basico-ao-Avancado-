'''Repeticoes

While (enquanto)''' #Executa uma acao enquanto uma condicao for verdeira 

# Loop infinito = Quando um codigo nao tem fim.

condicao = True 

while condicao:
    nome = input('Digite o seu nome: ')
    print('Seu nome e {}'.format(nome))

    if nome == 'sair':
        break

print('Acabou!')

