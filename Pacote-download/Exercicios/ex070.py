print('-' * 30)
print('LOJA SUPER BARATÃO'.center(30, ' '))
print('-' * 30)
preco = p_1000 = soma = menor = cont = 0
continuar = 'S'
while True:
    while continuar == 'S':
        produto = input('Nome do produto: ').strip()
        preco = float(input('Preço: R$'))
        cont += 1
        soma += preco
        continuar = ' '
        while continuar not in ('SN'):
            continuar = input('Quer continuar? [S/N]').strip().upper()
        if preco > 1000:
            p_1000 += 1
        if cont == 1 or preco < menor:
            menor = preco
            p_menor = produto
    if continuar == "N":
        print(' FIM DO PROGRAMA '.center(30, '-'))
        break
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {p_1000} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {p_menor} que custa R${menor:.2f}')
print('FIM')