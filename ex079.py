listvalor = list()
valor = []
while valor != 'sair':
    valor = input('digite um valor para armazenar ou "sair" para sair do programa')
    if valor in listvalor:
        print('valor ja digitado, digite outro')
    else:
        listvalor.append(valor)

listvalor.pop()
print(f'os valores unicos em ordem crescente são {sorted(listvalor)}')

