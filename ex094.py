pessoa = dict()
listap = list()
while True:
    pessoa['nome'] = str(input('Nome?'))
    pessoa['sexo'] = str(input('Sexo biológico [M/F]?')).split()[0][0].upper()
    pessoa['idade'] = int(input('Idade? '))
    resp = str(input('Quer continuar? [S/n]')).split()[0].upper()
    listap.append(pessoa.copy())
    pessoa.clear()
    if resp in 'Nn':
        break

print('+=' * 30)
print(f'Foram cadastradas {len(listap)} pessoas na lista ')
soma = 0
for pes in listap:
    soma += pes['idade']
media = soma / len(listap)
print('+=' * 30)
print(f'A média das idades do grupo é {media} anos ')
print('+=' * 30)
print(f'As mulheres da lista são: ')
for pes in listap:
    if pes['sexo'] in 'Ff':
        print(pes['nome'])

print('\n', '+=' * 30)
print(f'As pessoas com idade acima da média são:', end=' ')
for pes in listap:
    if pes['idade'] > media:
        print(f'{pes["nome"]}')
