tab = cont = 1
print('=+'*5, 'Gerador de tabuada', '+='*5)
while True:
    tab = int(input('Digite um numero para ver a sua tabuada'))
    if tab < 0:
        break
    print(f'A tabuada de {tab} é: \n')
    while True:
        print(f'{tab} x {cont} = {tab*cont}')
        cont += 1
        if cont == 10:
            cont = 0
            break
print('Tabuada finalizada')
