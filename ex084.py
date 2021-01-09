dados = list()
pessoas = list()
r = ''
listgorda = list()
listmagra = list()
while True:
    nome = str(input('Qual o nome da pessoa?'))
    massa = int(input(f'Qual a massa em kg de {nome}?'))
    pessoas.append(nome)
    pessoas.append(massa)
    dados.append(pessoas[:])
    pessoas.clear()
    r = str(input('Deseja cadastrar uma pessoa? [S/n]')).strip().split()[0].upper()
    print(r)
    if r in 'Nn':
        break
print(f'Foram cadastradas {len(dados)} pessoas na lista\n')
for p in dados:
    if p[1] >= 100:
        print(f'os mais gordinhos, com mais de 100kg foram {p[0]}')
    else:
        print(f'os mais magrinhos foram {p[0]}')
