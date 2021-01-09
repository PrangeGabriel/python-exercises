a = int(input('digite o primeiro numero'))
b = int(input('digite o segundo numero'))
opção = 0
while opção != 5:
    opção = int(input('''\nQual operação deseja fazer
    [1] somar
    [2] multiplicar
    [3] maior
    [4] digitar novos numeros 
    [5] sair do programa '''))
    if opção == 1:
        print('\033[32m operação de soma {} + {} = {}'.format(a, b, a + b),'\033[m')
    elif opção == 2:
        print('\033[33m operação de multiplicação  {} * {} = {}'.format(a, b, a * b),'\033[m')
    elif opção == 3:
        if a > b:
            print('o numero {} é maior do que {}'.format(a, b))
        else:
            print('o numero {} é maiorr do que {}'.format(b, a))
    elif opção == 4:
        a = int(input('digite o primeiro numero'))
        b = int(input('digite o segundo numero'))
print('Saiu da sessao')
