print('=' * 30)
print('BANCO ANDRUCHITO'.center(30, " "))
print('=' * 30)
valor = int(input('Qual valor você quer sacar? R$'))
# saldo = 0
# saldo = valor - saldo
# while saldo != 0:
if valor >= 50:
    cinquenta = valor // 50
    saldo = valor - (cinquenta * 50 )
    print(f'Total de {cinquenta} cédulas de R$50')
if saldo >= 20:
    vinte = saldo // 20
    saldo = saldo - (vinte * 20)
    print(f'Total de {vinte} cédulas de R$20')
if saldo >= 10:
    dez = saldo // 10
    saldo = saldo - (dez * 10)
    print(f'Total de {dez} cédulas de R$10')
if saldo >= 1:
    um = saldo // 1
    print(f'Total de {um} cédulas de R$1')
    saldo = saldo - (um * 1)
print("=" * 30)
print('Volte sempre ao BANCO ANDRUCHITO!\nTenha um bom dia!')

'''while True:
    if valor >= 50:
        cinquenta = valor // 50
        saldo = valor - (cinquenta * 50)
        print(f'Total de {cinquenta} cédulas de R$50')
     elif saldo = saldo - cinquenta * 50
        vinte = saldo // 20
        print(f'Total de {vinte} cédulas de R$20')
        dez = (valor-(cinquenta * 50) - (vinte * 20)) // 10
        print(f'Total de {dez} cédulas de R$10')
        um = (valor-(cinquenta * 50) - (vinte * 20) - (dez * 10)) // 1
        print(f'Total de {um} cédulas de R1')'''
