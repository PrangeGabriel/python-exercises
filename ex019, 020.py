from random import shuffle, choice
n1 = input('primeiro aluno: ')
n2 = input('aluno 2: ')
n3 = input('aluno 3: ')
n4 = input('ALUNO 4: ')
nomes = [n1, n2, n3, n4]
print('o nome do aluno escolhido foi {}\n'.format(choice(nomes)))
shuffle(nomes)
print('a ordem de apresentação de grupos será: \n {}'.format(nomes))
