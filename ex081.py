lista = list()
cont = 0
resp = ''
while resp in 'Ss':
    num = int(input('digite um numero para adicionar na sua lista  '))
    if cont == 0 or num > lista[-1]:
        lista.append(num)
        cont += 1
    else:
        for pos, val in enumerate(lista):
            if num < lista[pos]:
                lista.insert(pos,num)
                cont += 1
                break
    resp = str(input('Deseja adicionar mais um numero? [S/n]')).strip().split()[0].upper()
    print(lista)
if 5 in lista:
    resp = 'SIM'
else:
    resp = 'NÃO'
print(f'Foram adicionados {cont} numeros na lista')
print(f' a lista de valores ordenadas em forma descrescente é {sorted(lista, reverse=True)}')
print(f' o valor 5 está ou não na lista? {resp} esta na lista')

