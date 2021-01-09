from random import randint
from time import sleep

count = num = 0
listjooj = list()
numjooj = int(input('quantos palpites da mega sena você quer? '))
print('$_!_' * 4, f' SORTEANDO {numjooj} JOGOS ', '_!_$' * 4)
for j in range(0, numjooj):
    for n in range(0, 6):
        num = randint(1, 7)
        while True:
            if num not in listjooj:
                listjooj.append(num)
                break
            else:
                num = randint(1,7)

        # if n > 1:
        #     while True:
        #         if listjooj[-1] in listjooj[-2:-1]:
        #             listjooj.pop()
        #             listjooj.append(randint(1, 6))
        #             count += 1
        #         else:
        #             break
    listjooj.sort()
    # sleep(1)
    print(f'JOGO {j + 1}: ', end='')
    print(listjooj)
    listjooj.clear()
