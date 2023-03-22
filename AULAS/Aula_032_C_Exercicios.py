'''Faca um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou 
menos escreva "Seu nome e curto", se tiver entre 5 e 6 letras, escreva 
" Seu nome e normal"; maior que 6 escreva "Seu nome e muito grande".'''

nome = input('Digite o seu primeiro nome: ')
tam_nome = len(nome)
print('seu Nome tem {} letras'.format(tam_nome))

if tam_nome >=1: 
    if tam_nome <= 4:
        print('Seu nome e curto')
    elif tam_nome >= 5 and tam_nome <= 6:
        print('Seu nome e normal')
    else: 
        print('Seu nome e muito grande')

else: 
    print('Digite mais uma letra.')

