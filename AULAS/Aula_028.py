"""
Exercicio
Peca ao usuario para digitar seu nome
Peca ao usuario para digitar sua idade
Se o nome e idade forem digitados:
    Exiba: 
        Seu nome e {nome}
        Seu nome invertido e {nome invertido}
        Seu nome contem (ou nao) espacos
        Seu nome tem {n} letras
        A primeira letra do seu nome e {}
        A ultima letra do seu nome e {}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios."
"""

nome = input ('Digite o seu nome: ')
idade = input ('Digite a sua idade: ')

if nome and idade:
    print (f'Seu nome e {nome}')
    print (f'Seu nome invertido e {nome[ :: -1]}')

    if ' ' in nome:
        print ('Seu nome contem espacos')
    else:
        print ('Seu nome nao contem espacos')

    print (f'Seu nome tem {len(nome)} letras')
    print (f'A primeira letra do seu nome e {nome[0]}')
    print (f'A ultima letra do seu nome e {nome[-1]}')

else:
    print ("Desculpe, voce deixou campos vazios.")

