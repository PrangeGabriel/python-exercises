'''
numero = int(input('Calculadore de numeros fatoriais, digite um numero'))
cont = numero - 1
result = 1
while cont != 0:
    result = numero * cont
    cont -= 1
print('o fatorial de {} é igual a \n'.format(numero))
print('{}'.format(cont))
print(result, numero, cont)
'''

n = int(input('Calculador de numero fatorial, digite o numero'))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c > 1 else '=', end='')
    f *= c
    c -= 1
print('{}'.format(f))
