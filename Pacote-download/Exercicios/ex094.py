lista = list()
lista_p = dict()
soma =  0
while True:
    lista_p['nome'] = str(input('Nome: '))
    while True:
        lista_p['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if lista_p['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    lista_p['idade'] = int(input('Idade: '))
    soma += lista_p['idade']
    lista.append(lista_p.copy())
    while True:
        seguir = input('Quer continuar? [S/N] ').strip().upper()[0]
        if seguir in 'SN':
            break
        print('ERRO! Responda apaenas S ou N. ')
    if seguir == 'N':
        break
print('=' * 40)
print(f'- O grupo tem {len(lista)} pessoas cadastradas. ')
media = soma / len(lista)
print(f'- A média de idade é de {media:.2f} anos')
print(f'- As mulheres cadastradas foram: ', end = ' ')
for d in lista:
    if d["sexo"] == 'F':
        print(f'{d["nome"]}', end  = ' ')
print()
print(f'- Lista das pessoas que estão acima da média: ')
for p in lista:
    if p["idade"] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end = '')
        print()
# print(lista)
print('<< ENCERRADO >>')