def maior(*num):
    nmaior = 0

    for c, v in enumerate(num[0]):
        if c == 0:
            nmaior = num[0][0]
        elif c > 0:
            if num[0][c] > nmaior:
                nmaior = num[0][c]
    print(f'Analisando os valores passados...')
    for c, v in enumerate(num[0]):
        print(f'{v}', end=' ')
    print()
    print(f'Foram informados {len(num[0])} valores ao todo.')
    print(f'O maior valor informado foi {nmaior}')
    print('#+' * 30)
    print('\n')


# programa principal
l1 = [2, 6, 3, 7, 8, 9, 4, 3, 8]
l2 = [87, 32, 83, 23, 545, 7]

maior(l1)
maior(l2)
