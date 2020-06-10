bra = ('Flamengo', 'Santos', 'Palmeiras','Grêmio','Athletico-Pr', 'São Paulo',
       'Internacional', 'Corinthians', 'Fortaleza', 'Goias', 'Bahia', 'Vasco',
       'Atlético-MG', 'Fluminense', 'Botafogo', 'Cerá', 'Cruzeiro', 'CSA',
       'Chapecoense', 'Avaí')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {bra}')
print('-=' * 20)
print(f'Os 5 primeiros são {bra[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são {bra[-4:]}')
print('-=' * 20)
print(f'Times em ordem alfabética: {sorted(bra)}')
print('-=' * 20)
print(f'O Chapecoense está na {(bra.index("Chapecoense")) + 1}º posição')
print('-' * 40)
print('FIM')
