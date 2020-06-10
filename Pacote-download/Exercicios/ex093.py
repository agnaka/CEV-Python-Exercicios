lista = {}
lista_gols = list()
lista['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
for i in range(0,(partidas)):
    lista_gols.append(int(input(f'Quantos gols na partida {i}? ')))
lista['gols'] = lista_gols
lista['total'] = sum(lista_gols)
print('=' * 50)
print(lista)
print('=' * 50)
for k, v in lista.items():
    print(f'O campo {k} tem o valor {v}.')
print('=' * 50)
print(f'O jogador {lista["nome"]} jogou {partidas} partidas.')
for p, g in enumerate(lista_gols):
    print(f'   => Na partida {p}, fez {g} gols.')
print(f'Foi um total de {lista["total"]}')
print()
print('FIM')
