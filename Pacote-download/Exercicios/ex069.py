masc = fem = id_18 = 0
while True:
    print('-' * 25)
    print('CADASTRE UMA PESSOA'.center(25,' '))
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade > 18:
        id_18 += 1
#    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    sexo = " "
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F]: ')).strip().upper()
    if sexo == 'M':
        masc += 1
    elif sexo == 'F' and idade < 20:
        fem += 1
    print('-' * 25)
#    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    continuar = " "
    while continuar not in 'SsNn':
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break
print(' FIM DO PROGRAMA '.center(25, '='))
print(f'Total de pessoas com mais de 18 anos: {id_18}')
print(f'Ao todo temos {masc} homens cadastrados')
print(f'E temos {fem} mulheres com menos de 20 anos')