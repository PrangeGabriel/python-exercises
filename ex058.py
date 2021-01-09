from random import randint

num = randint(1, 10)
tent = num + 1
count = 0
print('DESAFIO DA ADIVINHAÇÃO')
while tent != num:
    tent = int(input('Tente adivinhar o numero que o computador pensou'))
    count +=1
    if tent == num:
        print('parabens voce acertou na sua {}ª tentativa'.format(count))
    else:
        print('tente novamente')
print(num, '\n', tent)
