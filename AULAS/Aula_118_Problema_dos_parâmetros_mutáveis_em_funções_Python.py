def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []
cliente1 = adiciona_cliente('Max')
adiciona_cliente('Joana', cliente1)
adiciona_cliente('Fernando', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 = adiciona_cliente('Helena')
adiciona_cliente('Joana', cliente2)
print(cliente2)

cliente3 = adiciona_cliente('Moreira')
adiciona_cliente('Vivi', cliente3)
print(cliente3)