def leiaint(texto):
    while True:
        num = str(input(texto))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[31mErro! digite um numero valido\033[m')
    return num


# programa principal
n = leiaint('digite um numeroooo ')
print(f' Voce acabou de digitar o numero {n}')
