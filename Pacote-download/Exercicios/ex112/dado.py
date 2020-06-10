def leiadinheiro():
    preco = str(input('preço'))
    # print(preco.isnumeric())
    while preco.isnumeric() == False:
        print(f'\033[1;31mERRO: \"{preco}\" é um preço inválido!\033[m)')
        preco = str(input('Digite o preço: R$'))
        if preco.isnumeric() == True:
            break
    # preco = float(preco)
    # dobro = preco * 2
    # print(dobro)
    # print('FIM!')
