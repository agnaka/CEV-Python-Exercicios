valores = list()
for cont in range(0,5):
    valores.append(int(input(f'Digite un valor para a posição {cont}: ')))
print('=-' * 20)
print(f'Você digitou os valores {valores}')
maior = max(valores)
menor = min(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end = '')
for c, ma in enumerate(valores):
    if ma == maior:
        print(f'{c}', end = '...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end = '')
for c, mi in enumerate(valores):
    if mi == menor:\
            print(f'{c}', end = '...')

'''if max(valores) in valores[:]:
    print(f'O maior valor digitado foi {max(valores)} nas posições {valores.index(max(valores))}', end = ',,,')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ')'''