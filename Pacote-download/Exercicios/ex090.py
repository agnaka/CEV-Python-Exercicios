lista = {}
print()
lista['nome'] = str(input('Nome: '))
lista['media'] = float(input(f'Média de {lista["nome"]}: '))
print()
if lista["media"] >= 7:
    lista['situação'] = 'Aprovado'
elif 5 <= lista['media'] < 7:
    lista['situação'] = 'Recuperação'
else:
    lista['situação'] = 'Reprovado'
for k, v in lista.items():
    print(f'  - {k} é igual a {v}')
print('FIM')
