num = [[], []]
for n in range(1,8):
    numero = int(input(f'Digite o {n}º valor: '))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print('-=' * 30)
print(sorted(num[0]))
print(f'Os valores pares digitados foram: \033[1;33m{sorted(num[0])}\033[m')
print(f'Os valores ímpares digitados foram: \033[1;35m{sorted(num[1])}\033[m')
print()
print('FIM')
