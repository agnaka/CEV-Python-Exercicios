from Exercicios.ex115.util115 import titulos

c = ('\033[m',          # 0 - sem cores
     '\033[0;31m',      # 1 - vermelho
     '\033[0;32m',      # 2 - verde
     '\033[0;33m',      # 3 - amarelo
     '\033[0;34m',      # 4 - azul
     '\033[0;35m',      # 5 - roxo
     '\033[7;30m'       # 6 - branco
     );

while True:
    titulos.titulo('MENU PRINCIPAL')
    titulos.subtitulo(1, 'Ver pessoas cadastradas')
    titulos.subtitulo(2, 'Cadastrar nova pessoa')
    titulos.subtitulo(3, 'Sair do Sistema')
    print(f'{c[0]}-' * 40)
    try:
        opcao = int(input(f'{c[2]}Sua Opção: '))
    except Exception as erro:
        print(f'{c[1]}ERRO! Digite uma opção válida!')
    else:
        if opcao == 1:
            titulos.titulo('PESSOAS CADASTRADAS')
            cadastro = open('cadastro.txt', 'r')
            for linha in cadastro:
                renglon = linha.split()
                print(f'{renglon[0]:<30} {renglon[1]} anos')
    #        cadastro.close()
        elif opcao == 2:
            titulos.titulo('NOVO CADASTRO')
            nome = input('Nome: ')
            try:
                idade = int(input('Idade: '))
            except Exception as erro:
                print(f'\033[31mERRO: por favor digite um número inteiro válido.\033[m')
            else:
                cadastro = open('cadastro.txt', 'a')
                cadastro.write(nome + ' ')
                cadastro.write(str(idade) + '\n')
                cadastro.close()
                print(f'Novo registro de {nome} adicinado.')
        elif opcao == 3:
            titulos.titulo('Saindo do sistema... Até logo!')
            break
        else:
            print(f'{c[1]}ERRO! Digite uma opção válida!')


