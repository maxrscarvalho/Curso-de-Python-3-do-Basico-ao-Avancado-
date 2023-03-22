'''Repeticoes

While (enquanto)''' #Executa uma condicao for verdeira 
# loop infinito = Quando um codigo nao tem fim

'''Exemplo 1'''

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_colunas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=},{coluna=}')
        coluna += 1

    linha += 1


print('Acabou')