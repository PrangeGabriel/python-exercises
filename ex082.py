lista = list()
resp = ''
while resp in 'Ss':
    num = int(input('Digite um valor para adicionar a lista'))
    lista.append(num)
    resp = str(input('quer adicionar mais um numero? [S/n]')).strip().split()[0].upper()

listapar = []
listaimp = []
for n in lista:
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimp.append(n)
print(f'a lista gerada foi {lista}')
print(f'a lista de numeros pares gerada foi {listapar}')
print(f'a lista de numeros impares gerada foi {listaimp}')

