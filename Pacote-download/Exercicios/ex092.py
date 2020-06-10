from datetime import date
lista = {}
lista['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
lista['idade'] = (date.today().year) - ano
lista['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if lista['ctps'] != 0:
    lista['contratação'] = int(input('Ano de Contratação: '))
    lista['salário'] = float(input("Salário: R$:"))
    lista['aposentadoria'] = (lista['contratação'] + 35) - (date.today().year) + lista['idade']
print('-=' * 30)
print(lista)
for k, v in lista.items():
    print(f'  - {k} tem o valor {v}')
print()
print('FIM')
