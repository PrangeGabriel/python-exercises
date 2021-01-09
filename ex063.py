num = int(input('Vizualizador de sequencia fibonacci, digite um numero'))
cont = 2
ele1 = 0
ele2 = 1
ele3 = 0
print('{} > {}'.format(ele1, ele2), end='')
while cont < num:
    print(' > {}'.format(ele1 + ele2), end='')
    ele3 = ele1 + ele2
    ele1 = ele2
    ele2 = ele3
    cont += 1
