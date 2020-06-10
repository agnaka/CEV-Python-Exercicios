lista = []
while True:
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    lista.append([nome, [nota_1, nota_2], media])
    seguir = input('Quer continuar? [S/N]').strip().upper()[0]
    if seguir == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i , a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opc = int(input('Mostrar notas do qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO ...')
        break
    if opc <= len(lista) - 1:
        print(f'Notas de {lista[opc][0]} são {lista[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
print()
print('FIM')
