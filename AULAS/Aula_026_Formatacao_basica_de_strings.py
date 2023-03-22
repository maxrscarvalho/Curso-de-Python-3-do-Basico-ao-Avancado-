""""
Formatacao basica de strings 
s - strings
d e i - int
f - float 
.<numero de digitos>f
x e X - Hexadecimal
(caractere) (><^)(quantidade)
> - Esquerda
< - Direita
^ - centro
= 0>-100,.1f
sinal - + ou -
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print (f'{variavel}')
print (f'{variavel: >10}')
print (f'{variavel: <10}.')
print (f'{variavel: ^10}.')
print (f'{1000.4873648123746:0=+10,.1f}')
print (f' O hexadecimal de 1500 e {1500:08x}')
print (f'{variavel!r}')