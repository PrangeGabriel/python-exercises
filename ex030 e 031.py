num = int(input('Digita ai pacero'))
if num % 2 == 0:
    print('Numero par com certeza')
else:
    print('numero nao par')

dist = float(input('Qual a distancia da viagem em kilometros?'))
if dist <= 200:
    print('Com bandeira 1 o preço fica {}reais'.format(0.5*dist))
else:
    print('com bandeira 2 fica {}'.format(0.45*dist))