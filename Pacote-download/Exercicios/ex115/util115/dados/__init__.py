from Exercicios.ex115.util115 import titulos

def lista():
    titulos.titulo('PESSOAS CADASTRADAS')
    cadastro = open('cadastro.txt', 'r')
    for linha in cadastro:
        renglon = linha.split(',')
        print(f'{renglon[0]:<30} {renglon[1]:<3} anos')


def opcao():
    while True:
        try:
            opcao = int(input('\033[32mSua Opção:\033[m '))
        except Exception as erro:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
        else:
            if 0 > opcao < 3:
                continue
        break



def novo():
    titulos.titulo('NOVO CADASTRO')
    while True:
        nome = input('Nome: ').strip()
        if nome == '':
            print(f'\033[31mERRO: o nome não pode ficar vazio.\033[m')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except Exception as erro:
            print(f'\033[31mERRO: por favor digite um número inteiro válido.\033[m')
        else:
            cadastro = open('cadastro.txt', 'a')
            cadastro.write(nome + ', ')
            cadastro.write(str(idade) + ', \n')
            cadastro.close()
            print(f'Novo registro de {nome} adicinado.')
            break
