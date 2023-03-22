nome = 'Max Carvalho'
altura = 1.80
peso = 95
imc = peso / altura ** 2
 
# Max Carvalho tem 1.8 de altura
# pesa 95 quilos e seu IMC e    
# 29.320987654320987

# f-strings

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa, {peso}, quilos e seu IMC e'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2) 
print(linha_3)
