def leiaint(texto):
    while True:
        num = str(input(texto))
        try:
            num = int(num)

        except Exception as erro:
            print(f'\033[35mErro! digite um numero valido. Erro do tipo {erro.__class__}\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\nEntrada de dados interrompida pelo usuario')
            return 0
        else:
            return num


def leiaFloat(texto):
    while True:
        num = str(input(texto))
        try:
            num = float(num)
        except (ValueError, TypeError):
            print(f'\033[33mErro! digite um numero real valido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n Entrada de dados interrompida pelo usuario')
            return 0
        else:
            return num


# programa principal
n = leiaint('digite um numeroooo ')
n2 = leiaFloat('digite um numero real')
print(f' Voce acabou de digitar o numero {n} \n e um numero real {n2}')
