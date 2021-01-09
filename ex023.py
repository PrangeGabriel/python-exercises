from math import floor

numero = int(input('digite um numero de 0 a 9999 '))
###numero = str(input('digite um numero de 0 até 9999 '))
print('o numero digitado foi  {}'.format(numero))
###print('unidades: {}\n dezenas: {}\n centenas: {}\n milhar: {}'.format(numero[3],numero[2],numero[1],numero[0]))
print(floor(numero/1000))
print('unidades:{3}\n dezenas: {2}\n centenas: {1}\n milhares: {0}\n'.format(floor(numero/1000), floor(numero/100), floor(numero/10), floor(numero)))
