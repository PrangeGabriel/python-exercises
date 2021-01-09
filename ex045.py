from random import randint

lista = ['pedra', 'papel', 'tesoura']
jogador = int(input('escolha seu movimento entre pedra, papel ou tesoura'))
comp = randint(0, 2)

print('o pc esoclheu {}'.format(lista[comp]))
print('tu jogou {}'.format(lista[jogador]))
if comp == 0:
    if jogador == 0:
        print('empatou')
    elif jogador == 1:
        print('jogador vence')
    elif jogador == 2:
        print('matrix vence')
elif comp == 1:
    if jogador == 0:
        print('matrix vence')
    elif jogador == 1:
        print('empatou')
    elif jogador == 2:
        print('jogador vence')
elif comp == 2:
    if jogador == 0:
        print('jogador vence')
    elif jogador == 1:
        print('matrix vence')
    elif jogador == 2:
        print('empatou')
