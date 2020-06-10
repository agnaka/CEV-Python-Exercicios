prod = float(input('Digite o preço do produto: '))
desc = float(input('Insira o desconto desejado em porcentagem: '))
valor = prod-(prod*desc/100 )
print('O valor do produto com o desconto desejado é de \033[1;31m{:.2f}R$\033[m'.format(valor))