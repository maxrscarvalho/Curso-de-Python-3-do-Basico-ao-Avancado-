# dir, hasattr, getattr em python

string = 'Max'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else: 
    print('Nao existe o metodo', metodo)
    
