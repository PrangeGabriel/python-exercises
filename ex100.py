def sorteia():
    from random import randint
    from time import sleep
    numeros.clear()
    for c in range(1, 6):
        numeros.append(randint(1, 9))
    print(f'Sorteando 5 valores da lista:')
    for n in numeros:
        print(n, end=' ')
        sleep(0.2)
    print('Fim do sorteio')
    print('#-' * 30)
    print('\n')


def somaPar():
    soma = 0
    for c, v in enumerate(numeros):
        if numeros[c] % 2 == 0:
            print(numeros[c], end=' ')
            soma += numeros[c]
    print(f' a soma dos numeros pares deu {soma}')
    print('#*' * 30)


# programa principal
numeros = []
sorteia()
sorteia()
print('#-' * 30)
somaPar()
