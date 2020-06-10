print('-' * 42)
print(f'LISTAGEM DE PREÇOS'.center(42))
print('-' * 42)
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)
# print(lista)
# print(len(lista))
for item in range(0,len(lista), 2):
    print(f'{lista[item]:.<30}R$ {lista[item + 1]:>7.2f}')
#    for preco in range(0,len(lista), 1):
#        print(f'{lista[preco]}')
print('-' * 42)