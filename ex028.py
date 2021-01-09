from random import randint
num = randint(1, 5)
esc = int(input('escolha um numero de 1 a 5'))
if esc == num:
    print('Parabens tu acertou')
else:
    print('Voce errou! O numero era {}'.format(num))
