sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
print(sexo)
# while sexo not in 'MF':
while sexo != "M" and sexo != "F":
    sexo = str(input('Usted digitou errado, por favor digite novamente [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
print('FIM')