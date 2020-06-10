while True:
    try:
        i = int(input('Digite um número: '))
    except Exception as erro:
        print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        continue
    except (KeyboardInterrupt):
        print('\033[31mEntrada de daos interrompida pelo usuário.\033[m')
    else:
        while True:
            try:
                r = float(input('Digite um número Real: '))
                break
            except Exception as erro:
                print(f'\033[1;31mERRO! por favor, digite um número real válido.\033[m')
                continue
    break

print(f'O valor inteiro digitado foi {i} e o real foi {r}')

# finally:
    # vai executar sempre no final, pode ser um print('Volte Sempre')
