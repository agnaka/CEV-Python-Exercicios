from operator import itemgetter
total = list()
lista = {}
lista_gols = list()
while True:
    lista.clear()
    lista_gols.clear()
    lista['nome'] = input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {lista["nome"]} jogou? '))
    for i in range(0,(partidas)):
        lista_gols.append(int(input(f'   Quantos gols na partida {i}? ')))
    lista['gols'] = lista_gols
    lista['total'] = sum(lista_gols)
    total.append(lista.copy())
    while True:
        seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
        if seguir in 'SN':
            break
        print('ERRO! Responda apenas S ou N ')
    if seguir == "N":
        break
    if seguir == 999:
        break
print('=' * 50)
# print(lista)
print(total)
print('=' * 50)
print('cod ', end= '')
for i in lista.keys():
    print(f'{i:<15}', end= '')
print()
for i, v in enumerate(total):
    print(f'{i:>3}', end = '')
    for d in v.values():
        print(f' {str(d):<14}', end = ' ')
    print('\n')
print('_' * 30)
while True:
    opc = int(input('Mostrar dados do qual jogador? (999 interrompe) '))
    if opc == 999:
        break
    if opc <= len(total):
        print(f'-- LEVANTAMENTO DO JOGADOR {total[opc]["nome"]}: ')
        for i, v in enumerate(total[opc]["gols"]):
            print(f'    No jogo {i} fez {v} gols.')
    if opc > len(total):
        print(f'ERRO! Não existe jogador com código {opc}! Tente novamente')
    print('-' * 30)
print()
print('<< VOLTE SEMPRE >>')
print('FIM')""