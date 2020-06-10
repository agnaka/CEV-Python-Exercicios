print('{:=^40}'.format('LOJAS BRAR'))
price = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Escolha a forma de pagamento:\n1- A vista dinheiro ou cheque: 10% de desconto\n2- Cartão á vista: 5% de desconto\n3- Cartão em 2x: mesmo preço\n4- Cartão 3x ou mais: 20% de juros\nQual é a opção? '))
if pagamento == 1:
    print('Valor do produto= R${:.2f}\nDesconto á vista de 10%= R${:.2f}\nPreço final= R${:.2f}'.format(price, price * .1, price-(price * .1)))
elif pagamento == 2:
    print('Valor do produto= R${:.2f}\nDesconto á vista no Cartão de 5%= R${:.2f}\nPreço final= R${:.2f}'.format(price, price * .05, price-(price * .05)))
elif pagamento == 3:
    print('Sua compra será parcelada em 2x de R${:.2F} SEM JUROS'.format(price / 2))
    print('Valor do produto= R${:.2f}\nDesconto Cartão até 2x de 0%= R${:.2f}\nPreço final= R${:.2f}'.format(price, price, price))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2F} COM JUROS'.format(parcelas, price / parcelas))
    print('Valor do produto= R${:.2f}\nJuros Cartão 3x ou mais de 20%= R${:.2f}\nPreço final= R${:.2f}'.format(price, price * .2, price+(price * .2)))
else:
    print('Você digitou uma opção errada')

