import random
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')

alunos = [n1, n2, n3, n4]
print('O aluno que vai apagar o quadro é {}{}'. format('\033[1;33m',random.choice(alunos)))


'''quadro = random.sample(alunos, 1)
print('O aluno que vai apagar o quadro é {}'.format(quadro))'''
