from time import sleep


def contador(inicio, fim, passo):
    lista = list()
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1

    if fim > inicio:
        lista.append(inicio)
        while True:
            if lista[-1] + passo <= fim:
                lista.append(lista[-1] + passo)
            else:
                break
    if inicio > fim:
        lista.append(inicio)
        while True:
            if lista[-1] - passo >= fim:
                lista.append(lista[-1] - passo)
            else:
                break
    print('=-' * 30)
    print(f'a contagem de {inicio} até {fim} com {pas} de passo é a lista:')
    for c, v in enumerate(lista):
        print(f'{v}', end=' ', flush=True)
        sleep(0.3)
    print()
    print(f'FIM DA CONTAGEM')
    print('=-' * 30)
    print('\n')


# programa principal
ini = 1
fm = 10
pas = 1
contador(ini, fm, pas)

ini = 10
fm = 0
pas = 2
contador(ini, fm, pas)

ini = int(input('Inicio: '))
fm = int(input('Fim:'))
pas = int(input('Passo:'))

contador(ini, fm, pas)
