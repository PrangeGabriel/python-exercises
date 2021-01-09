from random import randint

jooj = cont = numero = result = 0
while True:
    comp = randint(1, 3)
    jooj = str(input('PAR OU IMPAR?')).upper()[0]
    numero = int(input('Joga ai então'))
    result = (comp + numero) % 2
    if jooj is 'Pp' and result == 0:
        print('Parabens voce ganhou')
        cont += 1
    elif jooj in 'Ii' and result == 1:
        print('Parabens voce ganhou tambem')
        cont += 1
    else:
        print(f'Voce perdeu, mas ganhou {cont} vezes seguidas')
        break
