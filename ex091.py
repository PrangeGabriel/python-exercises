from random import randint
from operator import itemgetter
jogador = dict()
listajooj = list()

for total in range(1, 5):
    jogador['nome'] = 'jogador' + str(total)
    jogador['resultado'] = randint(1, 6)
    listajooj.append(jogador.copy())

print(listajooj)

count = 1
for elemento in listajooj:
    print(f'{count}ºlugar: ',end='')
    count += 1
    print(f' {elemento["nome"]} tirou {elemento["resultado"]} no dado')

#video exercicio 091 em 8min de video
ranking = sorted((jogo.items(), key = itemgetter(1), reverse=True))

